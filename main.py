from problema1.ponto_fixo import ponto_fixo
from problema2.newton import metodo_newton, f, df
from problema3.bissecao import bissecao, f_problema3
from problema4.posicao_falsa import calcular_posicao_falsa

if __name__ == '__main__':
    epsilon = 10**(-4)

    print("\nChamada do metodo do Ponto Fixo, problema 1:\n")
    ponto_fixo(2, 3)

    print("\nChamada do metodo de Newton, problema 2:\n")
    a, b = 0, 1  # Intervalo dado no problema
    x = (a + b) / 2  # Ponto inicial (metade do intervalo)

    raiz, iteracoes, diferenca_final, valor_funcao = metodo_newton(f, df, x) # Chamada do método
    print(f"Raiz aproximada: {raiz:.8f}")
    print(f"Número de iterações: {iteracoes}")
    print(f"Diferença final: {diferenca_final:.2e}")
    print(f"Valor da função na raiz: {valor_funcao:.2e}")
    
    print("\nChamada do metodo da Bissecao, problema 3:\n")
    bissecao(f_problema3, 1, 2, epsilon, 25)

    print("\nChamada do metodo da Posicao Falsa, problema 4:\n")
    calcular_posicao_falsa(a=0, b=1, epsilon1=epsilon, epsilon2=epsilon, iterMax=25)