import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(2, 4)

labels= ['PHB','Free Alginate','Capsular Alginate']

labels2= ['PHB', 'Capsular Alginate']

values7 = [27.2, 0, 1000]
values = [0, 0.024/0.46*100, 0.22/0.46*100]
values2 = [0.016071429/0.350000001*100, 0.073214286/0.350000001*100, 0.260714286/0.350000001*100]
values3 = [0.036206897/0.45862069*100, 0.117241379/0.45862069*100, 0.305172414/0.45862069*100]
values4 = [0.092086331/0.512230216*100, 0.094964029/0.512230216*100, 0.325179856/0.512230216*100]
values5 = [0.083687943/0.37446808499999995*100, 0.114893617/0.37446808499999995*100, 0.175886525/0.37446808499999995*100]
values6 = [0.051748252/0.34405594399999995*100, 0.148251748/0.34405594399999995*100, 0.144055944/0.34405594399999995*100]
values8 = [0.31, 1.08, 0.92]

explodes = [0,0,0]

pie = axs[0,0].pie(values7, shadow=True, startangle=120, colors=['gray', 'cornflowerblue', 'green'],
                   autopct=lambda p: '{:.0f}%'.format(round(p)) if p > 0 else '', textprops={'fontsize': 8})
axs[0,1].pie(values, shadow=True, startangle=120, colors=['gray', 'cornflowerblue', 'green'],
                   autopct=lambda p: '{:.0f}%'.format(round(p)) if p > 0 else '', textprops={'fontsize': 8})
axs[0,2].pie(values2, shadow=True, startangle=120, colors=['gray', 'cornflowerblue', 'green'],
                   autopct='%1.0f%%', textprops={'fontsize': 8})
axs[0,2].pie(values2, shadow=True, startangle=120, colors=['gray', 'cornflowerblue', 'green'],
                   autopct='%1.0f%%', textprops={'fontsize': 8})
axs[0,3].pie(values3, shadow=True, startangle=120, colors=['gray', 'cornflowerblue', 'green'],
                   autopct='%1.0f%%', textprops={'fontsize': 8})
axs[1,0].pie(values4, shadow=True, startangle=120, colors=['gray', 'cornflowerblue', 'green'],
                   autopct='%1.0f%%', textprops={'fontsize': 8})
axs[1,1].pie(values5, shadow=True, startangle=120, colors=['gray', 'cornflowerblue', 'green'],
                   autopct='%1.0f%%', textprops={'fontsize': 8})
axs[1,2].pie(values6, shadow=True, startangle=120, colors=['gray', 'cornflowerblue', 'green'],
                   autopct='%1.0f%%', textprops={'fontsize': 8})
axs[1,3].pie(values8, shadow=True, startangle=120, colors=['gray', 'cornflowerblue', 'green'],
                   autopct='%1.0f%%', textprops={'fontsize': 8})
plt.legend(pie[0],labels, fontsize = 'medium' ,bbox_to_anchor=(1,0), loc="lower right", bbox_transform=plt.gcf().transFigure)

plt.text(-9.6, 5.8, '15 г/л', color = 'black', size = 'x-large')
plt.text(-6.6, 5.8, '20 г/л', color = 'black', size = 'x-large')
plt.text(-3.6, 5.8, '25 г/л', color = 'black', size = 'x-large')
plt.text(-0.7, 5.8, '30 г/л', color = 'black', size = 'x-large')
plt.text(-9.6, 1.1, '35 г/л', color = 'black', size = 'x-large')
plt.text(-6.6, 1.1, '40 г/л', color = 'black', size = 'x-large')
plt.text(-3.6, 1.1, '45 г/л', color = 'black', size = 'x-large')
plt.text(-0.7, 1.1, '50 г/л', color = 'black', size = 'x-large')

#plt.show()

#plt.text(-7, 8.1, 'Biosythesis of polymers by Azotobacter vinelandii', color = 'black', size = 'x-large')
#plt.savefig('pie_ALG_3.png', format='png', dpi=300)
#axs[0,0].legend(values, labels, title = 'Biopolymers', loc = 'center right', bbox_to_anchor=(1, 0, 0.5, 1))
#values, labels = axs[0,0].get_legend_handles_labels()
#axs[0,0].legend(values, labels, title = 'Biopolymers', loc = 'right', bbox_to_anchor=(1, 0, 0.5, 1))

plt.savefig('pie_ALG_3.png', format='png', dpi=300)