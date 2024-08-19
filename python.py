def criar_matriz(n_linhas, n_colunas):
    matriz = []
    for i in range(n_linhas):
        linha = []
        for j in range(n_colunas):
            n = int(input('Número: '))
            linha.append(n)
        matriz.append(linha)
    return matriz
 
'''Necesitasse colocar matrz entre parentese para entender o que você quer imprimir.'''
def imprimir_matriz(matriz):
    for i in range(len(matriz)):
        for j in range (len(matriz[i])):
            print(f'matriz[{i}][{j}]: {matriz[{i}][{j}]}')
 
'''Primeiro Exercício'''
#Criar uma função que receba uma matriz e retorne o somatório
# de todos os elementos da matriz
 
def somar_numeros_matriz(matriz):
    soma = 0 #variável acumuladora
    for i in range (len(matriz)):
        for j in range(len(matriz[i])):
            soma += matriz[i][j]
    return soma
 
#Principal
matriz = criar_matriz(3, 3)
print(matriz) # imprime em formato de lista
imprimir_matriz(matriz) # imprime elemento por elemento
print ('Soma: {somar_numeros_matriz(matriz)}')