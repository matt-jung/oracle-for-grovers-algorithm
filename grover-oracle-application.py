import tkinter as tk
from qiskit import QuantumCircuit
import math
from qiskit.visualization import circuit_drawer
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

window = tk.Tk()
window.title("Oracle for Grover's Algorithm")


def generate_oracle_circuit():
    binary_string = user_string.get()

    if not all(i in ['0','1'] for i in binary_string):
        error_message['text'] = 'ERROR: Input must be a binary string'
        return

    error_message['text'] = ''
    system_size = len(binary_string)
    oracle = QuantumCircuit(system_size)

    qubits_to_flip = []
    control_qubits = [i for i in range(system_size-1)]
    target_qubit = system_size-1

    for i in range(system_size):
        if binary_string[i] == '0':
            qubits_to_flip.append(system_size-1-i)
    if qubits_to_flip:
        oracle.x(qubits_to_flip)
    oracle.mcp(math.pi, control_qubits, target_qubit)
    if qubits_to_flip:
        oracle.x(qubits_to_flip)

    ax.clear()
    circuit_drawer(oracle, output='mpl', ax=ax)
    canvas.draw()

top_frame = tk.Frame(master=window, bd=2, relief=tk.RAISED)

string_label = tk.Label(master=top_frame, text='Enter Binary String:')
user_string = tk.Entry(master=top_frame)
generate_button = tk.Button(master=top_frame, text='Generate Oracle Circuit', command=generate_oracle_circuit)


fig = plt.figure(figsize=(6, 4), facecolor='none')
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=window)
canvas_widget = canvas.get_tk_widget()

error_message = tk.Label(window, text='')

top_frame.pack(pady=10)
string_label.pack()
user_string.pack()
generate_button.pack()

canvas_widget.pack()
error_message.pack()

window.mainloop()
