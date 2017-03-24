# source : PythonProgramming.net
"""Plot 3D."""
import numpy as np

import matplotlib.pyplot as plt
from matplotlib import style
from mpl_toolkits.mplot3d import axes3d

style.use('ggplot')

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

x, y, z = axes3d.get_test_data()

print(axes3d.__file__)
ax1.plot_wireframe(x, y, z, rstride=3, cstride=3)

ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')

plt.show()
