import matplotlib.pyplot as plt
x1=[50,40,70,80,20]
y1=[x for x in range(1,6)]
x2=[80,20,20,50,60]
ax=plt.subplot()
ax.bar(x1,y1,color='g',width=3)
ax.bar(x2,y1,color='b',width=3)
plt.title('Information')
plt.xlabel('Days')
plt.ylabel('Distance')
plt.show()

import numpy as np
import matplotlib.pyplot as plt

Car1 = [50,40,70,80,20]
Car2 = [80,20,20,50,60]

X = np.arange(len(Car1))

plt.bar(X + 0.00, Car1, color = 'b', width = 0.25)
plt.bar(X + 0.25, Car2, color = 'g', width = 0.25)

plt.show()
