entradas = [1,7,5]
pesos = [0.8,0.1,0]

def soma(entradas,pesos):
    soma = 0
    for i in range(3):
        soma += entradas[i] * pesos[i]
    return soma

resultadoFuncaoSoma = soma(entradas,pesos) 

def stepFunction(valorFuncaoSoma):
    if valorFuncaoSoma < 0:
        return 0
    return 1

neuronio = stepFunction(resultadoFuncaoSoma)
print("Nosso neuronio tem valor: ", neuronio)
print("resultado da funcao soma: ", resultadoFuncaoSoma)