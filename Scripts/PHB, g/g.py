import matplotlib.pyplot as plt
import numpy as np


labels = ['5 g/l', '10 g/l', '15 g/l', '20 g/l', '25 g/l', '30 g/l', '35 g/l', '40 g/l', '45 g/l', '50 g/l']
low_aeration = [0.0111, 0.01439, 0.02, 0.032, 0.087, 0.1523, 0.14, 0.1359, 0.1327, 0.155]
medium_aeration = [0.008, 0.0125, 0.0158, 0.0488, 0.0744, 0.19, 0.189, 0.263, 0.303, 0.292]
high_aeration = [0, 0, 0, 0, 0.016, 0.036, 0.092, 0.083, 0.052, 0.041]

x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width, low_aeration, width, label='низкая аэрация')
rects2 = ax.bar(x + 0, medium_aeration, width, label='средняя аэрация')
rects3 = ax.bar(x + 2*width/1.98, high_aeration, width, label = 'высокая аэрация')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('g/g')
#ax.set_title('Produ')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


#autolabel(rects1)
#autolabel(rects2)
#autolabel(rects3)

fig.tight_layout()

#plt.show()

plt.savefig('PHB1.png', format='png', dpi=300)