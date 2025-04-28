from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import numpy as np

def bb84_protocol_no_eve():
    """
    Implements the BB84 quantum key distribution protocol without Eve.
    Uses 6 qubits as specified in the lab document.
    """
    # Create a 6-qubit quantum circuit with 6 classical bits for measurement
    qc = QuantumCircuit(6, 6)
    
    # Step 1: Alice's Preparation
    # Alice encodes bits using Z-basis (|0⟩, |1⟩) and X-basis (|+⟩, |-⟩)
    
    # Qubits 0, 1, 2: Z-basis
    # Qubit 0: Bit value 0 in Z-basis (|0⟩) - no gates needed
    # Qubit 1: Bit value 1 in Z-basis (|1⟩) - apply X gate
    qc.x(1)
    # Qubit 2: Bit value 0 in Z-basis (|0⟩) - no gates needed
    
    # Qubits 3, 4, 5: X-basis
    # Qubit 3: Bit value 0 in X-basis (|+⟩) - apply H gate
    qc.h(3)
    # Qubit 4: Bit value 1 in X-basis (|-⟩) - apply H then Z gate
    qc.h(4)
    qc.z(4)
    # Qubit 5: Bit value 1 in X-basis (|-⟩) - apply H then Z gate
    qc.h(5)
    qc.z(5)
    
    qc.barrier()  # For visual separation in the circuit
    
    # Step 2: Bob's Measurement
    # Bob randomly chooses measurement bases
    
    # Qubits 0, 1: Bob measures in Z-basis - no gates needed
    # Qubit 2: Bob measures in X-basis - apply H before measurement
    qc.h(2)
    # Qubit 3: Bob measures in X-basis - apply H before measurement
    qc.h(3)
    # Qubit 4: Bob measures in Z-basis - apply H to convert from X to Z basis
    qc.h(4)
    # Qubit 5: Bob measures in X-basis - apply H before measurement
    qc.h(5)
    
    # Measure all qubits
    qc.measure(range(6), range(6))
    
    return qc

def bb84_protocol_with_eve():
    """
    Implements the BB84 quantum key distribution protocol with Eve eavesdropping.
    Uses 6 qubits as specified in the lab document.
    """
    # Create a 6-qubit quantum circuit with 6 classical bits for measurement
    qc = QuantumCircuit(6, 6)
    
    # Step 1: Alice's Preparation - same as the version without Eve
    # Qubits 0, 1, 2: Z-basis
    # Qubit 0: Bit value 0 in Z-basis (|0⟩) - no gates needed
    # Qubit 1: Bit value 1 in Z-basis (|1⟩) - apply X gate
    qc.x(1)
    # Qubit 2: Bit value 0 in Z-basis (|0⟩) - no gates needed
    
    # Qubits 3, 4, 5: X-basis
    # Qubit 3: Bit value 0 in X-basis (|+⟩) - apply H gate
    qc.h(3)
    # Qubit 4: Bit value 1 in X-basis (|-⟩) - apply H then Z gate
    qc.h(4)
    qc.z(4)
    # Qubit 5: Bit value 1 in X-basis (|-⟩) - apply H then Z gate
    qc.h(5)
    qc.z(5)
    
    qc.barrier()  # For visual separation between Alice and Eve
    
    # Step 2: Eve's Interception
    # Eve chooses measurement bases (some match Alice, some don't)
    
    # Qubit 0: Eve measures in X-basis - apply H before measurement
    qc.h(0)
    # Qubit 1: Eve measures in Z-basis - no gates needed
    # Qubit 2: Eve measures in X-basis - apply H before measurement
    qc.h(2)
    # Qubit 3: Eve measures in Z-basis - convert from X to Z basis
    qc.h(3)
    # Qubit 4: Eve measures in X-basis - apply H (already in X basis after H,Z)
    qc.h(4)  # This will cancel out the effect of Z, leaving it in X basis
    # Qubit 5: Eve measures in Z-basis - convert from X to Z basis
    qc.h(5)
    
    # Eve resends qubits after her measurement
    # Qubit 0: Convert back to Z-basis 
    qc.h(0)
    # Qubit 2: Convert back to Z-basis
    qc.h(2)
    # Qubit 3: Already in Z-basis after Eve's measurement
    # Qubit 4: Convert back to Z-basis
    qc.h(4)
    # Qubit 5: Already in Z-basis after Eve's measurement
    
    qc.barrier()  # For visual separation between Eve and Bob
    
    # Step 3: Bob's Measurement - same as the version without Eve
    # Qubits 0, 1: Bob measures in Z-basis - no gates needed
    # Qubit 2: Bob measures in X-basis - apply H before measurement
    qc.h(2)
    # Qubit 3: Bob measures in X-basis - apply H before measurement
    qc.h(3)
    # Qubit 4: Bob measures in Z-basis - no gates needed (Eve already converted to Z)
    # Qubit 5: Bob measures in X-basis - apply H before measurement
    qc.h(5)
    
    # Measure all qubits
    qc.measure(range(6), range(6))
    
    return qc

# Run the BB84 protocol without Eve
simulator = AerSimulator()
circuit_no_eve = bb84_protocol_no_eve()
job_no_eve = simulator.run(circuit_no_eve, shots=1024)
result_no_eve = job_no_eve.result()
counts_no_eve = result_no_eve.get_counts()
print("BB84 Protocol Results Without Eve:", counts_no_eve)

# Run the BB84 protocol with Eve
circuit_with_eve = bb84_protocol_with_eve()
job_with_eve = simulator.run(circuit_with_eve, shots=1024)
result_with_eve = job_with_eve.result()
counts_with_eve = result_with_eve.get_counts()
print("\nBB84 Protocol Results With Eve:", counts_with_eve)

# Analyze and visualize the results
def analyze_results(counts_no_eve, counts_with_eve):
    """
    Analyzes and visualizes the results from both BB84 protocol circuits.
    """
    # Create figure with two subplots side by side
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))
    
    # Sort counts by binary value for consistent ordering
    sorted_counts_no_eve = dict(sorted(counts_no_eve.items()))
    sorted_counts_with_eve = dict(sorted(counts_with_eve.items()))
    
    # Plot histogram for circuit without Eve
    bars1 = ax1.bar(sorted_counts_no_eve.keys(), sorted_counts_no_eve.values(), color='steelblue')
    ax1.set_title("BB84 Results Without Eve\nTotal Shots: 1024")
    ax1.set_xlabel('Measured State')
    ax1.set_ylabel('Count')
    ax1.tick_params(axis='x', rotation=70)
    
    # Plot histogram for circuit with Eve
    bars2 = ax2.bar(sorted_counts_with_eve.keys(), sorted_counts_with_eve.values(), color='firebrick')
    ax2.set_title("BB84 Results With Eve\nTotal Shots: 1024")
    ax2.set_xlabel('Measured State')
    ax2.set_ylabel('Count')
    ax2.tick_params(axis='x', rotation=70)
    
    plt.tight_layout()
    plt.show()

analyze_results(counts_no_eve, counts_with_eve)