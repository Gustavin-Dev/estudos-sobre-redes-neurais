import numpy as np

entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
saidasEsperadas = np.array([0,0,0,1])
pesos = np.array([0.0,0.0])
taxaAprendizagem = 0.1

def stepFunction(resultadoFuncaoSoma):
    if(resultadoFuncaoSoma >= 1):
        return 1
    return 0

def calcularSaida(entrada):
    soma = entrada.dot(pesos) #funcao soma, faz o produto interno: x1*w1 + x2*w2 + ... xn * wn
    return stepFunction(soma)

def treinarRede():
    erroTotal = 1
    while (erroTotal != 0):
        erroTotal = 0
        for i in range(len(saidasEsperadas)):
            saidaCalculada = calcularSaida(np.asarray(entradas[i]))
            print("Saida esperada para entrada ", np.asarray(entradas[i]) , ": " ,saidasEsperadas[i] , "///  Saida calculada para entrada ", np.asarray(entradas[i]) , ": ", saidaCalculada)
            erro = abs(saidasEsperadas[i] - saidaCalculada)
            erroTotal += erro
            print("Pesos atuais: ", pesos)
            if erro != 0: #atualizar pesos somente quando houver erro, output mais limpo
             print("Valor do erro para entrada: ",np.asarray(entradas[i]), ": " ,erro)
             print("Atualização de pesos conforme estipulado: pesoNovo = pesoAtual + (taxaAprendizagem * entrada * pesoAtual)")
             for j in range(len(pesos)):
                 pesos[j] = pesos[j] + (taxaAprendizagem * entradas[i][j] * erro)
        print("Pesos atalizados! " + str(pesos))
        print("erro total da rede (caso particular erroTotal = vezes que a rede errou): ", erroTotal)
        print("nova tentativa com pesos atualizados!!!")
        print()
             
treinarRede()        