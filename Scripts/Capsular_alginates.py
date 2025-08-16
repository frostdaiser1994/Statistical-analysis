import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

Dinamics = pd.DataFrame({'Sucrose, g/l': [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
                   'V1': [0.24, 0.325, 0.395, 0.505, 0.435, 0.38, 0.4, 0.295, 0.255, 0.245],
                   'V2': [0.61, 0.775, 0.85, 1.145, 1.32, 0.92, 0.925, 0.755, 0.965, 1.1],
                   'V3': [None, None, 2.07, 1.1, 1.46, 1.77, 2.26, 1.24, 1.03, 0.92]})

Dinamics.to_csv('filename.csv')

Dinamics = pd.read_csv('filename.csv', sep=',')

new_sample_Dinamics = Dinamics['V1']
new_sample_Dinamics2 =Dinamics['V2']
new_sample_Dinamics3 =Dinamics['V3']


plt.xticks(np.arange(0, 65, step=5))
plt.yticks(np.arange(0, 4, step=0.2))

plt.plot(Dinamics['Sucrose, g/l'], new_sample_Dinamics, 'r-o', color = 'darkgrey', label = 'Капсулярный АЛГ (низкая аэрация)')
plt.plot(Dinamics['Sucrose, g/l'], new_sample_Dinamics2, 'r-v', color = 'tomato', label = 'Капсулярный АЛГ (средняя аэрация)')
plt.plot(Dinamics['Sucrose, g/l'], new_sample_Dinamics3, 'r-s', color = 'goldenrod', label = 'Капсулярный АЛГ (высокая аэрация)')


plt.xlabel('Sucrose, g/l', fontsize = 10)
plt.ylabel('g/l', fontsize = 10)
#plt.legend(fontsize = 8)
#plt.title('The growth dynamics of bacteria Azotobacter vinelandii 12 under various cultivation conditions')
plt.show()
#plt.savefig('caps.png', format='png', dpi=300)