import math
print("Seja bem vindo a calculadora de formas pessoal.")
print("Bom dia!")
nome = input("Qual é o seu nome? ")
print("Bem-vindo à calculadora de formas, " + nome + "!")
terminou = False

while not terminou:
    print("[1] Retângulo\n[2] Triângulo retângulo\n[3] Círculo")
    acao = input("De qual tipo de forma que você quer informações? ")
    
    if acao == "1":
        print("Nesse caso, precisamos de duas informações para fornecer o perímetro e a base da forma em questão")
        while True:
            try:
                baseret = float(input("Qual é a medida da base do seu retângulo? "))
                break
            except ValueError:
                print("Essa não é uma resposta válida, tente novamente")
        while True:
            try:
                alturaret = float(input("Qual é a altura do seu retângulo? "))
                break
            except ValueError:
                print("Essa não é uma resposta válida, tente novamente")
        permret = 2*baseret+2*alturaret
        arearet = baseret*alturaret
        print("O perímetro do seu retângulo é ", permret, "\nA área do seu retângulo é ", arearet, "\nA fórmula utilizada para encontrar o perímetro é a soma de todos os lados, que, em um retângulo, são dois pares iguais.\nJá a área foi obtida pela multiplicação da base pela altura.")
        
    elif acao == "2":
        print("No caso, necessitamos de duas informações para fornecer o perímetro e a base da forma solicitada")
        while True:
            try:
                basetr = float(input("Qual é a medida da base do seu triângulo retângulo? "))
                break
            except ValueError:
                print("Essa não é uma resposta válida, tente novamente")
        while True:
            try:
                alturatr = float(input("Qual é a altura do seu triângulo retângulo? "))
                break
            except ValueError:
                print("Essa não é uma resposta válida, tente novamente")
        c2 = basetr*basetr + alturatr*alturatr
        c = math.sqrt(c2)
        permtr = basetr + alturatr + c
        areatr = (basetr*alturatr)/2
        print("O perímetro do seu triângulo retângulo é ", permtr, "\nA área do seu triângulo retângulo é ", areatr, "\nA fórmula utilizada para descobrir o perímetro do triângulo retângulo foi o teorema de Pitágoras. Nele, com dois lados do triângulo retângulo, nós conseguimos a partir da estrutura: a^2[base elevada a dois]+b^2[altura elevada a dois]=c^2[hipotenusa elevada a dois].\n A área foi calculada multiplicando a base pela altura e dividindo o resultado por dois")
        
    elif acao == "3":
        print("No caso, necessitamos da medida do raio do seu círculo")
        while True:
            try:
                raio = float(input("Qual é o raio do seu círculo? "))
                break
            except ValueError:
                print("Essa não é uma resposta válida, tente novamente")
        permcir = 2 * math.pi * raio
        areacir = math.pi * (raio*raio)
        print("O perímetro do seu círculo é ", permcir, "\nA área do seu círculo é ", areacir, "\nA fórmula utilizada para conseguir o perímetro da circunferência é: 2*pi[3,14]*r[raio da circunferência].\nPara conseguirmos a área, a fórmula para a área é: pi*r^2[raio ao quadrado]")
        
    else:
        print("Por favor, escolha uma opção válida.")
        
    while True:
        try:
            escolha = input("Deseja continuar? (sim/não): ")
            break
        except ValueError:
            print("Essa não é uma resposta válida, tente novamente")
    if escolha == "não":
        terminou = True

print("Obrigado por utilizar a calculadora de formas!")  
