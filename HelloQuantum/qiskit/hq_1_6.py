"""
Author: Ryan McKirdy
Date: 2/9/2020

Implementation of Hello Quantum Level 1, Puzzle 6 and its solution in qiskit
"""

from qiskit import(
  QuantumCircuit,
  execute,
  Aer)
from qiskit.visualization import plot_histogram

#%%

# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')

# Create a Quantum Circuit acting on the q register
circuit = QuantumCircuit(2)

#%%

# Setup
circuit.h(1)
circuit.x(0)

# Solve
circuit.h(1)
circuit.x(0)

# Map the quantum measurement to the classical bits
circuit.measure_all()
print(circuit.draw())

#%%

# Execute the circuit on the qasm simulator
job = execute(circuit, simulator, shots=100)

# Grab results from the job
result = job.result()

# Returns counts
counts = result.get_counts(circuit)
print("\nTotal count:",counts)
plot_histogram(counts).show()
# Draw the circuit