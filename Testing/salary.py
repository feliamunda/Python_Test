matriz1 = [[1,2,3],[4,5,6],[7,8,9]]
matriz2 = [[10,11,12],[13,14,15],[16,17,18]]

matriz3 = [[1,2,3],[4,5,6],[7,8,9]]
print(matriz1)
print(matriz2)
for posF,value1 in enumerate(matriz1):
    for posC, value2 in enumerate(value1):
        matriz3[posF][posC] = value2 + matriz2[posF][posC]
print(matriz3)