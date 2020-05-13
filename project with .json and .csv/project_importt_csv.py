from matplotlib import pyplot as plt
from project_csv import Weather

values = Weather()
yvalues = [10, 20, 30, 40, 50, 60, 70, 80]

plt.scatter(values,yvalues,  s = 15, c = 'Red', edgecolors= None)
plt.xlabel(" var 1", fontsize = 15)
plt.ylabel("var 2", fontsize = 15)
plt.tick_params(axis = 'both')

plt.show()






