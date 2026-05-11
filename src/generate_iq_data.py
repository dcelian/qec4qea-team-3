import numpy as np
import pandas as pd
import os
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, ReadoutError

# 1. Przygotowanie obwodów
qc_0 = QuantumCircuit(1, 1)
qc_0.measure(0, 0)

qc_1 = QuantumCircuit(1, 1)
qc_1.x(0)
qc_1.measure(0, 0)

# 2. Budowa modelu szumu odczytu
p0_to_1 = 0.05
p1_to_0 = 0.10
readout_err = ReadoutError([[1 - p1_to_0, p1_to_0], [p0_to_1, 1 - p0_to_1]])

noise_model = NoiseModel()
noise_model.add_all_qubit_readout_error(readout_err)

sim = AerSimulator(noise_model=noise_model)
shots = 2000

job_0 = sim.run(qc_0, shots=shots, memory=True)
job_1 = sim.run(qc_1, shots=shots, memory=True)

results_0 = job_0.result().get_memory()
results_1 = job_1.result().get_memory()

# 4. Generacja ciągłego sygnału I/Q na podstawie cyfrowych błędów
center_0 = (1.0, 1.0)
center_1 = (-1.0, -1.0)
sigma = 0.5  # Rozmycie chmury

data = []

def generate_iq_point(bit_str, true_state):
    if bit_str == '0':
        i, q = np.random.normal(center_0, sigma, 2)
    else:
        i, q = np.random.normal(center_1, sigma, 2)
    return [i, q, true_state]

for bit in results_0:
    data.append(generate_iq_point(bit, true_state=0))

for bit in results_1:
    data.append(generate_iq_point(bit, true_state=1))

df = pd.DataFrame(data, columns=['I', 'Q', 'State'])

os.makedirs('data', exist_ok=True) 
df.to_csv('data/iq_training_data.csv', index=False)

print(f"Sukces! Wygenerowano {len(df)} punktów I/Q.")
print("Plik został zapisany jako: data/iq_training_data.csv")
