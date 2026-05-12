import numpy as np
import pandas as pd
import os

from qiskit_aer import AerSimulator
from qiskit import transpile

# IMPORTY Z MODUŁÓW LILIANY
from data_gen import create_bit_state
from noise_model import create_noise_model

def run_circuit(qc, sim, shots=2000):
    """Funkcja pomocnicza do uruchamiania obwodów z transpilacją."""
    tqc = transpile(qc, sim)
    job = sim.run(tqc, shots=shots, memory=True)
    return job.result().get_memory()

def generate_iq_points_from_results(results, true_state, sigma=0.5):
    """Generuje chmury I/Q na podstawie cyfrowych wyników symulacji."""
    center_0 = (1.0, 1.0)
    center_1 = (-1.0, -1.0)
    data = []
    
    for bit_str in results:
        # UWAGA: Zakładamy tu 1 kubit (wyniki '0' lub '1')
        if bit_str == '0':
            i, q = np.random.normal(center_0, sigma, 2)
        else:
            i, q = np.random.normal(center_1, sigma, 2)
        data.append([i, q, true_state])
        
    return data

def main():
    print("Inicjalizacja współdzielonego modelu szumu...")
    noise_model = create_noise_model()
    sim = AerSimulator(noise_model=noise_model)
    shots = 2000

    print("Generowanie obwodów...")
    qc_0 = create_bit_state(0)
    qc_1 = create_bit_state(1)

    print("Symulacja odczytów...")
    results_0 = run_circuit(qc_0, sim, shots)
    results_1 = run_circuit(qc_1, sim, shots)

    print("Tworzenie ciągłych danych I/Q (analogowych)...")
    data = []
    data += generate_iq_points_from_results(results_0, true_state=0)
    data += generate_iq_points_from_results(results_1, true_state=1)

    # Zapis do pliku
    df = pd.DataFrame(data, columns=['I', 'Q', 'State'])
    os.makedirs('data', exist_ok=True) 
    df.to_csv('data/iq_training_data.csv', index=False)

    print(f"Sukces! Zapisano {len(df)} próbek do: data/iq_training_data.csv")

    import matplotlib.pyplot as plt

    plt.scatter(
    df[df.State == 0]["I"],
    df[df.State == 0]["Q"],
    alpha=0.3,
    label="State 0"
)

    plt.scatter(
    df[df.State == 1]["I"],
    df[df.State == 1]["Q"],
    alpha=0.3,
    label="State 1"
)

    plt.xlabel("I")
    plt.ylabel("Q")
    plt.legend()
    plt.title("I/Q Calibration Data")

    plt.show()

if __name__ == "__main__":
    main()

