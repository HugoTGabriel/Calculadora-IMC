usuário = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = int(input("Digite o seu peso atual (em kg): "))
altura = float(input("Digite a sua altura atual (em centímetros): ")) / 100

opcoes = ["Calcular IMC", "Definir exercícios", "Lista de alimentos", "Sair"]

while True:
    print("\nMenu")
    for i, opcao in enumerate(opcoes, start=1):
        print(f"{i}. {opcao}")

    escolha = int(input("Escolha uma opçao: "))

    if escolha == 1:
        print("Ok, vamos calcular seu IMC")

        imc = peso / (altura**2)

        print(f"Seu IMC atualmente é de {imc:.2f}. Com isso, você está:")

        n1 = imc

        if n1 < 18.5:
            print("Abaixo do peso")
            categoria = "Abaixo do peso"
        elif 18.5 <= n1 < 25:
            print("Com peso normal")
            categoria = "Com peso normal"
        elif 25 <= n1 < 30:
            print("Acima do peso")
            categoria = "Acima do peso"
        elif 30 <= n1 < 35:
            print("Com obesidade grau 1")
            categoria = "Com obesidade grau 1"
        elif 35 <= n1 < 40:
            print("Com obesidade grau 2")
            categoria = "Com obesidade grau 2"
        else:
            print("Com obesidade grau 3")
            categoria = "Com obesidade grau 3"

    elif escolha == 2:
        print("Ok, vamos definir alguns exercícios básicos para se realizar em casa.")

        if "categoria" in locals():

            if categoria == "Abaixo do peso":
                print("- Agachamentos simples (corpo livre).")
                print("- Flexões de braço (ajoelhado, se necessário).")
                print("- Elevação de panturrilha (em um degrau).")
                print("- Yoga ou Pilates (para melhorar o equilíbrio).")

            elif categoria == "Com peso normal":
                print("- Polichinelos (aquecimento).")
                print("- Abdominais básicos.")
                print("- Prancha (começar com 20-30 segundos).")
                print("- Corrida estacionária ou caminhada rápida no local.")

            elif categoria == "Acima do peso":
                print("- Caminhada em casa (marcando o passo no mesmo lugar).")
                print("- Agachamento com apoio (encostado em uma parede).")
                print("- Exercícios com elásticos (resistência moderada).")
                print("- Alongamentos.")

            elif categoria == "Com obesidade grau 1":
                print("- Caminhada leve (no local ou em um espaço pequeno).")
                print("- Alongamentos dinâmicos (pescoço, braços e pernas).")
                print("- Elevação de joelhos (baixo impacto).")

            elif categoria == "Com obesidade grau 2":
                print("- Movimentos de dança simples (para divertir e estimular o movimento).")
                print("- Marcha estacionária.")
                print("- Alongamento estático (foco na respiração).")

            elif categoria == "Com obesidade grau 3":
                print("- Exercícios sentados (elevação de pernas, rotação de ombros).")
                print("- Respiração profunda (para relaxamento e controle).")
                print("- Alongamentos simples (de pescoço, braços e pernas).")
                
        else:
            print("Valor inválido, insira os dados novamente!")

    elif escolha == 3:
        print("Tudo bem, aqui vai uma lista de bons alimentos para suas refeições.")
        
        if "categoria" in locals():
            if categoria == "Abaixo do peso":
                print("- Frutas secas (ex.: castanhas e amêndoas)")
                print("- Abacate (ótima fonte de calorias boas).")
                print("- Arroz integral.")
            elif categoria == "Com peso normal":
                print("- Frutas frescas (maçã, laranja, banana).")
                print("- Verduras e legumes variados.")
                print("- Proteínas magras (frango, peixe).")
            elif categoria == "Acima do peso" or "Com obesidade grau 1" in categoria:
                print("- Carnes magras.")
                print("- Leguminosas (feijão, grão-de-bico).")
                print("- Alimentos integrais.")
            else:
                print("- Dieta baseada em orientação médica.")
        else:
            print("Inclua alimentos saudáveis como frutas, legumes e proteínas magras.")

    elif escolha == 4:
        print("Ok, até logo!")
        break

    else:
        print("Opção inválida! Selecione algumas das opções acima para continuar.")
