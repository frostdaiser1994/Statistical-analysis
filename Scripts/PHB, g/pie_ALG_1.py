import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(2, 5)

labels= ['PHB','Free Alginate','Capsular Alginate']

labels2= ['PHB', 'Capsular Alginate']

values = [0.007974482/1.15629984*100, 0.175438596/1.15629984*100, 0.972886762/1.15629984*100]
values2 = [0.012587413/0.73986014*100, 0.185314685/0.73986014*100, 0.541958042/0.73986014*100]
values3 = [0.015846995/0.6251366119999999*100, 0.144808743/0.6251366119999999*100, 0.464480874/0.6251366119999999*100]
values4 = [0.048888889/0.6533333339999999*100, 0.095555556/0.6533333339999999*100, 0.508888889/0.6533333339999999*100]
values5 = [0.074468085/0.5957446799999999*100, 0.053191489/0.5957446799999999*100, 0.468085106/0.5957446799999999*100]
values6 = [0.190332326/0.48791540699999997*100, 0.019637462/0.48791540699999997*100, 0.277945619/0.48791540699999997*100]
values7 = [0.18956044/0.449175824*100, 0.005494505/0.449175824*100, 0.254120879/0.449175824*100]
values8 = [0.263636364/0.492424243*100, 0, 0.228787879/0.492424243*100]
values9 = [0.3043/0.627042475*100, 0, 0.322742475/0.627042475*100]
values10 = [0.292035398/0.616519174*100, 0, 0.324483776/0.616519174*100]

explodes = [0,0,0]

pie = axs[0,0].pie(values, shadow=True, startangle=120, colors=['gray', 'cornflowerblue', 'green'],
                   autopct='%1.0f%%', textprops={'fontsize': 8})

#axs[0,0].legend(values, labels, title = 'Biopolymers', loc = 'center right', bbox_to_anchor=(1, 0, 0.5, 1))

#values, labels = axs[0,0].get_legend_handles_labels()
#axs[0,0].legend(values, labels, title = 'Biopolymers', loc = 'right', bbox_to_anchor=(1, 0, 0.5, 1))

plt.legend(pie[0],labels, fontsize = 'medium' ,bbox_to_anchor=(1,0), loc="lower right",
                          bbox_transform=plt.gcf().transFigure)

plt.text(-12.5, 7, '5 г/л', size = 'medium')

axs[0,1].pie(values2, shadow=True, startangle=120, colors=['gray', 'cornflowerblue', 'green'],
                   autopct='%1.0f%%', textprops={'fontsize': 8})

plt.text(-9.55, 7, '10 г/л', size = 'medium')

axs[0,2].pie(values3, shadow=True, startangle=120, colors=['gray', 'cornflowerblue', 'green'],
                   autopct='%1.0f%%', textprops={'fontsize': 8})

plt.text(-6.7, 7, '15 г/л', size = 'medium')

axs[0,3].pie(values4, shadow=True, startangle=120, colors=['gray', 'cornflowerblue', 'green'],
                   autopct='%1.0f%%', textprops={'fontsize': 8})

plt.text(-3.6, 7, '20 г/л', size = 'medium')

axs[0,4].pie(values5, shadow=True, startangle=120, colors=['gray', 'cornflowerblue', 'green'],
                   autopct='%1.0f%%', textprops={'fontsize': 8})

plt.text(-0.7, 7, '25 г/л', size = 'medium')

axs[1,0].pie(values6, shadow=True, startangle=120, colors=['gray', 'cornflowerblue', 'green'],
                   autopct='%1.0f%%', textprops={'fontsize': 8})
plt.text(-12.5, 1.1, '30 г/л', size = 'medium')
axs[1,1].pie(values7, shadow=True, startangle=120, colors=['gray', 'cornflowerblue', 'green'],
                   autopct='%1.0f%%', textprops={'fontsize': 8})
plt.text(-9.55, 1.1, '35 г/л', size = 'medium')
axs[1,2].pie(values8, shadow=True, startangle=120, colors=['gray', 'cornflowerblue', 'green'],
                   autopct=lambda p: '{:.0f}%'.format(round(p)) if p > 0 else '', textprops={'fontsize': 8})
plt.text(-6.7, 1.1, '40 г/л', size = 'medium')
axs[1,3].pie(values9, shadow=True, startangle=120, colors=['gray', 'cornflowerblue', 'green'],
                   autopct=lambda p: '{:.0f}%'.format(round(p)) if p > 0 else '', textprops={'fontsize': 8})
plt.text(-3.6, 1.1, '45 г/л', size = 'medium')
axs[1,4].pie(values10, shadow=True, startangle=120, colors=['gray', 'cornflowerblue', 'green'],
                   autopct=lambda p: '{:.0f}%'.format(round(p)) if p > 0 else '', textprops={'fontsize': 8})
plt.text(-0.7, 1.1, '50 г/л', size = 'medium')


#plt.text(-7, 8.1, 'Biosythesis of polymers by Azotobacter vinelandii', color = 'black', size = 'x-large')

#plt.show()
plt.savefig('pie_ALG_2.png', format='png', dpi=300)