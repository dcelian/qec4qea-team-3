from qiskit import QuantumCircuit
import random


def create_bit_state(bit=0):
    qc = QuantumCircuit(1, 1)

    if bit == 1:
        qc.x(0)

    qc.measure(0, 0)
    return qc

def create_bell():
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])
    return qc


def create_ghz(n=3):
    qc = QuantumCircuit(n, n)
    qc.h(0)
    for i in range(n - 1):
        qc.cx(i, i + 1)
    qc.measure(range(n), range(n))
    return qc


def create_random_circuit(n=3, depth=2):

    qc = QuantumCircuit(n, n)

    for _ in range(depth):
        for q in range(n):
            qc.ry(random.random(), q)

        for q in range(n - 1):
            qc.cx(q, q + 1)

    qc.measure(range(n), range(n))
    return qc