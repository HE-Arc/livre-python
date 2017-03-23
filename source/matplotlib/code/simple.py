import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, np.pi * 2, 0.1)  # [0, 0.1, 0.2, ..., pi*2]
y = np.cos(x)
plt.plot(x, y)

plt.show()  # huh, important!
