import matplotlib.pyplot as plt 
import numpy as np 
x_values1 = np.linspace(-10,-0.01,num = 100)
x_values2 = np.linspace(0.01,10,num = 100)
x  = np.concatenate((x_values1, x_values2))
#x_values1 =np.arange(-10,-0.1,0.0001)
# x_value2= np.arange(0.1,10,num = 0.0001)
ε = 8.54 * 10**(-12) #F/m 
q = 1.602 * 10**(-19) #C
#z = 1
k = -(pow(q,2))/(4*np.pi*ε)
v_x = k/abs(x)
plt.plot(x,v_x,color='red', label='Coulombic Potential')
plt.ylabel('Coulombic Potential well')
plt.xlabel('x-Distance')
plt.hlines(y=0, xmin=-10, xmax=10, color='blue', linestyle=':', linewidth=2 )
plt.show()
