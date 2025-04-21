from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import numpy as np

def multiple_rz_gates():
    # Create quantum circuit
    qc = QuantumCircuit(2, 2)
    
    # Create initial superposition
    qc.h(0)
    
    # Apply multiple RZ gates
    qc.rz(np.pi/2, 0)   # First RZ gate (π/2)
    qc.rz(np.pi/3, 0)   # Second RZ gate (π/3)
    
    # Interfere
    qc.h(0)
    
    # Measure
    qc.measure(0, 0)
    
    return qc

# Run the circuit
simulator = AerSimulator()
circuit = multiple_rz_gates()
job = simulator.run(circuit, shots=1024)
result = job.result()
counts = result.get_counts()

print("Multiple RZ Gates Results:", counts)
plot_histogram(counts, title="Multiple RZ Gates Experiment")
plt.show()