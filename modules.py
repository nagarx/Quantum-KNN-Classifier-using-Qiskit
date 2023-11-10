from qiskit import QuantumCircuit, QuantumRegister

def swap_test(N):
    '''
    `N`: Number of qubits of the quantum registers.
    '''
    a = QuantumRegister(N, 'a')
    b = QuantumRegister(N, 'b')
    d = QuantumRegister(1, 'd')
    
    # Quantum Circuit
    qc_swap = QuantumCircuit(name = ' SWAP \nTest')
    qc_swap.add_register(a)
    qc_swap.add_register(b)
    qc_swap.add_register(d)
    
    qc_swap.h(d)
    for i in range(N):
        qc_swap.cswap(d, a[i], b[i])
            
    qc_swap.h(d)    
    
    return qc_swap