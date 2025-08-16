import matplotlib.pyplot as plt
import numpy as np
PHB_1 = [0.11, 0.21, 0.63, 0.69, 0.87, 0.31]
PHB_2 = [0.078, 0.27, 0.55, 0.54, 0.48, 0.33]
PHB_3 = [0, 0.09, 0.21, 0.64, 0.59, 0.37]
labels = ["V4", "V5", "V6", "V7", "V8", "V9"] 
x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars
fig, ax = plt.subplots()
rects1 = ax.bar(x - width, PHB_1, width, color = "darksalmon", label='PHB_1')
rects2 = ax.bar(x, PHB_2, width, color = "powderblue", label='PHB_2')
rects3 = ax.bar(x + width, PHB_3, width, label='PHB_3', color = "lightslategrey")
ax.set_ylabel('g/l', fontsize = 12)
ax.set_title('Biosynthesis of PHB', fontsize = 20)
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend(loc = 2, fontsize = 20)
fig.tight_layout()
plt.xticks(size = 14)
plt.yticks(size = 12)
plt.yticks(np.arange(0, 0.95, 0.05))
plt.show()

