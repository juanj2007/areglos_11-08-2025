import numpy as np
vector = np.array([1, 2, 3])
print(vector)
print("version:", np.__version__)
print("tipo de dato:", type(vector))# tipo de dato
print("dimension;", vector.ndim) # dimension del vector
print("forma ", vector.shape) # forma del vector
# crear vector de ceros 
vector_ceros = np.zeros((5))
print("vector de ceros:", vector_ceros)

# crear vector para llenar con unos
vector_unos = np.ones((5))
print("vector de unos:", vector_unos)
# vector con un rango de numerps
vector_rango = np.arange(10)
print("vector con rango de numeros:", vector_rango)