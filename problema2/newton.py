import math

def f(x):
    return math.cos(x) - x  # Função do problema cos(x) - x

def df(x):
    return -math.sin(x) - 1  # Derivada da função: -sin(x) - 1

def metodo_newton(f, df, x, tol1=1e-4, tol2=1e-4, max_iter=25): # método de Newton-Raphson
    if abs(f(x)) < tol1:
        return x, 0, 0, f(x)
    
    k = 1
    diferenca = float('inf')
    while True:
        x1 = x - f(x) / df(x)  # Ajusta a estimativa na direção da raiz usando a tangente
        diferenca = abs(x1 - x) # Diferença entre as estimativas 
        print(f"Iteração {k}: x = {x1:.8f}, f(x) = {f(x1):+.2e}")
        
        if abs(f(x1)) < tol1 or diferenca < tol2 or k >= max_iter: # Verificação das condições de parada
            return x1, k, diferenca, f(x1)
        
        x = x1
        k += 1

