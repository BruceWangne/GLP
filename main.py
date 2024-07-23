import numpy as np
import matplotlib.pyplot as plt

def gamma(z):
    rtn = np.gamma(z)
    return rtn

line = []
for i in range(100):
    line.append(gamma(i/100))

plt.plot(line)
plt.show()
