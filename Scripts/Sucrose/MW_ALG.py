import numpy as np
import matplotlib.pyplot as plt

N = 6

#deviation = (28.82,15.62,9.84,33.71,9.53,30.04,2.64,21.16)

acetylation = (391.46, 477.69, 342.91, 372.73, 211.93, 196.09)
ind = np.arange(N)    # the x locations for the groups
width = 0.88       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, acetylation, width, label = 'ММ АЛГ, высокая аэрация')


plt.ylabel('kDa', fontsize = 16)
#plt.title('Acetylation level of capsular bacterial alginates_Dudun')
plt.xticks(ind, ("20 г/л", "25 г/л", "30 г/л", "35 г/л", "40 г/л", "45 г/л"), fontsize = 8)
plt.yticks(np.arange(0, 600, 50))
#plt.legend(fontsize = 14)
#plt.grid(axis = 'y')
#plt.show()
plt.savefig('ALG_MW.png', format='png', dpi=300)