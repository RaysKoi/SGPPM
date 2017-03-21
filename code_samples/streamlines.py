# streamlines.py
# -------------------------------------------------------------------------
# Create streamlines from a vector field.
# ------------------------------------------------------------------------- 
import numpy as np
import matplotlib.pyplot as plt

# generate grid of points
lower = -2; upper = 2; step = 0.2
coords = np.arange(lower, upper+step, step)
X, Y = np.meshgrid(coords, coords)

# define vector field
Vx, Vy = Y, -X

# display streamlines defined by vector field
plt.figure()
plt.streamplot(X, Y, Vx, Vy, linewidth=2)
plt.show()
