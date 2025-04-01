import math

def f(x):
    return math.cos(x) - x  # Função do problema cos(x) - x

def df(x):
    return -math.sin(x) - 1  # Derivada da função: -sin(x) - 1

def newton_method(f, df, x0, tol1=1e-6, tol2=1e-6, max_iter=100): # método de Newton-Raphson
    if abs(f(x0)) < tol1:
        return x0, 0, 0, f(x0)
    
    k = 1
    diferenca = float('inf')
    while True:
        x1 = x0 - f(x0) / df(x0)  # Ajusta a estimativa na direção da raiz usando a tangente
        diferenca = abs(x1 - x0) # Diferença entre as estimativas 
        print(f"Iteração {k}: x = {x1:.8f}, f(x) = {f(x1):+.2e}")
        
        if abs(f(x1)) < tol1 or diferenca < tol2 or k >= max_iter: # Verificação das condições de parada
            return x1, k, diferenca, f(x1)
        
        x0 = x1
        k += 1

a, b = 0, 1  # Intervalo dado no problema
x0 = (a + b) / 2  # Ponto inicial (metade do intervalo)

raiz, iteracoes, diferenca_final, valor_funcao = newton_method(f, df, x0) # Chamada do método
print(f"Raiz aproximada: {raiz:.8f}")
print(f"Número de iterações: {iteracoes}")
print(f"Diferença final: {diferenca_final:.2e}")
print(f"Valor da função na raiz: {valor_funcao:.2e}")