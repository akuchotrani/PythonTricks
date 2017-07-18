# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 17:03:03 2017

@author: aakash.chotrani
"""

import matplotlib.pyplot as plt

x = [5,6,7,8]
y = [7,3,4,1]

x2 = [5,6,7,8]
y2 = [10,14,12,5]

plt.plot(x,y, label = "first line")
plt.plot(x2,y2, label = "second line")
plt.xlabel("x label")
plt.ylabel("y label")

plt.title("Interesting Graph \ncheck it out")
plt.legend()
plt.show()
