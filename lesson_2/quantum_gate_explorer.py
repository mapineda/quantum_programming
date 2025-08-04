from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

class QuantumGateExplorer:
  def __init__(self):
    self.simulator = AerSimulator()
    print("Welcome to Lesson 2: Quantum Gates!")
    print("=" * 50)

  def demonstrate_gate(self, gate_name, circuit, explanation):
    """Helper function to demonstrate any Gate"""
    print(f"\n {gate_name.upper()} GATE")
    print("-" * 30)
    print(f"What it does: {explanation}")
    print("\nCircuit:")
    print(circuit.draw())

    # Run the circuit
    job = self.simulator.run(transpile(circuit, self.simulator), shots=1000)
    result = job.result()
    counts = result.get_counts()

    print(f"Results: {counts}")

    # Calculate probabilities for teaching
    total = sum(counts.values())
    for outcome, count in counts.items():
      prob = count / total * 100
      print(f" | {outcome}>: {prob:.1f}%")

    return counts
  
  def lesson2a_single_qubit_gates(self):
    """Part A: Single-Qubit Gates - Manipulating One Quantum Coin"""
    