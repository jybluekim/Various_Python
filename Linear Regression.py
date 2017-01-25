import numpy as np
import matplotlib.pyplot as plt
import random

X = []
Y = []

for i in range (10):
    X.append(random.randint(1,10))
    Y.append(random.randint(1,10))


X = np.array(X)
Y = np.array(Y)



plt.scatter(X,Y)
plt.show()
