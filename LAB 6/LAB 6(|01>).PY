from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import numpy as np

def grover_algorithm_solution_10():
    # Create a 2-qubit quantum circuit
    qc = QuantumCircuit(2, 2)
    
    # Step 1: State Preparation - Apply Hadamard to create superposition
    qc.h(0)
    qc.h(1)
    qc.barrier()  # For visual separation in the circuit
    
    # Step 2: Grover's Oracle - Mark the solution state |10⟩
    # For solution |10⟩, we apply phase flip only to |10⟩
    qc.x(0)  # Flip for control
    # Note: q[1] is already in correct state for |10⟩ target (we want |0⟩)
    
    # Implement controlled-Z
    qc.h(1)
    qc.cx(0, 1)
    qc.h(1)
    
    qc.x(0)  # Unflip
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
circuit = grover_algorithm_solution_10()
job = simulator.run(circuit, shots=1024)
result = job.result()
counts = result.get_counts()
print("Grover's Algorithm Results for Solution |10⟩:", counts)

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
ax.set_title(f"Grover's Algorithm Results for Solution |10⟩\nTotal Shots: 1024")
ax.set_xlabel('State')
ax.set_ylabel('Count')

plt.tight_layout()
plt.show()