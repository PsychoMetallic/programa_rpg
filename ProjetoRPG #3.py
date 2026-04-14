import random

azul = "\033[34m"
branco = "\033[37m"
verde = "\033[32m"
amarelo = "\033[33m"
roxo = "\033[35m"
vermelho = "\033[31m"

print("-"*260)
nome=input("Qual é o Seu Nome? ")
print("-"*260)

print("Escolha sua Classe, Por Favor!")
classe = input("Mago / Executor / Guerreiro: ").lower()
print("-"*260)

while classe != "mago" and classe != "executor" and classe != "guerreiro":
    print("Resposta Inválida! Tente Novamente!")
    classe = input("Mago, Executor ou Guerreiro: ").lower()
    print("-"*260)
    
print("Classe Escolhida:", classe.capitalize())

print()
print("Olá", nome.capitalize(), "ficamos felizes por ter Entrado em Nossa Guilda!")
print("-"*260)

nível = int(input("Qual é o seu Nível? "))

if nível >= 1 and nível <=100:
    print()
    print("Bem Vindo a Guilda dos Aventureiros, seu Nível é:", nível)
    
elif nível <= 0:
    nível=1
    print("você não é tão fraco assim, seu nível agora é:", nível)

else:
    print()
    nível = 1
    print("O Nível Máximo é 100! sua Punição por ter Mentido é, seu Nível será:", nível)

print()
print("Esses são seus atributos!: ")
print("-"*260)

hp = nível * 100
mana = nível * 75
reais = nível * 50

print("Hp:", hp,)
print("Mana:", mana)
print(f"{amarelo}Dinheiro:", reais)
print(f"{branco}-"*260)

pocao = 11.99

print(f"{amarelo}Comerciante:{branco} Bem vindo a Loja da Guilda, temos essa Poção que custa R$11.99!")
loja = input("Você quer Comprar? Y/N: ").strip().lower() in ["sim", "s", "y"]
print("-"*260)

qtd = 0

if loja:
    if reais < 11.99:
        print(f"{amarelo}Comerciante:{branco} Você não tem {amarelo}Dinheiro{branco} Suficiente!")
        print("-"*260)
          
    
    else:
        qtd = int(input(f"{amarelo}Comerciante:{branco} Quantas Poções Você Deseja? "))
        venda = qtd * pocao
        
        print("-"*260)
        
        if qtd <=0:
            print(f"{amarelo}Comerciante:{branco} Muito Engraçado... Saia da Minha Loja!!!")
            qtd = 0
            print("-"*260)
        
        elif reais < venda:
            print(f"{amarelo}Comerciante:{branco} Seu {amarelo}Dinheiro{branco} é Insuficiente!")
            qtd = 0
            print("-"*260)
            
        elif reais >= venda:
            reais -= venda
            print(f"{amarelo}Comerciante:{branco} São Todas Suas Campeão!")
            print(qtd, "Poções Adicionadas Ao Inventário")
            print(f"{amarelo}Comerciante:{branco} Aqui está seu troco:",round(reais, 2))
            print("-"*260)

            
        else:
            print("Resposta Inválida!")
            print("-"*260)   
            
else:
    print(f"{amarelo}Comerciante:{branco} Volte Sempre!")
    print("-"*260)

import time
train = 3
for i in range(3):
    print("Você Voltou de um Treinamento Árduo que Durou 3 Anos!")
    print("E quando Volta para sua Cidade Natal...")
    print("Um Problema Aparece!!!")
    print("-"*260)
    time.sleep(2)
    break

bosshp = 10000
print(f"Oh Não, Apareceu um {roxo}Dragão {branco}e Ele está Atacando o Vilarejo!")

while bosshp > 0:
    print("A Vida dele está em:", bosshp)
    print()

    luta = input("Oque Você Fará? 1-Atacar / 2-Fugir / 3-Magia / 4-Bomba: ")
    print()
    print("Validando Ação, Aguarde...")
    time.sleep(1)
    print("-"*260)

    if luta == "1":
        sorte = random.randint(1, 100)
        
        if sorte <= 20:
            print()
            print("Você errou o Ataque!!!")
            print()
            print("-"*260)
            
        elif sorte >=21:
           atk = random.randint(1, 100)

           if atk >= 90:
                print()
                print(f"Você deu Um SuperPulo e Cortou a Cabeça do {roxo}Dragão{branco}")
                print("Causando 10000 de Dano!")
                print()
                dano = 10000
                bosshp = bosshp - dano
                print("-"*260)

           elif atk >= 60:
                print()
                print("Você Cortou a Barriga dele! o Corte foi Profundo!!!")
                print("Causando 3000 de Dano!")
                print()
                dano = 3000
                bosshp = bosshp - dano
                print("-"*260)
                
           elif atk >= 30:
                print()
                print("Você deu um Superpulo e Desferiu Vários Cortes em sequência no Rosto dele!")
                print("Causando 2000 de Dano!")
                print()
                dano = 2000
                bosshp = bosshp - dano
                print("-"*260)
                    
           elif atk >= 1:
                print()
                print("Você Desferiu um corte na Perna dele!")
                print("Causando 1000 de Dano!")
                print()
                dano = 100
                bosshp = bosshp - dano
                print("-"*260)

    elif luta == "3":
        sorte = random.randint(1, 100)
        
        if sorte <= 50:
            print()
            print("Você usou a Magia Errada!!!")
            print()
            print("-"*260)
            
        elif sorte >=51:

            mg = random.randint(1, 100)

            if mg >= 90 and mana >= 1000:
                print()
                print("Você Esmagou o Crânio Dele!")
                print("Causando 10000 de Dano e Gastando 1000 de Mana!")
                print()
                dano = 10000
                bosshp = bosshp - dano
                gasto = 1000
                mana = mana - gasto
                print("Mana Restante:", mana)
                print()
                print("-"*260)

            elif mg >= 60 and mana >= 500:
                print()
                print("Você Prensou ele com Duas Pedras!")
                print("Causando 1500 de Dano e Gastando 500 de Mana!")
                print()
                dano = 1500
                bosshp = bosshp - dano
                gasto = 500
                mana = mana - gasto
                print("Mana Restante:", mana)
                print()
                print("-"*260)

            elif mg >= 30 and mana >= 350:
                print()
                print("Você Lançou uma Bola de Fogo nele!")
                print("Causando 1000 de Dano e Gastando 350 de Mana!")
                print()
                dano = 1000
                bosshp = bosshp - dano
                gasto = 350
                mana = mana - gasto
                print("Mana Restante:", mana)
                print()
                print("-"*260)

            elif mg >= 1 and mana >= 400:
                print()
                print("Você Conseguiu Criar um Boneco feito com os Escombros para Atacá-lo! mas o Efeito acabou Rápido e seu Boneco foi Destruído!")
                print("Mas Causou 600 de Dano e Gastou 400 de Mana!")
                print()
                dano = 600
                bosshp = bosshp - dano
                gasto = 400
                mana = mana - gasto
                print("Mana Restante:", mana)
                print()
                print("-"*260)

            else:
                print()
                print("Mana Insuficiente!")
                print()
                print("-"*260)

        elif sorte >=51 and mana <= 199:
                print("Mana Insuficiente!")
                print("-"*260)

    elif luta == "2":
        sorte = random.randint(1, 100)
        
        if sorte <= 60:
            print()
            print(f"sua Tentativa de Fuga Falhou o {roxo}Dragão{branco}te Matou!!!")
            print(f"{vermelho}GAME OVER!")
            print()
            print("-"*260)
            break
            
        elif sorte >=61:
            print()
            print(f"Você Fugiu do {roxo}Dragão {branco}com Sucesso!")
            print("Porém, O Vilarejo foi Destruído...")
            print(f"{vermelho}GAME OVER!")
            print()
            print("-"*260)
            break

    elif luta == "4":
        sorte = random.randint(1, 100)
        
        if sorte <= 50:
            import time

            bomba = 10
            while bomba > 0:
                print(bomba)
                bomba -= 1
                time.sleep(0.5)
            print("BOOM!!!")
            print("Você Errou a Bomba!")
            print("-"*260)

            
        elif sorte >=51:

            bomb = random.randint(1, 100)

            if bomb <= 40:
                import time

                bomba = 10
                while bomba > 0:
                    print(bomba)
                    bomba -= 1
                    time.sleep(0.5)
                print("BOOM!!!")
                print(f"Na hora que o {roxo}Dragão {branco}Abriu a Boca, Você lançou a Bomba na Garganta Dele!")
                print("Causando 5000 de Dano!")
                dano = 5000
                bosshp = bosshp - dano

                print("-"*260)
                
            elif bomb >= 60:
                import time

                bomba = 10
                while bomba > 0:
                    print(bomba)
                    bomba -= 1
                    time.sleep(0.5)
                print("BOOM!!!")
                print(f"Você lançou a Bomba no {roxo}Dragão{branco}, Machucou Muito!")
                print("Causando 1000 de Dano!")
                dano = 1000
                bosshp = bosshp - dano
                print("-"*260)

        else:
            print()
            print(f"Ação Inválida! Você demorou Para Responder e o {roxo}Dragão {branco}Obliterou a Vila!")
            print(f"{vermelho}GAME OVER!")
            print()
            print("-"*260)
            break

                
if bosshp <= 0:
    print()
    print(f"O {roxo}Dragão {branco}está Morto, Você salvou o Vilarejo!!!")
    print()

    povo = input(f"{verde}Povo do Vilarejo:{branco} MUITO OBRIGADO {nome.upper()} VOCÊ NOS SALVOU, PEGUE ISSO COMO RECOMPENSA: ")
    
    win = 10000
    reais += win
    print()

    print(f"{amarelo}{win} Reais{branco} Adicionados ao Banco")
    print()

    print(f"Seu saldo Agora é: {amarelo}", round(reais, 2))
    print()
    print(f"{branco}-"*260)