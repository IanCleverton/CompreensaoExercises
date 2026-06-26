def pares_matriz(matriz):
    return [x for linha in matriz for x in linha if x % 2 == 0]

print(pares_matriz([[6, 22, 35], [3, 53, 66], [5, 84, 97]]))