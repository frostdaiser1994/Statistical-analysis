import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['5 g/l', '10 g/l', '15 g/l', '20 g/l', '25 g/l', '30 g/l', '35 g/l', '40 g/l', '45 g/l', '50 g/l']
low_aeration = [0.81, 1.32, 1.78, 2.38, 3.09, 3.61, 3.85, 3.53, 3.69, 3.42]
medium_aeration = [0.627, 1.43, 1.83, 2.25, 2.82, 3.31, 3.64, 3.3, 2.99, 3.39]
high_aeration = [0, 0, 1.88, 5, 5.6, 5.8, 6.95, 7.05, 7.15, 7.10]

x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width, low_aeration, width, label='low_aeration')
rects2 = ax.bar(x + 0, medium_aeration, width, label='medium_aeration')
rects3 = ax.bar(x + 2*width/1.98, high_aeration, width, label = 'high_aeration')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('g/l')
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

plt.savefig('biomass.png', format='png', dpi=300)