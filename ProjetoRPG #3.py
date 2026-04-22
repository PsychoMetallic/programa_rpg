import random

azul = "\033[34m"
branco = "\033[37m"
verde = "\033[32m"
amarelo = "\033[33m"
roxo = "\033[35m"
vermelho = "\033[31m"
ciano = "\033[36m"


print("-"*150)
nome=input("Qual é o Seu Nome? ")
print("-"*150)

print("Escolha sua Classe, Por Favor!")
classe = input("Mago / Executor / Guerreiro: ").lower()
print("-"*150)

while classe != "mago" and classe != "executor" and classe != "guerreiro":
    print("Resposta Inválida! Tente Novamente!")
    classe = input("Mago, Executor ou Guerreiro: ").lower()
    print("-"*150)
    
print("Classe Escolhida:", classe.capitalize())

print()
print("Olá", nome.capitalize(), "ficamos felizes por ter Entrado em Nossa Guilda!")
print("-"*150)

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
print("-"*150)

hp = nível * 100
mana = nível * 75
reais = nível * 50

print("Hp:", hp,)
print(f"{ciano}Mana:", mana)
print(f"{amarelo}Dinheiro:", reais)
print(f"{branco}-"*150)

pocao = 11.99

print(f"{amarelo}Comerciante:{branco} Bem vindo a Loja da Guilda, temos essa Poção que custa R$11.99!")
loja = input("Você quer Comprar? Y/N: ").strip().lower() in ["sim", "s", "y"]
print("-"*150)

qtd = 0

if loja:
    if reais < 11.99:
        print(f"{amarelo}Comerciante:{branco} Você não tem {amarelo}Dinheiro{branco} Suficiente!")
        print("-"*150)
          
    
    else:
        qtd = int(input(f"{amarelo}Comerciante:{branco} Quantas Poções Você Deseja? "))
        venda = qtd * pocao
        
        print("-"*150)
        
        if qtd <=0:
            print(f"{amarelo}Comerciante:{branco} Muito Engraçado... Saia da Minha Loja!!!")
            qtd = 0
            print("-"*150)
        
        elif reais < venda:
            print(f"{amarelo}Comerciante:{branco} Seu {amarelo}Dinheiro{branco} é Insuficiente!")
            qtd = 0
            print("-"*150)
            
        elif reais >= venda:
            reais -= venda
            print(f"{amarelo}Comerciante:{branco} São Todas Suas Campeão!")
            print(qtd, "Poções Adicionadas Ao Inventário")
            print(f"{amarelo}Comerciante:{branco} Aqui está seu troco:",round(reais, 2))
            print("-"*150)

            
        else:
            print("Resposta Inválida!")
            print("-"*150)   
            
else:
    print(f"{amarelo}Comerciante:{branco} Volte Sempre!")
    print("-"*150)

import time
train = 3
for i in range(3):
    print("Você Voltou de um Treinamento Árduo que Durou 3 Anos!")
    print("E quando Volta para sua Cidade Natal...")
    print("Um Problema Aparece!!!")
    print("-"*150)
    time.sleep(2)
    break

bosshp = 10000
print(f"Oh Não, Apareceu um {roxo}Dragão {branco}e Ele está Atacando o Vilarejo!")

if nível < 30:
    print()
    print("Porém, Você é Muito Fraco para Enfrentar um Inimigo tão Forte!")
    print(f"O {roxo}Dragão {branco}Destruiu o Vilarejo!")
    print(f"{vermelho}GAME OVER!{branco}")
    print("-"*150)

else:
    while bosshp > 0:
        print(f"A Vida dele está em: {roxo}{bosshp}{branco}")
        print()

        luta = input("Oque Você Fará? 1-Atacar / 2-Fugir / 3-Magia / 4-Bomba: ")
        print()
        print("Validando Ação, Aguarde...")
        time.sleep(1)
        print("-"*150)

        if luta == "1":
            sorte = random.randint(1, 100)
            
            if sorte <= 20:
                print()
                print("Você errou o Ataque!!!")
                print()
                print("-"*150)
                
            elif sorte >=21:
                atk = random.randint(1, 100)

            if atk >= 90:
                    print()
                    print(f"Você deu Um SuperPulo e Cortou a Cabeça do {roxo}Dragão{branco}")
                    print("Causando 10000 de Dano!")
                    print()
                    dano = 10000
                    bosshp = bosshp - dano
                    print("-"*150)

            elif atk >= 60:
                    print()
                    print("Você Cortou a Barriga dele! o Corte foi Profundo!!!")
                    print("Causando 3000 de Dano!")
                    print()
                    dano = 3000
                    bosshp = bosshp - dano
                    print("-"*150)
                    
            elif atk >= 30:
                    print()
                    print("Você deu um Superpulo e Desferiu Vários Cortes em sequência no Rosto dele!")
                    print("Causando 2000 de Dano!")
                    print()
                    dano = 2000
                    bosshp = bosshp - dano
                    print("-"*150)
                        
            elif atk >= 1:
                    print()
                    print("Você Desferiu um corte na Perna dele!")
                    print("Causando 1000 de Dano!")
                    print()
                    dano = 1000
                    bosshp = bosshp - dano
                    print("-"*150)

        elif luta == "3":
            sorte = random.randint(1, 100)
            
            if sorte <= 20:
                print()
                print("Você usou a Magia Errada!!!")
                print()
                print("-"*150)
                
            elif sorte >=21:

                mg = random.randint(1, 100)

                if mg >= 90 and mana >= 1000:
                    print()
                    print("Você Esmagou o Crânio Dele!")
                    print(f"Causando 10000 de Dano e Gastando {ciano}1000 de Mana!")
                    print()
                    dano = 10000
                    bosshp = bosshp - dano
                    gasto = 1000
                    mana = mana - gasto
                    print("Mana Restante:", mana)
                    print()
                    print(f"{branco}-"*150)

                elif mg >= 60 and mana >= 700:
                    print()
                    print("Você Prensou ele com Duas Pedras!")
                    print(f"Causando 1500 de Dano e Gastando {ciano}700 de Mana!")
                    print()
                    dano = 1500
                    bosshp = bosshp - dano
                    gasto = 700
                    mana = mana - gasto
                    print("Mana Restante:", mana)
                    print()
                    print(f"{branco}-"*150)

                elif mg >= 30 and mana >= 550:
                    print()
                    print("Você Lançou uma Bola de Fogo nele!")
                    print(f"Causando 1000 de Dano e Gastando {ciano}550 de Mana!")
                    print()
                    dano = 1000
                    bosshp = bosshp - dano
                    gasto = 550
                    mana = mana - gasto
                    print("Mana Restante:", mana)
                    print()
                    print(f"{branco}-"*150)

                elif mg >= 1 and mana >= 400:
                    print()
                    print("Você Conseguiu Criar um Boneco feito com os Escombros para Atacá-lo! mas o Efeito acabou Rápido e seu Boneco foi Destruído!")
                    print(f"Mas Causou 600 de Dano e Gastou {ciano}400 de Mana!")
                    print()
                    dano = 600
                    bosshp = bosshp - dano
                    gasto = 400
                    mana = mana - gasto
                    print("Mana Restante:", mana)
                    print()
                    print(f"{branco}-"*150)

                else:
                    print()
                    print(f"{ciano}Mana {branco}Insuficiente!")
                    print()
                    print("-"*150)

            elif sorte >=51 and mana <= 199:
                    print()
                    print(f"{ciano}Mana {branco}Insuficiente!")
                    print()
                    print("-"*150)

        elif luta == "2":
            sorte = random.randint(1, 100)
            
            if sorte <= 60:
                print()
                print(f"sua Tentativa de Fuga Falhou o {roxo}Dragão{branco} te Matou!!!")
                print(f"{vermelho}GAME OVER!{branco}")
                print()
                print("-"*150)
                break
                
            elif sorte >=61:
                print()
                print(f"Você Fugiu do {roxo}Dragão {branco}com Sucesso!")
                print("Porém, O Vilarejo foi Destruído...")
                print(f"{vermelho}GAME OVER!{branco}")
                print()
                print("-"*150)
                break

        elif luta == "4":
            sorte = random.randint(1, 100)
            
            if sorte <= 50:
                import time

                bomba = 5
                while bomba > 0:
                    print(bomba)
                    bomba -= 1
                    time.sleep(0.3)
                print("BOOM!!!")
                print("Você Errou a Bomba!")
                print("-"*150)

                
            elif sorte >=51:

                bomb = random.randint(1, 100)

                if bomb <= 40:
                    import time

                    bomba = 5
                    while bomba > 0:
                        print(bomba)
                        bomba -= 1
                        time.sleep(0.3)
                    print("BOOM!!!")
                    print(f"Na hora que o {roxo}Dragão {branco}Abriu a Boca, Você lançou a Bomba na Garganta Dele!")
                    print("Causando 5000 de Dano!")
                    dano = 5000
                    bosshp = bosshp - dano

                    print("-"*150)
                    
                elif bomb >= 60:
                    import time

                    bomba = 5
                    while bomba > 0:
                        print(bomba)
                        bomba -= 1
                        time.sleep(0.3)
                    print("BOOM!!!")
                    print(f"Você lançou a Bomba no {roxo}Dragão{branco}, Machucou Muito!")
                    print("Causando 1500 de Dano!")
                    dano = 1500
                    bosshp = bosshp - dano
                    print("-"*150)

            else:
                print()
                print(f"Ação Inválida! Você demorou Para Responder e o {roxo}Dragão {branco}Obliterou a Vila!")
                print(f"{vermelho}GAME OVER!{branco}")
                print()
                print("-"*150)
                break

                    
    if bosshp <= 0:
        print()
        print(f"O {roxo}Dragão {branco}está Morto, Você salvou o Vilarejo!!!")
        print()

        povo = input(f"{verde}Povo do Vilarejo:{branco} MUITO OBRIGADO {verde}{nome.upper()}{branco} VOCÊ NOS SALVOU, PEGUE ISSO COMO RECOMPENSA: ")
        
        win = 10000
        reais += win
        print()

        print(f"{amarelo}{win} Reais{branco} Adicionados ao Banco")
        print()

        print(f"Seu saldo Agora é: {amarelo}", round(reais, 2))
        print()
        print(f"{branco}-"*150)