from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

def main():
    print("Welcome to Quantum Computing!")
    
    # Step 1: Create your first quantum circuit
    print("\n=== Step 1: Creating a Quantum Coin Flip ===")
    
    # Create circuit with 1 qubit and 1 classical bit
    qc = QuantumCircuit(1, 1)
    
    # Add Hadamard gate (creates 50/50 superposition)
    qc.h(0)
    
    # Measure the qubit
    qc.measure(0, 0)
    
    # Print the circuit
    print("Circuit diagram:")
    print(qc.draw())
    
    # Step 2: Run the circuit
    print("\n=== Step 2: Running on Simulator ===")
    
    # Set up simulator
    simulator = AerSimulator()
    
    # Run the circuit 1000 times
    job = simulator.run(transpile(qc, simulator), shots=1000)
    result = job.result()
    counts = result.get_counts()
    
    print(f"Results after 1000 shots: {counts}")
    
    # Calculate probabilities
    total_shots = sum(counts.values())
    for outcome, count in counts.items():
        prob = count / total_shots
        print(f"Outcome '{outcome}': {count} times ({prob:.1%})")
    
    # Step 3: Create an entangled pair (Bell state)
    print("\n=== Step 3: Creating Quantum Entanglement ===")
    
    bell_circuit = QuantumCircuit(2, 2)
    
    # Create superposition on first qubit
    bell_circuit.h(0)
    
    # Entangle with second qubit
    bell_circuit.cx(0, 1)
    
    # Measure both
    bell_circuit.measure([0, 1], [0, 1])
    
    print("Bell state circuit:")
    print(bell_circuit.draw())
    
    # Run Bell state
    job = simulator.run(transpile(bell_circuit, simulator), shots=1000)
    result = job.result()
    bell_counts = result.get_counts()
    
    print(f"Bell state results: {bell_counts}")
    print("Notice: Only '00' and '11' outcomes")
    
    try:
        from qiskit.visualization import plot_histogram
        
        # This will save plots as images you can view
        plot1 = plot_histogram(counts, title="Quantum Coin Flip")
        plot1.savefig("coin_flip_results.png")
        
        plot2 = plot_histogram(bell_counts, title="Bell State Results")
        plot2.savefig("bell_state_results.png")
        
        print("\nPlots saved as 'coin_flip_results.png' and 'bell_state_results.png'")
        
    except Exception as e:
        print(f"Visualization skipped: {e}")

if __name__ == "__main__":
    main()
    print("\nQuantum computing setup complete!")
