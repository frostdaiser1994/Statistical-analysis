import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

Dinamics = pd.DataFrame({'Sucrose, g/l': [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
                   'V1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   'V2': [0.11, 0.265, 0.265, 0.215, 0.15, 0.065, 0.02, 0, 0, 0],
                   'V3': [None, None, 0, 0.12, 0.41, 0.68, 0.66, 0.81, 1.06, 1.08]})

Dinamics.to_csv('filename.csv')

Dinamics = pd.read_csv('filename.csv', sep=',')

new_sample_Dinamics = Dinamics['V1']
new_sample_Dinamics2 =Dinamics['V2']
new_sample_Dinamics3 =Dinamics['V3']


plt.xticks(np.arange(0, 65, step=5))
plt.yticks(np.arange(0, 1.8, step=0.1))

plt.plot(Dinamics['Sucrose, g/l'], new_sample_Dinamics, 'r-o', color = 'darkgrey', label = 'Свободный АЛГ (низкая аэрация)')
plt.plot(Dinamics['Sucrose, g/l'], new_sample_Dinamics2, 'r-v', color = 'tomato', label = 'Свободный АЛГ (средняя аэрация)')
plt.plot(Dinamics['Sucrose, g/l'], new_sample_Dinamics3, 'r-s', color = 'goldenrod', label = 'Свободный АЛГ (высокая аэрация)')


plt.xlabel('Sucrose, g/l', fontsize = 10)
plt.ylabel('g/l', fontsize = 10)
plt.legend(fontsize = 8)
#plt.title('The growth dynamics of bacteria Azotobacter vinelandii 12 under various cultivation conditions')
plt.show()
#plt.savefig('free.png', format='png', dpi=300)