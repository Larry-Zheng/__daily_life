from sklearn.datasets import make_moons,make_blobs
from matplotlib import pyplot as plt
import numpy as np


if __name__ == '__main__':

    X,y = make_blobs(100,2,centers=3,random_state=1)
    # plt.scatter(X[:,0],X[:,1],c=y)
    # plt.show()
    print(y)
    V = np.array([X[0],X[1],X[4]])
    V_y = np.array([y[0],y[1],y[4]])
    lr = 0.5
    
    for _ in range(100):
        i = np.random.randint(len(y))
        targetX = X[i].reshape(1,-1)
        targety = y[i]
        update_i = ((targetX-V)**2).sum(axis=1).argmin()

        k = 1 if V_y[update_i] == targety else -1
        V[update_i] += k*lr*(targetX.flatten()-V[update_i])

    
    res_y = []
    for each_x in X:
        res_y.append(((each_x.reshape(1,-1)-V)**2).sum(axis=1).argmin())
    
    plt.scatter(X[:,0],X[:,1],c=res_y)
    plt.show()


