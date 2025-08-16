import matplotlib.pyplot as plt
import numpy as np
PHB_1 = [757, 1064, 1115, 828, 968, 808, 732]
PHB_2 = [782.5, 320, 529.8, 882.6, 862.2, 880, 897]
PHB_3 = [49, 0, 534, 1479, 1104, 933, 1024]
labels = ["V3", "V4", "V5", "V6", "V7", "V8", "V9"] 
x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars
fig, ax = plt.subplots()
rects1 = ax.bar(x - width, PHB_1, width, color = "darksalmon", label='PHB_1')
rects2 = ax.bar(x, PHB_2, width, color = "powderblue", label='PHB_2')
rects3 = ax.bar(x + width, PHB_3, width, label='PHB_3', color = "lightslategrey")
ax.set_ylabel('kDa', fontsize = 12)
ax.set_title('MW of PHBs', fontsize = 20)
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend(loc = 2, fontsize = 20)
fig.tight_layout()
plt.xticks(size = 14)
plt.yticks(size = 12)
plt.yticks(np.arange(0, 1600, 100))
plt.show()

