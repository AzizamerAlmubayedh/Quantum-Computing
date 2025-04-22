from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import numpy as np

def grover_algorithm_solution_00():
    # Create a 2-qubit quantum circuit
    qc = QuantumCircuit(2, 2)
    
    # Step 1: State Preparation - Apply Hadamard to create superposition
    qc.h(0)
    qc.h(1)
    qc.barrier()  # For visual separation in the circuit
    
    # Step 2: Grover's Oracle - Mark the solution state |00⟩
    # For solution |00⟩, we apply phase flip only to |00⟩
    # The standard CZ implementation would mark state |11⟩, not |00⟩
    # So we need to negate the inputs first, apply CZ, then negate back
    qc.x(0)  # Negate inputs
    qc.x(1)  # Negate inputs
    
    # Implement controlled-Z
    qc.h(1)
    qc.cx(0, 1)
    qc.h(1)
    
    qc.x(0)  # Negate back
    qc.x(1)  # Negate back
    qc.barrier()  # For visual separation in the circuit
    
    # Step 3: Diffusion Operator (Grover's Diffusion)
    # Apply H gates to all qubits
    qc.h(0)
    qc.h(1)
    
    # Apply phase inversion about the mean
    qc.x(0)
    qc.x(1)
    
    # Apply controlled-Z
    qc.h(1)
    qc.cx(0, 1)
    qc.h(1)
    
    qc.x(0)
    qc.x(1)
    
    # Apply H gates again
    qc.h(0)
    qc.h(1)
    qc.barrier()  # For visual separation in the circuit
    
    # Measure the result
    qc.measure([0, 1], [0, 1])
    
    return qc

# Run the circuit
simulator = AerSimulator()
circuit = grover_algorithm_solution_00()
job = simulator.run(circuit, shots=1024)
result = job.result()
counts = result.get_counts()
print("Grover's Algorithm Results for Solution |00⟩:", counts)

# Create a dictionary with all possible states initialized to zero
all_states = {'00': 0, '01': 0, '10': 0, '11': 0}
    
# Update with measured counts
for state, count in counts.items():
    all_states[state] = count

# Plot the histogram with all states
fig, ax = plt.subplots(figsize=(10, 6))
states = ['00', '01', '10', '11']  # Ensure consistent ordering
values = [all_states[state] for state in states]

# Plot bars manually
bars = ax.bar(states, values, color='steelblue')

# Add title and labels - FIXED to avoid collision
ax.set_title(f"Grover's Algorithm Results for Solution |00⟩\nTotal Shots: 1024")
ax.set_xlabel('State')
ax.set_ylabel('Count')

plt.tight_layout()
plt.show()