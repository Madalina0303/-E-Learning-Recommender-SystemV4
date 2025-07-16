

import matplotlib.pyplot as plt

labels = ['15 Qubits', '10 Qubits', '8 Qubits', '6 Qubits']
correct =  [96.6, 98.85, 99.77, 99.95]
wrong =    [3.4, 1.15, 0.23, 0.05]
perfect =  [93.47, 97.18, 99.39, 99.84]
mismatch = [6.53, 2.82, 0.61, 0.16]

labels = labels[::-1]
correct = correct[::-1]
wrong = wrong[::-1]
perfect = perfect[::-1]
mismatch = mismatch[::-1]

plt.rcParams.update({'font.size': 7})

fig, ax1 = plt.subplots(figsize=(6, 3.5))  # în inch

ax1.plot(labels, correct, marker='o', label='Correct', color='green')
ax1.plot(labels, perfect, marker='o', label='Perfect', color='blue')
ax1.set_ylabel('Accuracy Metrics (%)', color='black')
ax1.set_ylim(90, 100)
ax1.tick_params(axis='y')

ax2 = ax1.twinx()
ax2.plot(labels, wrong, marker='o', label='Wrong', color='red', linestyle='dashed')
ax2.plot(labels, mismatch, marker='o', label='Mismatch', color='orange', linestyle='dashed')
ax2.set_ylabel('Error Rate (%)', color='black')
ax2.set_ylim(0, 7)
ax2.tick_params(axis='y')

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
plt.legend(lines1 + lines2, labels1 + labels2, loc='upper center', ncol=4)


# plt.title('Metric Evolution by Qubit Count')
plt.xlabel('Qubits')
plt.grid(True)
plt.tight_layout()

fig.savefig("metrics.png", dpi=300)

plt.show()
