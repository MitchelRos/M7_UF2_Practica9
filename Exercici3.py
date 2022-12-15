import numpy as np

def random():
    m = np.random.randint(0,100, size=100)
    print(m)
random()

def valorMaxim():
    n = np.array([
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
        ])
    print('Max',np.max(n))
valorMaxim()

def valorMinim():
    b = np.array([
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
        ])
    print('Min',np.min(b))
valorMinim()
