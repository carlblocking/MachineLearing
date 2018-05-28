import numpy as np

raw_output=np.random.randint(0, 255, (1, 5, 5, 3))
label_batch=np.random.randint(0, 5, (1, 5, 5, 1))

np.save("a.npy", raw_output)
np.save("b.npy", label_batch)
