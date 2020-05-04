import sys
import matplotlib.pyplot as plt

labels = {0:'cat', 1:'dutch', 2:'eng', 3:'fin', 4:'french', 5:'gal', 6:'ger', 7:'ita', 8:'jap', 9:'port'}
x = [0.6, 0.3, 0.1, 0.5, 0.2, 0.3, 0.2, 0.2, 0.9, 0.2]  # proportion of OV
y = [0.4, 0.7, 0.9, 0.5, 0.8, 0.7, 0.8, 0.8, 0.1, 0.8]  # proportion of VO
plt.plot(x, y, 'ro')
plt.title('Relative word order of verb and object')
plt.xlim([0,1]) # Set the x and y axis ranges
plt.ylim([0,1])
plt.xlabel('OV') # Set the x and y axis labels
plt.ylabel('VO')
for i in labels:  # Add labels to each of the points
    plt.text(x[i]-0.03, y[i]-0.03, labels[i], fontsize=9)
#plt.savefig(sys.argv[])
plt.show()
