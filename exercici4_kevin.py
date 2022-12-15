import numpy as np

# asdf
col = 3
row = 4
#Crea una array amb numeros random de dimensions 'col' i 'row'
matrix = np.random.randint(1, 10, size=(row, col))
print("Row :{} Cols:{}".format(row,col))
print(matrix)
# Canvia els cols per el rows
new_matrix = np.transpose(matrix)
print("Canvia els cols per els rows ")
print(new_matrix)
