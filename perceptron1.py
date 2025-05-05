import numpy as np

entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
saidasEsperadas = np.array([0,0,0,1])
pesos = np.array([0.0,0.0])
taxaAprendizagem = 0.1

def stepFunction(resultadoFuncaoSoma):
    if resultadoFuncaoSoma >= 1:
        return 1
    return 0

def calcularSaida(entrada):
    soma = entrada.dot(pesos)
    return stepFunction(soma)

def treinarRede():
    erroTotal = 1
    while erroTotal != 0:
        erroTotal = 0
        for i in range(len(saidasEsperadas)):
            entradaAtual = np.asarray(entradas[i])
            saidaCalculada = calcularSaida(entradaAtual)
            erro = saidasEsperadas[i] - saidaCalculada
            erroTotal += abs(erro)

            
            print("Pesos atuais:", pesos)

            if erro != 0:
                print("Erro:", erro)
                print("Atualização de pesos conforme: pesoNovo = pesoAtual + (taxaAprendizagem * entrada * erro)")
                for j in range(len(pesos)):
                    pesos[j] += taxaAprendizagem * entradaAtual[j] * erro

        print("Pesos atualizados:", pesos)
        print("Erro total da época:", erroTotal)
        print("Nova tentativa com pesos atualizados!\n")

treinarRede()
