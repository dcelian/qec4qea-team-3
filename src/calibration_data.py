import numpy as np
import pandas as pd
import os

from qiskit_aer import AerSimulator
from qiskit import transpile

from data_gen import create_bit_state
from noise_model import create_noise_model

def run_circuit(qc, sim, shots=2000):
    tqc = transpile(qc, sim)
    job = sim.run(tqc, shots=shots, memory=True)
    return job.result().get_memory()

def bitstream_to_iq(bitstream, true_state, sigma=0.4):
    data = []
    for b in bitstream:
        base = 1.0 if b == '0' else -1.0
        i = np.random.normal(base, sigma)
        q = np.random.normal(0.0, sigma)
        data.append([i, q, true_state, int(b)])
        
    return data

def run_calibration(shots=2000):
    noise_model = create_noise_model()

    qc_0 = create_bit_state(0)
    qc_1 = create_bit_state(1)

    # simulator
    sim = AerSimulator(noise_model=noise_model)

    # run experiments
    results_0 = run_circuit(qc_0, sim, shots)
    results_1 = run_circuit(qc_1, sim, shots)

    # build dataset
    data = []
    data += bitstream_to_iq(results_0, true_state=0)
    data += bitstream_to_iq(results_1, true_state=1)

    df = pd.DataFrame(
        data,
        columns=["I", "Q", "TrueState", "MeasuredBit"]
    )

    os.makedirs("data", exist_ok=True)
    df.to_csv("data/iq_calibration_data.csv", index=False)

    print("Saved: data/iq_calibration_data.csv")

if __name__ == "__main__":
    run_calibration()