import math
import matplotlib.pyplot as plt
x1=[x for x in range(11)]
y1=[math.e-(x/10)*math.sin(math.pi*x) for x in range(11)]
plt.plot(x1,y1,color='red',label='f(x)')
x2=[x for x in range(11)]
y2=[math.e*x-(x/3) for x in range(11)]
plt.plot(x2,y2,color='green',label='g(x)')
plt.xlabel('Values of x')
plt.ylabel('Value of function')
plt.legend()
scale_x=1
scale_y=2
plt.show()
