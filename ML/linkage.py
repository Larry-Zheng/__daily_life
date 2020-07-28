import numpy as np 

#西瓜书对应聚类章节中层次聚类计算类间距离的过程
def linkage(x1,x2,mode):
    if len(x1)>len(x2):
        x1,x2 = x2,x1 

    if mode=='avg':
        res = 0
        for each_x1 in x1:
            res += np.sqrt(((each_x1-x2)**2).sum(axis=-1)).sum()
        return res/len(x1)/len(x2)
    
    elif mode == 'min':
        res = np.inf
        for each_x1 in x1:
            temp = np.sqrt(((each_x1-x2)**2).sum(axis=-1)).min()
            if res > temp:
                res = temp
        
        return res 

    elif mode == 'max':
        res = -np.inf
        for each_x1 in x1:
            temp = np.sqrt(((each_x1-x2)**2).sum(axis=-1)).max()
            if res < temp:
                res = temp
        
        return res
    
    else:
        raise Exception('哼哼 啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊')



if __name__ == '__main__':
    a = np.arange(100).reshape(-1,2)
    b = np.arange(10).reshape(-1,2)

    print(linkage(a,b,mode='avg'))


