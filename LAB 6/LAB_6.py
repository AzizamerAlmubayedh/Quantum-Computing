from qiskit import QuantumCircuit
from qiskit.primitives import Sampler
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Bell state |Φ+⟩ = (|00⟩ + |11⟩)/√2
def bell_state_phi_plus():
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])
    return qc

# Bell state |Ψ+⟩ = (|01⟩ + |10⟩)/√2
def bell_state_psi_plus():
    qc = QuantumCircuit(2, 2)
    qc.x(1)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])
    return qc

# Bell state |Φ-⟩ = (|00⟩ - |11⟩)/√2
def bell_state_phi_minus():
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.z(1)
    qc.measure([0, 1], [0, 1])
    return qc

# Run the circuits
simulator = AerSimulator()
sampler = Sampler()

# Execute Bell states and display results
for name, circuit in [
    ("Bell state |Φ+⟩", bell_state_phi_plus()),
    ("Bell state |Ψ+⟩", bell_state_psi_plus()),
    ("Bell state |Φ-⟩", bell_state_phi_minus())
]:
    print(f"\nCircuit for {name}:")
    print(circuit.draw())
    
    job = simulator.run(circuit, shots=1024)
    result = job.result()
    counts = result.get_counts()
    
    print(f"Results for {name}:", counts)
    plot_histogram(counts, title=name)
    plt.show()

print("\nThe function in Qiskit that shows histogram is 'plot_histogram' from qiskit.visualization module")