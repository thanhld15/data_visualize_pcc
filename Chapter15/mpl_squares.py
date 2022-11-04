import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x_value**2 for x_value in x_values]

plt.scatter(x_values, y_values,c = y_values, cmap = plt.cm.Blues ,edgecolors='none' ,s=40)

plt.axis([0,1100,0,1100000])
plt.savefig('../Image/scatter.png', bbox_inches = 'tight')