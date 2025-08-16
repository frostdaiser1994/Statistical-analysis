import matplotlib.pyplot as plt
import numpy as np
Capsular_1 = [1.14, 1.32, 0.92, 0.92, 0.75, 0.96]
Capsular_2 = [0.5, 0.43, 0.38, 0.4, 0.29, 0.25]
Capsular_3 = [1.1, 1.46, 1.77, 2.26, 1.24, 1.03]
labels = ["V4", "V5", "V6", "V7", "V8", "V9"] 
x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars
fig, ax = plt.subplots()
rects1 = ax.bar(x - width, Capsular_1, width, color = "darksalmon", label='Capsular_1')
rects2 = ax.bar(x, Capsular_2, width, color = "powderblue", label='Capsular_2')
rects3 = ax.bar(x + width, Capsular_3, width, label='Capsular_3', color = "lightslategrey")
ax.set_ylabel('g/l', fontsize = 12)
ax.set_title('Biosynthesis of Capsular Alginate', fontsize = 20)
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend(loc = 2, fontsize = 20)
fig.tight_layout()
plt.xticks(size = 14)
plt.yticks(size = 12)
plt.yticks(np.arange(0, 2.5, 0.1))
plt.show()
