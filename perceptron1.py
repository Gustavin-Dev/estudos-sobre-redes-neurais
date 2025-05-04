import numpy as np


entradas = np.array([1,7,5])
pesos = np.array([0.8,0.1,0])

def soma(entradas,pesos):
    soma = entradas.dot(pesos)
    return soma

resultadoFuncaoSoma = soma(entradas,pesos) 

def stepFunction(valorFuncaoSoma):
    if valorFuncaoSoma < 0:
        return 0
    return 1

neuronio = stepFunction(resultadoFuncaoSoma)
print("Nosso neuronio tem valor: ", neuronio)
print("resultado da funcao soma: ", resultadoFuncaoSoma)