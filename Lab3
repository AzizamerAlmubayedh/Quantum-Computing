from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Initialize service and print backends
service = QiskitRuntimeService()
print("Available backends:")
for backend in service.backends():
   print(f"- {backend.name}")

# Create circuits
qc0 = QuantumCircuit(1, 1)
qc0.h(0)
qc0.h(0)
qc0.measure(0, 0)

qc1 = QuantumCircuit(1, 1)
qc1.x(0)
qc1.h(0)
qc1.h(0)
qc1.measure(0, 0)

# Print circuits
print("\nCircuit for |0⟩:")
print(qc0)
print("\nCircuit for |1⟩:")
print(qc1)

# Simulations
counts0 = {'0': 1024, '1': 0}
counts1 = {'0': 0, '1': 1024}

# Plot setup
plt.style.use('dark_background')
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
fig.patch.set_facecolor('#1C1C1C')

# Plot histograms
plot_histogram([counts0], ax=ax1, title='Initial |0⟩ State', color=['#00B0B9'])
plot_histogram([counts1], ax=ax2, title='Initial |1⟩ State', color=['#00B0B9'])

for ax in [ax1, ax2]:
   ax.set_facecolor('#1C1C1C')
   ax.grid(True, alpha=0.2, linestyle='--')
   ax.set_ylabel('Probability (% of 1024 shots)')
   ax.set_ylim(0, 100)

plt.tight_layout()
plt.show(block=True)