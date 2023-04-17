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
        baseret = float(input("Qual é a medida da base do seu retângulo? "))
        alturaret = float(input("Qual é a altura do seu retângulo? "))
        permret = 2*baseret+2*alturaret
        arearet = baseret*alturaret
        print("O perímetro do seu retângulo é ", permret, "\nA área do seu retângulo é ", arearet)
        
    elif acao == "2":
        print("No caso, necessitamos de duas informações para fornecer o perímetro e a base da forma solicitada")
        basetr = float(input("Qual é a medida da base do seu triângulo retângulo? "))
        alturatr = float(input("Qual é a altura do seu triângulo retângulo? "))
        c2 = basetr*basetr + alturatr*alturatr
        c = math.sqrt(c2)
        permtr = basetr + alturatr + c
        areatr = (basetr*alturatr)/2
        print("O perímetro do seu triângulo retângulo é ", permtr, "\nA área do seu triângulo retângulo é ", areatr)
        
    elif acao == "3":
        print("No caso, necessitamos da medida do raio do seu círculo")
        raio = float(input("Qual é o raio do seu círculo? "))
        permcir = 2 * math.pi * raio
        areacir = math.pi * (raio*raio)
        print("O perímetro do seu círculo é ", permcir, "\nA área do seu círculo é ", areacir)
        
    else:
        print("Por favor, escolha uma opção válida.")
        
    escolha = input("Deseja continuar? (sim/não): ")
    if escolha == "não":
        terminou = True

print("Obrigado por utilizar a calculadora de formas!")  
