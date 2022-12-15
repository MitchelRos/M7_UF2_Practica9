import numpy as np

ndarray = np.array([
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
])


#Per defecte si no es posa una array
def exerici1(arr=ndarray):
    print(arr)
    # Retorna la dimesio de la array
    print("Dimensio Matriu", arr.ndim)
    # Retorna el tamnany de l'array
    print("Tamany Matriu", arr.shape)
    # Retorna el total d'elements de l'array
    print("Total", arr.size)
    # Retorna el tipus d'elements d'array
    print("Tipus", arr.dtype)
    #Guarda fitxer binary
    print("Guardar fitxer Binari",np.save("exercici1.npy",arr))



exerici1()


