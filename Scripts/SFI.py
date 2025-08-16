import numpy as np
import matplotlib.pyplot as plt

objects = ('Control', 'PHB', 'PHB/M14')
ind = np.arange(len(objects))

SFI = (-15.3461957, -2.838147644, -7.822814027)
width = 0.65       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, SFI, width, color = "red", label = 'SFI', align='center', alpha=0.5)

# Get the axes object
ax = plt.gca()
# remove the existing ticklabels
ax.set_xticklabels([])
# remove the extra tick on the negative bar
ax.set_xticks([idx for (idx, x) in enumerate(SFI) if x > 0])
ax.spines["bottom"].set_position(("data", 0))
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
# placing each of the x-axis labels individually
label_offset = 0.5
for language, (x_position, y_position) in zip(objects, enumerate(SFI)):
    if y_position > 0:
        label_y = -label_offset
    else:
        label_y = y_position - label_offset
    ax.text(x_position, label_y, language, ha="center", va="top")
# Placing the x-axis label, note the transformation into `Axes` co-ordinates
# previously data co-ordinates for the x ticklabels
#ax.text(0.5, -0.05, ha="center", va="top", transform=ax.transAxes)


plt.ylabel('SFI level')
#plt.title('Acetylation level of free bacterial alginates_Dudun')
#plt.xticks(ind, ('Control', 'PHB', 'PHB/M14'))
plt.yticks(np.arange(-25, 10, 5))
#plt.legend()

plt.savefig("SFI.png", format = "png", dpi = 300)

from pathlib import Path

current_dir = Path.cwd()
print(current_dir)