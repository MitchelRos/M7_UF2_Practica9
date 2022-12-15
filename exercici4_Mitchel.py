import numpy as np


def CreaMariu():
    return np.random.randint(0, 80, [3, 4], int)


def ModificaMatriu():
    a = CreaMariu()
    b = a[:, 3]
    print(a)
    print(" - ")
    np.delete(a, 3, 1)
    print(a)
    return



print(ModificaMatriu())
