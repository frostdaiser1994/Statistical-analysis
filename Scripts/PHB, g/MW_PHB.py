import matplotlib.pyplot as plt
import numpy as np


labels = ['5 g/l', '10 g/l', '15 g/l', '20 g/l', '25 g/l', '30 g/l', '35 g/l', '40 g/l', '45 g/l', '50 g/l']
low_aeration = [0, 718, 782.5, 320, 529.8, 882.6, 862.2, 880, 897, 955]
medium_aeration = [26.7, 890, 757, 1064, 1115, 828, 968, 808, 732, 1081]
high_aeration = [0, 0, 0, 0, 534, 1479, 1104, 933, 1024, 0]


x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width, low_aeration, width, label='низкая аэрация')
rects2 = ax.bar(x + 0, medium_aeration, width, label='средняя аэрация')
rects3 = ax.bar(x + 2*width/1.98, high_aeration, width, label = 'высокая аэрация')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('kDa')
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
plt.savefig('PHB_MW.png', format='png', dpi=300)