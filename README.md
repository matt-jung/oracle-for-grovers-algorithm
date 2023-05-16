# qiskit-introduction-course-project
The aim of this project is to create a program that takes a given binary string and creates an oracle circuit for Grover's search algorithm.

The 'n-qubit-invert' files are tests for flipping the sign of target n-qubit states for small n. For 2- and 3-qubit systems, the cz and ccz gates are sufficient for inverting the target state once it has been transformed to |11> or |111>. However, for larger systems these are substituted for the mcp (multi-control phase) gate with a phase shift of pi radians, which essentially does the same as the cz and ccz gates but can be generalised for larger n-qubit systems.
