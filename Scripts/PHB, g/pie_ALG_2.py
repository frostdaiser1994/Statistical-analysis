import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(2, 5)

labels= ['PHB','Free Alginate','Capsular Alginate']

labels2= ['PHB', 'Capsular Alginate']

values = [0.011111111/0.307407407*100, 0.296296296/0.307407407*100]

values2 = [0.014393939/0.26060606000000003*100, 0.246212121/0.26060606000000003*100]

values3 = [0.020224719/0.242134831*100, 0.221910112/0.242134831*100]

values4 = [0.032773109/0.244957983*100, 0.212184874/0.244957983*100]

values5 = [0.087378641/0.22815534*100, 0.140776699/0.22815534*100]

values6 = [0.152354571/0.257617729*100, 0.105263158/0.257617729*100]

values7 = [0.14025974/0.244155844*100, 0.103896104/0.244155844*100]

values8 = [0.135977337/0.21954674200000002*100, 0.083569405/0.21954674200000002*100]

values9 = [0.089430894/0.158536585*100, 0.069105691/0.158536585*100]

values10 = [0.15497076/0.22660818700000002*100, 0.071637427/0.22660818700000002*100]

explodes = [0,0,0]

pie = axs[0,0].pie(values, shadow=True, startangle=120, colors=['gray', 'green'],
                   autopct='%1.0f%%', textprops={'fontsize': 8})

plt.legend(pie[0],labels2, fontsize = 'medium' ,bbox_to_anchor=(1,0), loc="lower right",
                          bbox_transform=plt.gcf().transFigure)

plt.text(-12.5, 7, '5 г/л', color = 'black', size = 'medium')

axs[0,1].pie(values2, shadow=True, startangle=120, colors=['gray', 'green'],
                   autopct='%1.0f%%', textprops={'fontsize': 8})

plt.text(-9.55, 7, '10 г/л', color = 'black', size = 'medium')

axs[0,2].pie(values3, shadow=True, startangle=120, colors=['gray', 'green'],
                   autopct='%1.0f%%', textprops={'fontsize': 8})

plt.text(-6.7, 7, '15 г/л', color = 'black', size = 'medium')

axs[0,3].pie(values4, shadow=True, startangle=120, colors=['gray', 'green'],
                   autopct='%1.0f%%', textprops={'fontsize': 8})

plt.text(-3.6, 7, '20 г/л', color = 'black', size = 'medium')

axs[0,4].pie(values5, shadow=True, startangle=120, colors=['gray', 'green'],
                   autopct='%1.0f%%', textprops={'fontsize': 8})

plt.text(-0.7, 7, '25 г/л', color = 'black', size = 'medium')

axs[1,0].pie(values6, shadow=True, startangle=120, colors=['gray', 'green'],
                   autopct='%1.0f%%', textprops={'fontsize': 8})
plt.text(-12.5, 1.1, '30 г/л', color = 'black', size = 'medium')
axs[1,1].pie(values7, shadow=True, startangle=120, colors=['gray', 'green'],
                   autopct='%1.0f%%', textprops={'fontsize': 8})
plt.text(-9.55, 1.1, '35 г/л', color = 'black', size = 'medium')
axs[1,2].pie(values8, shadow=True, startangle=120, colors=['gray', 'green'],
                   autopct='%1.0f%%', textprops={'fontsize': 8})
plt.text(-6.7, 1.1, '40 г/л', color = 'black', size = 'medium')
axs[1,3].pie(values9, shadow=True, startangle=120, colors=['gray', 'green'],
                   autopct='%1.0f%%', textprops={'fontsize': 8})
plt.text(-3.6, 1.1, '45 г/л', color = 'black', size = 'medium')
axs[1,4].pie(values10, shadow=True, startangle=120, colors=['gray', 'green'],
                   autopct='%1.0f%%', textprops={'fontsize': 8})
plt.text(-0.7, 1.1, '50 г/л', color = 'black', size = 'medium')


#plt.text(-7, 8.1, 'Biosythesis of polymers by Azotobacter vinelandii', color = 'black', size = 'x-large')

plt.show()

#plt.savefig('pie_ALG_1.png', format='png', dpi=300)