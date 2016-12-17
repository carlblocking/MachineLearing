import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-4, 4, 100)
y=1/(1+np.exp(-x))
plt.plot(y)
plt.show()
