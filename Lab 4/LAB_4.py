from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import numpy as np

# Create a function for our three-qubit circuit
def three_qubit_circuit():
    # Create a 3-qubit circuit with 3 classical bits
    qc = QuantumCircuit(3, 3)
    
    # Apply at least 4 gates
    qc.h(0)       # Hadamard on qubit 0
    qc.h(1)       # Hadamard on qubit 1
    qc.cx(0, 2)   # CNOT: control=q0, target=q2
    qc.cx(1, 2)   # CNOT: control=q1, target=q2
    qc.rz(np.pi/4, 2)  # Phase shift on qubit 2
    
    # Measure all qubits
    qc.measure([0, 1, 2], [0, 1, 2])
    
    return qc

# Create the circuit
circuit = three_qubit_circuit()

# Display the circuit
print("Circuit diagram:")
print(circuit.draw())

# Run the simulation
simulator = AerSimulator()
job = simulator.run(circuit, shots=1024)
result = job.result()
counts = result.get_counts()

# Plot the histogram of results
print("\nMeasurement results:")
plot_histogram(counts, title="Three-Qubit Circuit Results")
plt.show()

# Mathematical description
print("\nMathematical description of the circuit:")
print("Initial state: |000⟩")
print("After H on q0: (|0⟩ + |1⟩)/√2 ⊗ |00⟩")
print("After H on q1: (|0⟩ + |1⟩)/√2 ⊗ (|0⟩ + |1⟩)/√2 ⊗ |0⟩")
print("After CNOT(0,2): (|0⟩ ⊗ |0⟩ ⊗ |0⟩ + |0⟩ ⊗ |1⟩ ⊗ |0⟩ + |1⟩ ⊗ |0⟩ ⊗ |1⟩ + |1⟩ ⊗ |1⟩ ⊗ |0⟩)/2")
print("After CNOT(1,2): (|0⟩ ⊗ |0⟩ ⊗ |0⟩ + |0⟩ ⊗ |1⟩ ⊗ |1⟩ + |1⟩ ⊗ |0⟩ ⊗ |1⟩ + |1⟩ ⊗ |1⟩ ⊗ |0⟩)/2")
print("After RZ(π/4) on q2: (|000⟩ + e^(iπ/4)|011⟩ + e^(iπ/4)|101⟩ + |110⟩)/2")
print("This creates an entangled state where q2 (third qubit) is the parity (XOR) of q0 and q1, with additional phase.")