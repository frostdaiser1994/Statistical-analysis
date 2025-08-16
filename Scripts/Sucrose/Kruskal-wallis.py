from scipy import stats
import pandas as pd

Aeration = pd.DataFrame({ 'low aeration': [0.78, 0.79, 0.85, 1.17, 1.54, 1.26, 1.67, 1.81, 1.85,
                                           2.27, 2.32, 2.54, 2.98, 3.11, 3.19, 3.88, 3.52, 3.42,
                                           4.03, 3.41, 4.11, 3.64, 3.39, 3.56, 3.80, 3.63, 3.64,
                                           3.44, 3.30, 3.52],
                          'medium aeration': [0.57, 0.62, 0.69, 1.43, 1.49, 1.37, 1.58, 1.89, 2.01,
                                              2.16, 2.31, 2.28, 3.09, 2.86, 2.51, 3.45, 3.07, 3.41,
                                              3.36, 3.61, 3.95, 3.20, 3.49, 3.20, 2.96, 2.94, 3.07,
                                              3.45, 3.36, 3.36],
                          'high aeration': [0, 0, 0, 0, 0, 0, 1.63, 1.97, 2.03, 4.87, 5.10, 5.03,
                                            5.82, 5.81, 5.17, 6.18, 5.35, 5.87, 6.70, 7.11, 7.05,
                                            6.79, 7.24, 7.12, 7.29, 6.94, 7.22, 7.39, 6.88, 7.04]})

Aeration.to_csv('~/Documents/Scripts/Sucrose/Tables/Aeration.csv')

#print(stats.kruskal(low_aeration1, medium_aeration1, high_aeration1))

a = stats.kruskal([Aeration.at [0, 'low aeration'], Aeration.at [1, 'low aeration'], Aeration.at [2, 'low aeration']],
                    [Aeration.at [0, 'medium aeration'], Aeration.at [1, 'medium aeration'], Aeration.at [2, 'medium aeration']],
                    [Aeration.at [0, 'high aeration'], Aeration.at [1, 'high aeration'], Aeration.at [2, 'high aeration']])
b = stats.kruskal([Aeration.at [3, 'low aeration'], Aeration.at [4, 'low aeration'], Aeration.at [5, 'low aeration']],
                    [Aeration.at [3, 'medium aeration'], Aeration.at [4, 'medium aeration'], Aeration.at [5, 'medium aeration']],
                    [Aeration.at [3, 'high aeration'], Aeration.at [4, 'high aeration'], Aeration.at [5, 'high aeration']])
c = stats.kruskal([Aeration.at [6, 'low aeration'], Aeration.at [7, 'low aeration'], Aeration.at [8, 'low aeration']],
                    [Aeration.at [6, 'medium aeration'], Aeration.at [7, 'medium aeration'], Aeration.at [8, 'medium aeration']],
                    [Aeration.at [6, 'high aeration'], Aeration.at [7, 'high aeration'], Aeration.at [8, 'high aeration']])
d = stats.kruskal([Aeration.at [9, 'low aeration'], Aeration.at [10, 'low aeration'], Aeration.at [11, 'low aeration']],
                    [Aeration.at [9, 'medium aeration'], Aeration.at [10, 'medium aeration'], Aeration.at [11, 'medium aeration']],
                    [Aeration.at [9, 'high aeration'], Aeration.at [10, 'high aeration'], Aeration.at [11, 'high aeration']])
e = stats.kruskal([Aeration.at [12, 'low aeration'], Aeration.at [13, 'low aeration'], Aeration.at [14, 'low aeration']],
                    [Aeration.at [12, 'medium aeration'], Aeration.at [13, 'medium aeration'], Aeration.at [14, 'medium aeration']],
                    [Aeration.at [12, 'high aeration'], Aeration.at [13, 'high aeration'], Aeration.at [14, 'high aeration']])
f = stats.kruskal([Aeration.at [15, 'low aeration'], Aeration.at [16, 'low aeration'], Aeration.at [17, 'low aeration']],
                    [Aeration.at [15, 'medium aeration'], Aeration.at [16, 'medium aeration'], Aeration.at [17, 'medium aeration']],
                    [Aeration.at [15, 'high aeration'], Aeration.at [16, 'high aeration'], Aeration.at [17, 'high aeration']])
g = stats.kruskal([Aeration.at [18, 'low aeration'], Aeration.at [19, 'low aeration'], Aeration.at [20, 'low aeration']],
                    [Aeration.at [18, 'medium aeration'], Aeration.at [19, 'medium aeration'], Aeration.at [20, 'medium aeration']],
                    [Aeration.at [18, 'high aeration'], Aeration.at [19, 'high aeration'], Aeration.at [20, 'high aeration']])
h = stats.kruskal([Aeration.at [21, 'low aeration'], Aeration.at [22, 'low aeration'], Aeration.at [23, 'low aeration']],
                    [Aeration.at [21, 'medium aeration'], Aeration.at [22, 'medium aeration'], Aeration.at [23, 'medium aeration']],
                    [Aeration.at [21, 'high aeration'], Aeration.at [22, 'high aeration'], Aeration.at [23, 'high aeration']])
i = stats.kruskal([Aeration.at [24, 'low aeration'], Aeration.at [25, 'low aeration'], Aeration.at [26, 'low aeration']],
                    [Aeration.at [24, 'medium aeration'], Aeration.at [25, 'medium aeration'], Aeration.at [26, 'medium aeration']],
                    [Aeration.at [24, 'high aeration'], Aeration.at [25, 'high aeration'], Aeration.at [26, 'high aeration']])
k = stats.kruskal([Aeration.at [27, 'low aeration'], Aeration.at [28, 'low aeration'], Aeration.at [29, 'low aeration']],
                    [Aeration.at [27, 'medium aeration'], Aeration.at [28, 'medium aeration'], Aeration.at [29, 'medium aeration']],
                    [Aeration.at [27, 'high aeration'], Aeration.at [28, 'high aeration'], Aeration.at [29, 'high aeration']])

Kruskal_aeration = (a, b, c, d, e, f, g, h, i, k)

#print(Kruskal_aeration)

statistic = [7.45, 5.79, 0.80, 5.96, 6.49, 6.49, 5.96, 6.54, 7.20, 5.47]
pvalue = [0.024, 0.055, 0.670, 0.050, 0.039, 0.039, 0.050, 0.038, 0.027, 0.065]

Kruskal = pd.DataFrame({ 'levels':['5 г/л', '10 г/л', '15 г/л', '20 г/л', '25 г/л', '30 г/л', '35 г/л', '40 г/л', '45 г/л', '50 г/л'],
                         'statistic': [7.45, 5.79, 0.80, 5.96, 6.49, 6.49, 5.96, 6.54, 7.20, 5.47],
                         'pvalue': [0.024, 0.055, 0.670, 0.050, 0.039, 0.039, 0.050, 0.038, 0.027, 0.065]

})

Kruskal.to_csv('~/Documents/Scripts/Sucrose/Tables/Kruskal-Wallis.csv')

#print(Aeration.at [0, 'low aeration'])


print(stats.kruskal([Aeration.at [6, 'low aeration'], Aeration.at [7, 'low aeration'], Aeration.at [8, 'low aeration']],
[Aeration.at [9, 'medium aeration'], Aeration.at [10, 'medium aeration'], Aeration.at [11, 'medium aeration']]))


print(stats.kruskal([Aeration.at [9, 'low aeration'], Aeration.at [10, 'low aeration'], Aeration.at [11, 'low aeration'],
               Aeration.at [9, 'medium aeration'], Aeration.at [10, 'medium aeration'], Aeration.at [11, 'medium aeration'],
               Aeration.at [9, 'high aeration'], Aeration.at [10, 'high aeration'], Aeration.at [11, 'high aeration']],
              [Aeration.at [15, 'low aeration'], Aeration.at [16, 'low aeration'], Aeration.at [17, 'low aeration'],
               Aeration.at [15, 'medium aeration'], Aeration.at [16, 'medium aeration'], Aeration.at [17, 'medium aeration'],
               Aeration.at [15, 'high aeration'], Aeration.at [16, 'high aeration'], Aeration.at [17, 'high aeration']]))

print(stats.kruskal([Aeration.at [18, 'low aeration'], Aeration.at [19, 'low aeration'], Aeration.at [20, 'low aeration'],
               Aeration.at [18, 'medium aeration'], Aeration.at [19, 'medium aeration'], Aeration.at [20, 'medium aeration'],
               Aeration.at [18, 'high aeration'], Aeration.at [19, 'high aeration'], Aeration.at [20, 'high aeration']],
              [Aeration.at [15, 'low aeration'], Aeration.at [16, 'low aeration'], Aeration.at [17, 'low aeration'],
               Aeration.at [15, 'medium aeration'], Aeration.at [16, 'medium aeration'], Aeration.at [17, 'medium aeration'],
               Aeration.at [15, 'high aeration'], Aeration.at [16, 'high aeration'], Aeration.at [17, 'high aeration']]))

