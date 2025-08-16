import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['5 g/l', '10 g/l', '15 g/l', '20 g/l', '25 g/l', '30 g/l', '35 g/l', '40 g/l', '45 g/l', '50 g/l']
low_aeration = [0.81, 1.32, 1.78, 2.38, 3.09, 3.61, 3.85, 3.53, 3.69, 3.42]
low_aeration1 = [0.78, 0.79, 0.85]
low_aeration2 = [1.17, 1.54, 1.26]
low_aeration3 = [1.67, 1.81, 1.85]
low_aeration4 = [2.27, 2.32, 2.54]
low_aeration5 = [2.98, 3.11, 3.19]
low_aeration6 = [3.88, 3.52, 3.42]
low_aeration7 = [4.03, 3.41, 4.11]
low_aeration8 = [3.64, 3.39, 3.56]
low_aeration9 = [3.80, 3.63, 3.64]
low_aeration10 = [3.44, 3.30, 3.52]
dev_low_aeration = [0.035, 0.192, 0.094, 0.144, 0.106, 0.241, 0.381, 0.127, 0.093, 0.113]

medium_aeration = [0.627, 1.43, 1.83, 2.25, 2.82, 3.31, 3.64, 3.3, 2.99, 3.39]
medium_aeration1 = [0.57, 0.62, 0.69]
medium_aeration2 = [1.43, 1.49, 1.37]
medium_aeration3 = [1.58, 1.89, 2.01]
medium_aeration4 = [2.16, 2.31, 2.28]
medium_aeration5 = [3.09, 2.86, 2.51]
medium_aeration6 = [3.45, 3.07, 3.41]
medium_aeration7 = [3.36, 3.61, 3.95]
medium_aeration8 = [3.20, 3.49, 3.20]
medium_aeration9 = [2.96, 2.94, 3.07]
medium_aeration10 = [3.45, 3.36, 3.36]
dev_medium_aeration = [0.055, 0.059, 0.22, 0.078, 0.29, 0.21, 0.29, 0.17, 0.073, 0.048]

high_aeration = [0, 0, 1.88, 5, 5.6, 5.8, 6.95, 7.05, 7.15, 7.10]
high_aeration1 = [0, 0, 0]
high_aeration2 = [0, 0, 0]
high_aeration3 = [1.63, 1.97, 2.03]
high_aeration4 = [4.87, 5.10, 5.03]
high_aeration5 = [5.82, 5.81, 5.17]
high_aeration6 = [6.18, 5.35, 5.87]
high_aeration7 = [6.70, 7.11, 7.05]
high_aeration8 = [6.79, 7.24, 7.12]
high_aeration9 = [7.29, 6.94, 7.22]
high_aeration10 = [7.39, 6.88, 7.04]
dev_high_aeration = [0, 0, 0.22, 0.12, 0.37, 0.42, 0.22, 0.23, 0.18, 0.26]

x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width, low_aeration, width, yerr = dev_low_aeration, label='низкая аэрация', capsize=3)
rects2 = ax.bar(x + 0, medium_aeration, width, yerr = dev_medium_aeration, label='средняя аэрация', capsize=3)
rects3 = ax.bar(x + 2*width/1.98, high_aeration, width, yerr = dev_high_aeration, label = 'высокая аэрация', capsize=3)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('г/л')
#ax.set_title('Produ')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend(loc = 2, fontsize = 12)


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

plt.yticks(np.arange(0, 10, 1))

plt.show()

#plt.savefig('biomass.png', format='png', dpi=300)