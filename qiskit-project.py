from qiskit import QuantumCircuit,transpile
from qiskit.circuit.library import GroverOperator
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from matplotlib import pyplot as plt
import math

def string_to_oracle(binary_string):
    """
    Generates an oracle circuit for a given binary string, to be used in Grover's algorithm

    Args:
        binary_string (str): The binary string for which the oracle circuit is created

    Returns:
        oracle (QuantumCircuit): A quantum circuit representing the oracle for the input binary string
    
    Raises:
        ValueError: If the input string is not a valid binary string.    

    Notes:
        -The oracle uses x and mcp (multi-control phase) gates with a phase shift of pi radians to invert the sign of the state corresponding to the input binary string.
    """
    if not all(bit in '01' for bit in binary_string):
        raise ValueError("Invalid binary string. Input must contain only '0' or '1'.")


    system_size=len(binary_string)
    oracle=QuantumCircuit(system_size)

    qubits_to_flip=[]
    control_qubits=[i for i in range(system_size-1)]
    target_qubit=system_size-1

    for i in range(system_size):
        if binary_string[i]=='0':
            qubits_to_flip.append(system_size-1-i)
    if qubits_to_flip:        
        oracle.x(qubits_to_flip)
    oracle.mcp(math.pi,control_qubits,target_qubit)
    if qubits_to_flip:        
        oracle.x(qubits_to_flip)

    return oracle

def grover_measurement(oracle):
    """
    Produces a histogram showing measurement outcomes of a cirucit running Grover's algorithm with a given oracle.

    Args:
        oracle (QuantumCircuit): A quantum circuit representing a given oracle in Grover's algiorithm
    
    Returns:
        None. Displays a graph of measurements

    Raises:
        TypeError: If the input is not a valid QuantumCircuit    
    """
    if not isinstance(oracle,QuantumCircuit):
        raise TypeError("Input must be a valid QuantumCircuit")
    
    system_size=oracle.num_qubits
    grover=GroverOperator(oracle)
    init=QuantumCircuit(system_size)
    init.h([i for i in range(system_size)])
    qc=init.compose(grover)
    qc.measure_all()

    sim=AerSimulator()
    t_qc=transpile(qc,sim)

    plot_histogram(sim.run(t_qc).result().get_counts())
    plt.show()


binary_string=input('Enter a binary string: ')
while not all(bit in '01' for bit in binary_string):
    binary_string=input('Enter a binary string: ')
grover_measurement(string_to_oracle(binary_string))

