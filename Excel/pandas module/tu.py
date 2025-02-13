import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
x = np.linspace(0,20)
y = np.sin(x)
z = np.cos(x)
font = font_manager.FontProperties(fname='E:\picuter.jpg')
plt.xlabel('x',fontproperties = font)
plt.xlabel('y',fontproperties = font)
_x = range(0,20,2)
_xticks = ['%s点'%i for i in _x]
plt.xticks(range(0,20,2),_xticks,fontproperties = font,rotation =45)
_y = range(0,20,2)
_yticks = ['%.2f点'%i for i in _x]
plt.xticks(range(0,20,2),_yticks,fontproperties = font,rotation =45)
plt.plot(x,y)
plt.plot(x,z)