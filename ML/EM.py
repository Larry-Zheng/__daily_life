import numpy as np 

def gauss(x,u,sig):
    return np.exp(-1*(x-u)**2/(2*sig**2))/np.sqrt(2*np.pi*sig**2)


data = [np.random.normal(loc=3,scale=1,size=100),np.random.normal(loc=100,scale=1,size=100)]
data = np.array(data).flatten()
u1,s1 = 4.9,0.1
u2,s2 = 5.1,0.1

cls1 = []
cls2 = []

for _ in range(5):
    for d in data:
        score1 = gauss(d,u1,s1)
        score2 = gauss(d,u2,s2)

        if score1 > score2:
            cls1.append(d)
        else:
            cls2.append(d)

    u1,u2 = np.mean(cls1),np.mean(cls2)
    s1,s2 = np.std(cls1,ddof=1),np.std(cls2,ddof=1)
    print(u1,s1)
    print(u2,s2)
    print('*'*20)
    cls1.clear()
    cls2.clear()



    






