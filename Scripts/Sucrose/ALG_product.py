import matplotlib.pyplot as plt
import numpy as np


labels = ['5 g/l', '10 g/l', '15 g/l', '20 g/l', '25 g/l', '30 g/l', '35 g/l', '40 g/l', '45 g/l', '50 g/l']
low_aeration = [0.296296296, 0.246212121, 0.221910112, 0.212184874, 0.140776699, 0.105263158, 0.103896104, 0.083569405, 0.069105691, 0.071637427]
medium_aeration = [0.972886762, 0.541958042, 0.464480874, 0.508888889, 0.468085106, 0.277945619, 0.254120879, 0.228787879, 0.322742475, 0.324483776]
high_aeration = [0, 0, 0, 0.22, 0.260714286, 0.305172414, 0.325179856, 0.175886525, 0.144055944, 0]



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

plt.show()

#plt.savefig('ALG_caps.png', format='png', dpi=300)