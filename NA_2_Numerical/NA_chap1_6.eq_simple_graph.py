from scipy import linalg as la
from scipy import optimize
import sympy
sympy.init_printing()
import numpy as np
import matplotlib.pyplot as plt


#### 간단한 그래프 그리기 ####
## pp.242 ##


x = np.linspace(-2, 2, 1000)
f1 = x**2 - x- 1
f2 = x**3 - 3*np.sin(x)
f3 = np.exp(x) - 2
f4 = 1 - x**2 + np.sin(50 / (1 + x**2))

fig, axes = plt.subplots(1, 4, figsize=(12, 3), sharey = True)

for n, f in enumerate([f1, f2, f3, f4]):
    axes[n].plot(x, f, lw=1.5)
    axes[n].axhline(0, ls=':', color='k')
    axes[n].set_ylim(-5,5)
    axes[n].set_xticks([-2, -1, 0, 1, 2])

fig.show()
