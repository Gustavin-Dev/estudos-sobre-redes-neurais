import numpy as np

# Dados iniciais
entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
saidasEsperadas = np.array([0,0,0,1])
pesos = np.array([0.0, 0.0])
taxaAprendizagem = 0.1

# Função de ativação binária
def stepFunction(resultadoFuncaoSoma):
    return 1 if resultadoFuncaoSoma >= 1 else 0

# Função que calcula a saída (soma ponderada + ativação)
def calcularSaida(entrada):
    soma = entrada.dot(pesos)
    return stepFunction(soma)

# Função para calcular o erro (com sinal)
def calcularErro(saidaEsperada, saidaCalculada):
    return saidaEsperada - saidaCalculada

# Função para atualizar os pesos com base no erro
def atualizarPesos(pesos, entrada, erro, taxa):
    for j in range(len(pesos)):
        pesos[j] += taxa * entrada[j] * erro
    return pesos

# Função para logar dados de uma iteração
def logDados(entrada, saidaEsperada, saidaCalculada, pesos, erro):
    print(f"Entrada: {entrada}, Esperado: {saidaEsperada}, Calculado: {saidaCalculada}")
    print("Pesos atuais:", pesos)
    if erro != 0:
        print("Erro:", erro)
        print("Atualizando pesos...\n")

# Função principal de treinamento
def treinarRede():
    erroTotal = 1
    while erroTotal != 0:
        erroTotal = 0
        for i in range(len(saidasEsperadas)):
            entradaAtual = entradas[i]
            saidaCalculada = calcularSaida(entradaAtual)
            erro = calcularErro(saidasEsperadas[i], saidaCalculada)
            erroTotal += abs(erro)

            logDados(entradaAtual, saidasEsperadas[i], saidaCalculada, pesos, erro)

            if erro != 0:
                atualizarPesos(pesos, entradaAtual, erro, taxaAprendizagem)

        print("Pesos atualizados:", pesos)
        print("Erro total da época:", erroTotal)
        print("Nova tentativa com pesos atualizados!\n")

# Inicia o treinamento
treinarRede()
