from qiskit_aer.noise import NoiseModel
from qiskit_aer.noise.errors import depolarizing_error
from qiskit_aer.noise.errors import ReadoutError

def create_noise_model():

    noise_model = NoiseModel()
    # 1-qubit gate noise
    error_1q = depolarizing_error(0.01, 1)
    # 2-qubit gate noise
    error_2q = depolarizing_error(0.05, 2)
    # readout (measurement) noise

    readout_error = ReadoutError(
        [[0.95, 0.05],
         [0.10, 0.90]]
    )

    # apply gate noise
    noise_model.add_all_qubit_quantum_error(error_1q, ['h', 'x', 'ry'])
    noise_model.add_all_qubit_quantum_error(error_2q, ['cx'])

    # apply readout noise
    noise_model.add_all_qubit_readout_error(readout_error)

    return noise_model