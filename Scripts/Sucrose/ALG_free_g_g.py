import matplotlib.pyplot as plt
import numpy as np


labels = ['5 g/l', '10 g/l', '15 g/l', '20 g/l', '25 g/l', '30 g/l', '35 g/l', '40 g/l', '45 g/l', '50 g/l']
low_aeration = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
medium_aeration = [0.175438596, 0.185314685, 0.144808743, 0.095555556, 0.053191489, 0.019637462, 0.005494505, 0, 0, 0]
high_aeration = [0, 0, 0, 0.024, 0.073214286, 0.117241379, 0.094964029, 0.114893617, 0.148251748, 0.15211267605]


x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width, low_aeration, width, label='низкая аэрация')
rects2 = ax.bar(x + 0, medium_aeration, width, label='средняя аэрация')
rects3 = ax.bar(x + 2*width/1.98, high_aeration, width, label = 'высокая аэрация')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('г/г')
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

#plt.savefig('ALG_free_g_g.png', format='png', dpi=300)