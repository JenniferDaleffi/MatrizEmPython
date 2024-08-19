# Projeto: Manipulação de Matrizes

Este projeto em Python consiste em três funções principais para manipular matrizes. Abaixo, descrevo cada função e seu propósito.

## Funções

### 1. `criar_matriz(n_linhas, n_colunas)`

Cria uma matriz de dimensões `n_linhas` x `n_colunas`. O usuário é solicitado a fornecer um número para cada célula da matriz. A função retorna a matriz criada.

#### Parâmetros:
- `n_linhas`: Número de linhas da matriz.
- `n_colunas`: Número de colunas da matriz.

### 2. `imprimir_matriz(matriz)`

Imprime cada elemento da matriz no formato `matriz[i][j]: valor`, onde `i` e `j` são os índices da linha e coluna, respectivamente.

#### Parâmetros:
- `matriz`: A matriz a ser impressa.

### 3. `somar_numeros_matriz(matriz)`

Calcula e retorna a soma de todos os elementos presentes na matriz.

#### Parâmetros:
- `matriz`: A matriz cujos elementos serão somados.

## Como Usar

1. Execute o script.
2. A função `criar_matriz` será chamada, e você deverá fornecer os números para preencher a matriz.
3. A matriz será impressa usando a função `imprimir_matriz`.
4. A soma dos elementos da matriz será exibida.

```python
matriz = criar_matriz(3, 3)
print(matriz)  # Imprime a matriz em formato de lista
imprimir_matriz(matriz)  # Imprime elemento por elemento
print(f'Soma: {somar_numeros_matriz(matriz)}')  # Imprime a soma dos elementos da matriz
