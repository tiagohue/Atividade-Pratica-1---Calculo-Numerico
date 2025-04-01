from problema4.posicao_falsa import calcular_posicao_falsa, f

if __name__ == '__main__':
    epsilon = 10**(-4)
    
    calcular_posicao_falsa(a=0, b=1, epsilon1=epsilon, epsilon2=epsilon, iterMax=25)