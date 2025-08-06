from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

class QuantumGateExplorer:
    def __init__(self):
        self.simulator = AerSimulator()
        print("🎓 Welcome to Lesson 2: Quantum Gates!")
        print("=" * 50)
    
    def demonstrate_gate(self, gate_name, circuit, explanation):
        """Helper function to demonstrate any gate"""
        print(f"\n🚪 {gate_name.upper()} GATE")
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
            print(f"  |{outcome}⟩: {prob:.1f}%")
        
        return counts
    
    def lesson_2a_single_qubit_gates(self):
        """Part A: Single-Qubit Gates - Manipulating One Quantum Coin"""
        print("\n" + "="*60)
        print("PART A: SINGLE-QUBIT GATES")
        print("="*60)
        
        # 1. Identity Gate (do nothing)
        print("\n🔵 1. IDENTITY GATE (I) - The 'Do Nothing' Gate")
        qc_i = QuantumCircuit(1, 1)
        qc_i.id(0)  # Identity gate
        qc_i.measure(0, 0)
        self.demonstrate_gate("Identity", qc_i, 
                            "Does absolutely nothing! Qubit stays |0⟩")
        
        # 2. Pauli-X Gate (quantum NOT)
        print("\n🔴 2. PAULI-X GATE (X) - The Quantum NOT")
        qc_x = QuantumCircuit(1, 1)
        qc_x.x(0)  # Flip the qubit
        qc_x.measure(0, 0)
        self.demonstrate_gate("Pauli-X", qc_x, 
                            "Flips |0⟩ to |1⟩ and |1⟩ to |0⟩. Like classical NOT!")
        
        # 3. Hadamard Gate (superposition creator)
        print("\n🟡 3. HADAMARD GATE (H) - The Superposition Master")
        qc_h = QuantumCircuit(1, 1)
        qc_h.h(0)
        qc_h.measure(0, 0)
        self.demonstrate_gate("Hadamard", qc_h, 
                            "Creates perfect 50/50 superposition. |0⟩ + |1⟩!")
        
        # 4. Pauli-Z Gate (phase flip)
        print("\n🟣 4. PAULI-Z GATE (Z) - The Invisible Phase Flipper")
        qc_z = QuantumCircuit(1, 1)
        qc_z.h(0)  # First create superposition
        qc_z.z(0)  # Then apply phase flip
        qc_z.h(0)  # Convert phase back to amplitude to see effect
        qc_z.measure(0, 0)
        self.demonstrate_gate("Pauli-Z", qc_z, 
                            "Flips the phase. Invisible unless you look carefully!")
        
        # 5. Pauli-Y Gate (combination flip)
        print("\n🟠 5. PAULI-Y GATE (Y) - The Combo Flipper")
        qc_y = QuantumCircuit(1, 1)
        qc_y.y(0)
        qc_y.measure(0, 0)
        self.demonstrate_gate("Pauli-Y", qc_y, 
                            "Does X and Z flip combined! |0⟩ → -i|1⟩")
    
    def lesson_2b_rotation_gates(self):
        """Part B: Rotation Gates - Fine Control"""
        print("\n" + "="*60)
        print("PART B: ROTATION GATES - PRECISION CONTROL")
        print("="*60)
        
        import math
        
        # RX Gate - X rotation
        print("\n🔄 6. RX GATE - Rotate Around X-axis")
        qc_rx = QuantumCircuit(1, 1)
        qc_rx.rx(math.pi/4, 0)  # 45-degree rotation
        qc_rx.measure(0, 0)
        self.demonstrate_gate("RX(π/4)", qc_rx, 
                            "Rotates qubit 45° around X-axis. Partial superposition!")
        
        # RY Gate - Y rotation  
        print("\n🔄 7. RY GATE - Rotate Around Y-axis")
        qc_ry = QuantumCircuit(1, 1)
        qc_ry.ry(math.pi/3, 0)  # 60-degree rotation
        qc_ry.measure(0, 0)
        self.demonstrate_gate("RY(π/3)", qc_ry, 
                            "Rotates qubit 60° around Y-axis. Different superposition!")
        
        # RZ Gate - Z rotation
        print("\n🔄 8. RZ GATE - Rotate Around Z-axis")
        qc_rz = QuantumCircuit(1, 1)
        qc_rz.h(0)  # Create superposition first
        qc_rz.rz(math.pi/2, 0)  # 90-degree phase rotation
        qc_rz.h(0)  # Convert back to see effect
        qc_rz.measure(0, 0)
        self.demonstrate_gate("RZ(π/2)", qc_rz, 
                            "Rotates the quantum phase. Very subtle!")
    
    def lesson_2c_two_qubit_gates(self):
        """Part C: Two-Qubit Gates - Quantum Teamwork"""
        print("\n" + "="*60)
        print("PART C: TWO-QUBIT GATES - QUANTUM TEAMWORK")
        print("="*60)
        
        # CNOT Gate (controlled-X)
        print("\n⚡ 9. CNOT GATE (CX) - The Entangler")
        qc_cnot = QuantumCircuit(2, 2)
        qc_cnot.h(0)  # Put control in superposition
        qc_cnot.cx(0, 1)  # Apply controlled-X
        qc_cnot.measure_all()
        self.demonstrate_gate("CNOT", qc_cnot, 
                            "If control=1, flip target. Creates entanglement!")
        
        # Controlled-Z Gate
        print("\n⚡ 10. CONTROLLED-Z GATE (CZ) - The Phase Entangler")
        qc_cz = QuantumCircuit(2, 2)
        qc_cz.h(0)  # Superposition on first qubit
        qc_cz.h(1)  # Superposition on second qubit
        qc_cz.cz(0, 1)  # Controlled-Z
        qc_cz.h(0)  # Convert phases back
        qc_cz.h(1)
        qc_cz.measure_all()
        self.demonstrate_gate("Controlled-Z", qc_cz, 
                            "Phase flip if both qubits are |1⟩. Symmetric entanglement!")
        
        # SWAP Gate
        print("\n🔄 11. SWAP GATE - The Quantum Switcher")
        qc_swap = QuantumCircuit(2, 2)
        qc_swap.x(0)  # Put first qubit in |1⟩
        qc_swap.swap(0, 1)  # Swap the qubits
        qc_swap.measure_all()
        self.demonstrate_gate("SWAP", qc_swap, 
                            "Swaps the states of two qubits. |01⟩ becomes |10⟩!")
    
    def lesson_2d_gate_combinations(self):
        """Part D: Gate Combinations - Building Quantum Algorithms"""
        print("\n" + "="*60)
        print("PART D: GATE COMBINATIONS - QUANTUM RECIPES")
        print("="*60)
        
        # Quantum teleportation preparation circuit
        print("\n🌟 12. QUANTUM TELEPORTATION SETUP")
        qc_teleport = QuantumCircuit(3, 3)
        
        # Step 1: Create the state to teleport
        qc_teleport.h(0)  # Create |+⟩ state to teleport
        
        # Step 2: Create entangled pair
        qc_teleport.h(1)
        qc_teleport.cx(1, 2)
        
        # Step 3: Bell measurement
        qc_teleport.cx(0, 1)
        qc_teleport.h(0)
        
        qc_teleport.measure_all()
        self.demonstrate_gate("Teleportation Setup", qc_teleport, 
                            "First steps of quantum teleportation protocol!")
        
        # Quantum Fourier Transform (2-qubit)
        print("\n🌟 13. QUANTUM FOURIER TRANSFORM (2-qubit)")
        qc_qft = QuantumCircuit(2, 2)
        import math
        
        # Prepare interesting initial state
        qc_qft.x(0)
        
        # Apply 2-qubit QFT
        qc_qft.h(0)
        qc_qft.cp(math.pi/2, 1, 0)  # Controlled phase
        qc_qft.h(1)
        qc_qft.swap(0, 1)  # Swap to get correct order
        
        qc_qft.measure_all()
        self.demonstrate_gate("QFT", qc_qft, 
                            "Quantum Fourier Transform - foundation of many algorithms!")
    
    def professor_summary(self):
        """Professor's final wisdom"""
        print("\n" + "🎓" * 60)
        print("PROFESSOR'S QUANTUM GATE WISDOM")
        print("🎓" * 60)
        
        print("""
🔑 KEY INSIGHTS YOU JUST LEARNED:

1. SINGLE-QUBIT GATES:
   • X, Y, Z: The three Pauli gates (basic flips)
   • H: Creates/destroys superposition (the most important!)
   • RX, RY, RZ: Precise rotations for fine control

2. TWO-QUBIT GATES:
   • CNOT: Creates entanglement (quantum magic!)
   • CZ: Phase entanglement (more subtle)
   • SWAP: Moves quantum information around

3. QUANTUM UNIVERSALITY:
   • Any quantum computation can be built from these basic gates!
   • It's like having quantum LEGO blocks

4. THE MEASUREMENT PARADOX:
   • Gates are reversible (you can undo them)
   • Measurement is irreversible (destroys superposition)
   • This is why quantum computing is so different!

🏆 CHALLENGE FOR LESSON 3:
Try combining gates in new ways! What happens if you apply:
- H, then X, then H again?
- Multiple CNOT gates in a row?
- Can you create a 3-qubit entangled state?

Remember: Every quantum algorithm ever invented uses just these basic gates!
You now have the complete quantum toolbox! 🛠️⚛️
        """)

def main():
    """Run the complete Lesson 2"""
    prof = QuantumGateExplorer()
    
    # Run all parts of the lesson
    prof.lesson_2a_single_qubit_gates()
    prof.lesson_2b_rotation_gates()
    prof.lesson_2c_two_qubit_gates()
    prof.lesson_2d_gate_combinations()
    prof.professor_summary()
    
    print("\n✨ Lesson 2 Complete! You're becoming a quantum gate master! ✨")

if __name__ == "__main__":
    main()