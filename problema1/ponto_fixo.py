#Função de iteração
def phi(x):
    return (4 * x + 9) ** (1/3)
 
#Função do ponto fixo
def ponto_fixo(a, b, tolerancia = 1e-4, maximo_iteracoes = 25):
    #Calcula a metade do intervalo
    x0 = (a + b) / 2
    x = x0 
    iteracoes = 0 #Contador de iterações

    #Loop enquanto o número de iterações for menor que o número máximo de iterações
    while iteracoes < maximo_iteracoes:
        y = phi(x)  # Aplica a função phi(x) no valor atual de x
        iteracoes += 1  #Incrementa o contador
        
        #Imprime o número da iteração, a aproximação atual e a diferença entre as iterações
        print(f"Iteração: {iteracoes}, Aproximação: {y:.6f}, Diferença: {abs(y - x):.6f}")

        #Verifica se a diferença entre as iterações é menor que a tolerância
        if abs(y - x) < tolerancia:
            #Se estiver ok, imprime o valor da raiz e a quantidade de iterações foi necessária para chegar ao resultado
            print(f"Raiz encontrada: {y:.6f} após {iteracoes} iterações")
            return y  #Retorna o valor aproximado da raiz

        #Atualiza para a próxima aproximação
        x = y
        
#Intervalo [a, b]
a = 2 
b = 3  

#Chama a função ponto_fixo
raiz = ponto_fixo(a, b)