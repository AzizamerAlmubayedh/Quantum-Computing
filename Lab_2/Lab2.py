from qiskit_ibm_runtime import QiskitRuntimeService
import qiskit
# Initialize the service
service = QiskitRuntimeService()

# List available backends
backend = 'ibm_brisbane'

backend_info = service.backend(backend)
# Print Qiskit version

print(f"Qiskit Version: {qiskit.__version__}")

# Print the number of qubits available on the backend
print(f"{backend} Has : {backend_info.num_qubits} qubits available!!!!")
