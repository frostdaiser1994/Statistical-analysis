import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

Dinamics = pd.DataFrame({'Sucrose, g/l': [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
                   'V1': [0.009, 0.019, 0.036, 0.078, 0.27, 0.55, 0.54, 0.48, 0.49, 0.53],
                   'V2': [0.005, 0.018, 0.029, 0.11, 0.21, 0.63, 0.69, 0.87, 0.91, 0.99],
                   'V3': [None, None, 0, 0, 0.09, 0.21, 0.64, 0.59, 0.37, 0.29]})

Dinamics.to_csv('filename.csv')

Dinamics = pd.read_csv('filename.csv', sep=',')

new_sample_Dinamics = Dinamics['V1']
new_sample_Dinamics2 =Dinamics['V2']
new_sample_Dinamics3 =Dinamics['V3']


plt.xticks(np.arange(0, 65, step=5))
plt.yticks(np.arange(0, 4, step=0.2))

plt.plot(Dinamics['Sucrose, g/l'], new_sample_Dinamics, 'r-o', color = 'darkgrey', label = 'низкая аэрация')
plt.plot(Dinamics['Sucrose, g/l'], new_sample_Dinamics2, 'r-v', color = 'tomato', label = 'средняя аэрация')
plt.plot(Dinamics['Sucrose, g/l'], new_sample_Dinamics3, 'r-s', color = 'goldenrod', label = 'высокая аэрация')


plt.xlabel('Sucrose, g/l', fontsize = 10)
plt.ylabel('g/l', fontsize = 10)
plt.legend(fontsize = 8)
#plt.title('The growth dynamics of bacteria Azotobacter vinelandii 12 under various cultivation conditions')
plt.show()
#plt.savefig('PHB.png', format='png', dpi=300)