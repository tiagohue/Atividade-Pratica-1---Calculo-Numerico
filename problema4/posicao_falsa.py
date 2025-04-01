from random import choice
from math import e


def f(x: float):
    """
    Calcula a função da quarta questão a partir de um x real.

    Args:
        x (float): A variável da função.

    Returns:
        float: O y resultando do x.
    """
    return (e ** x) - 4 * x

def escolha(a: float, b: float):
    """
    Retorna "aleatoriamente" um dos dois números recebidos.

    Args:
        a (float): Um número flutuante.
        b (float): Um número flutuante.

    Returns:
        float: O número escolhido "aleatoriamente".
    """
    return choice((a, b))

def calcular_posicao_falsa(a: float, b: float, epsilon1: float, epsilon2: float, iterMax: int):
    """
    Aplica o método da posição falsa para descobrir a raíz de uma função.

    Args:
        a (float): Início do intervalo.
        b (float): Fim do intervalo.
        epsilon1 (float): Critério de parada 1.
        epsilon2 (float): Critério de parada 2.
        iterMax (float): Iterações máxima do método.

    Returns:
        float: Raiz aproximada encontrada.
    """
    Fa = f(a)
    Fb = f(b)

    if Fa * Fb > 0:
        print('“Erro: função não muda de sinal entre a e b')
        return

    intervX = abs(b-a)

    if intervX < epsilon1:
        raiz = escolha(a, b)
        return raiz
    if abs(Fa) < epsilon2:
        raiz = a
        return raiz
    if abs(Fb) < epsilon2:
        raiz = b
        return raiz
    k = 0

    while(True):
        x = (a * Fb - b * Fa)/(Fb-Fa)
        Fx = f(x)
        print(k, a, Fa, b, Fb, x, Fx, intervX)
        if abs(f(x)) < epsilon2 or k >= iterMax:
            raiz = x
            break

        if Fa * Fx > 0:
            a = x
            Fa = Fx

        else: 
            b = x
            Fb = Fx

        intervX = abs(b-a)
        if intervX <= epsilon1:
            raiz = escolha(a,b)
            break
        k = k+1

    return raiz