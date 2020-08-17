from sklearn.datasets import make_moons,make_blobs
from matplotlib import pyplot as plt
import numpy as np


if __name__ == '__main__':

    X,y = make_moons(200,noise=0.02,random_state=1)
    status = np.full(y.shape,-1)  #标记所有对象unvisited
    C = 0   #当前新类别
    N = []  
    MinPts = 1
    eta = 0.08
    # plt.scatter(X[:,0],X[:,1],c=y)
    # plt.show()

    #但凡status里有-1 就有没有访问到的
    while (status==-1).any():  
        index = np.where(status==-1)[0][0]  #取第一个未读取点

        status[index] = 0  #标记噪声已读


        #算该点是不是核心点
        adjPts = np.sqrt(((X[index] - X)**2).sum(axis=1))<=eta
        adjPts[index] = False


        #如果不是 continue
        if adjPts.sum()< MinPts:
            continue
           
        #如果是
        C += 1  #生成新类别
        status[index] = C  #该点标记新类别
        affPts = np.where(adjPts)[0]  #关联点
        N.extend(affPts.tolist())  #加进去
        for ni in N:
            if status[ni] != -1:
                continue  #已经读取过就不管
            
            status[ni] = C  #标记该关联点
            #算该关联点是否为核心
            n_adjPts = np.sqrt(((X[ni] - X)**2).sum(axis=1))<=eta
            n_adjPts[ni] = False

            #如果不是跳过
            if n_adjPts.sum() < MinPts:
                continue
            #如果是则把关联点关联点 添加进去
            n_affPts = np.where(n_adjPts)[0]
            N.extend(n_affPts.tolist())
    

    plt.scatter(X[:,0],X[:,1],c=status)
    plt.show()
    













