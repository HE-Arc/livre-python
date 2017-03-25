"""Affiche des points."""
import matplotlib.pyplot as plt
import numpy as np

xs = np.arange(0, 2 * np.pi, 0.1)
ys = np.cos(xs)
# r -> red
# o -> dot
plt.plot(xs, ys, "ro")

plt.show()
