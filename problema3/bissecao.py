import math

#definicao do metodo de bissecao
def bissecao (f, a, b, epson, maxIter):
    fa = f(a)
    fb = f(b)
    
    if fa*fb > 0:
        print("Erro: funcao nao muda de sinal entre a e b")
        return
    
    intervX = abs(b - a)
    k = 0
    while True:
        x = (a + b)/2
        fx = f(x)
        
        print(f"k = {k}, a = {k}, fa = {fa}, fb = {fb}, x = {x}, fx = {fx},  intervX = {intervX}")
        
        #caso de parada
        if intervX <= epson or k >= maxIter:
            break
        
        #descobre se a raiz está em [a, x] ou [x, b]
        if fa * fx > 0:
            a = x
            fa = fx
        else:
            b = x
            fb = fx
            
        intervX = intervX / 2
        k = k + 1
        
    raiz = x

    return raiz;

#definicao de f(x)
#f(x) = ln(x) + x^2 - 3
def f(x):
    return math.log(x) + x**2 - 3

#chamada do método
bissecao(f, 1, 2, 10**-4, 25)