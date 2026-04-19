import random

# Cores do Terminal

azul = "\033[34m"
branco = "\033[37m"
verde = "\033[32m"
amarelo = "\033[33m"
roxo = "\033[35m"
vermelho = "\033[31m"
verde1 = "\033[92m"

# Informações Iniciais

print("-"*150)
nome=input("Qual é o Seu Nome? ")
print("-"*150)

print("Escolha sua Classe, Por Favor!")
classe = input("Mago / Executor / Guerreiro / Arqueiro: ").lower()
print("-"*150)

while classe != "mago" and classe != "executor" and classe != "guerreiro" and classe != "arqueiro":
    print("Resposta Inválida! Tente Novamente!")
    classe = input("Mago / Executor / Guerreiro / Arqueiro: ").lower()
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

hp = nível * 50
mana = nível * 75
reais = nível * 100

print(f"{azul}Hp: {hp}")
print(f"{verde1}Mana: {mana}")
print(f"{amarelo}Dinheiro: {reais}")
print(f"{branco}-"*150)

# Loja da Guilda

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

# Inventário do Jogador

print("Inventário:")
print(f"Poção: {qtd}") 
if classe == "guerreiro":
    print("Espada de Ferro")
elif classe == "executor":
    print("Machado de Batalha")
elif classe == "mago":
    print("Cajado de Madeira")
elif classe == "arqueiro":
    print("Arco de Madeira")
    print("Flechas Comuns")
print("-"*150)

# Treinamento de 3 Anos

import time
train = 3
for i in range(3):
    print("Você Voltou de um Treinamento Árduo que Durou 3 Anos!")
    if nível <= 74:
        nível += 25
    elif nível >= 75 and nível <= 100:
        nível = 100
    print("Você Aumentou seu Nível, Agora Você é um Aventureiro de Nível", nível)
    print()
    print("Esses são seus novos atributos!: ")
    print("-"*150)

    hp = nível * 50
    mana = nível * 75

    print(f"{azul}Hp: {hp}")
    print(f"{verde1}Mana: {mana}")
    print(f"{amarelo}Dinheiro: {reais}")
    print(f"{branco}-"*150)

    print("Quando Volta para o seu Vilarejo, percebe que Ele está sob Ataque!!!")
    print("-"*150)
    time.sleep(2)
    break

# Batalha contra o Dragão

bosshp = nível * 100
print(f"Oh Não, Apareceu um {roxo}Dragão {branco}e Ele está Atacando o Vilarejo!")

while bosshp > 0:
    print(f"A Vida dele está em: {roxo}{bosshp}{branco}")
    print()

# Opções de Luta

    luta = input("Oque Você Fará? 1-Atacar / 2-Fugir / 3-Magia / 4-Bomba: ")
    print()
    print("Validando Ação, Aguarde...")
    time.sleep(1)
    print("-"*150)

# Luta = Atacar

    if luta == "1" and classe == ("guerreiro" or classe == "executor"):
        sorte = random.randint(1, 100)
            
        if sorte <= 20:
            print()
            print("Você errou o Ataque!!!")
            print()
            print("-"*150)
                
        elif sorte >=21:
            atk = random.randint(1, 100)

            if atk >= 90:
                dano = 10000
                bosshp = bosshp - dano
                print()
                print(f"Você deu Um SuperPulo e Cortou a Cabeça do {roxo}Dragão{branco}")
                print("Matando ele na Hora!!!")
                print()
                print("-"*150)

            elif atk >= 60:
                dano = nível * 35
                bosshp = bosshp - dano
                print()
                print("Você Cortou a Barriga dele! o Corte foi Profundo!!!")
                print(f"Causando {roxo}{dano}{branco} de Dano!")
                print()
                print("-"*150)
                    
            elif atk >= 30:
                dano = nível * 25
                bosshp = bosshp - dano
                print()
                print("Você deu um Superpulo e Desferiu Vários Cortes em sequência no Rosto dele!")
                print(f"Causando {roxo}{dano}{branco} de Dano!")
                print()
                print("-"*150)
                        
            elif atk >= 1:
                dano = nível * 10
                bosshp = bosshp - dano
                print()
                print("Você Desferiu um corte na Perna dele!")
                print(f"Causando {roxo}{dano}{branco} de Dano!")
                print()
                print("-"*150)

    elif luta == "1" and classe == "mago":
        print()
        print("Um Mago não é tão bom em Combate Corpo a Corpo, Tente Usar Magias!!!")
        print()
        print("-"*150)

    elif luta == "1" and classe == "arqueiro":
        sorte = random.randint(1, 100)
            
        if sorte <= 20:
            print()
            print("Você errou o Tiro!!!")
            print()
            print("-"*150)
                
        elif sorte >=21:
            atk = random.randint(1, 100)

            if atk >= 90:
                dano = 10000
                bosshp = bosshp - dano
                print()
                print(f"Você atirou uma Flecha que perfurou o Coração do {roxo}Dragão{branco}")
                print("Matando ele na Hora!!!")
                print()
                print("-"*150)

            elif atk >= 60:
                dano = nível * 35
                bosshp = bosshp - dano
                print()
                print("Você atirou uma Flecha na Barriga dele! e ela entrou muito fundo!!!")
                print(f"Causando {roxo}{dano}{branco} de Dano!")
                print()
                print("-"*150)
                    
            elif atk >= 30:
                dano = nível * 25
                bosshp = bosshp - dano
                print()
                print("Você deu um tiro na cabeça dele, mas ele conseguiu desviar, o Tiro Acertou o rosto dele!")
                print(f"Causando {roxo}{dano}{branco} de Dano!")
                print()
                print("-"*150)
                        
            elif atk >= 1:
                dano = nível * 10
                bosshp = bosshp - dano
                print()
                print("Você atirou uma Flecha na Perna dele!")
                print(f"Causando {roxo}{dano}{branco} de Dano!")
                print()
                print("-"*150)


# Luta = Magia

    elif luta == "3" and classe == "mago":
        sorte = random.randint(1, 100)

        print()
        print("Qual Magia Você Quer Usar?")
        magia = input("1-Bola de Fogo / 2-Telecinese / 3-Congelamento: ")
        print()
        print("Validando Magia, Aguarde...")
        time.sleep(1)
        print("-"*150)
            
        if sorte <= 10:
            print()
            print("Você Errou!!!")
            print()
            print("-"*150)
                
        elif sorte >=11:
            mg = random.randint(1, 100)

            if mg >= 90 and mana >= 1000 and magia == "2":

                print()
                print("Você Esmagou o Crânio Dele!")
                print(f"Matando ele na hora e Gastando {verde1}1000{branco} de Mana!")
                print()
                dano = 10000
                bosshp = bosshp - dano
                gasto = 1000
                mana = mana - gasto
                print(f"{verde1}Mana Restante: {mana}{branco}")
                print()
                print("-"*150)

            elif mg >= 60 and mana >= 700 and magia == "2":
                dano = nível * 35
                bosshp = bosshp - dano
                print()
                print("Você Prensou ele com Duas Pedras!")
                print(f"Causando {roxo}{dano}{branco} de Dano e Gastando {verde1}700{branco} de Mana!")
                print()
                gasto = 700
                mana = mana - gasto
                print(f"{verde1}Mana Restante: {mana}{branco}")
                print()
                print("-"*150)

            elif mg >= 30 and mana >= 550 and magia == "1":
                dano = nível * 25
                bosshp = bosshp - dano
                print()
                print("Você Lançou uma Bola de Fogo nele!")
                print(f"Causando {roxo}{dano}{branco} de Dano e Gastando {verde1}550{branco} de Mana!")
                print()
                gasto = 550
                mana = mana - gasto
                print(f"{verde1}Mana Restante: {mana}{branco}")
                print()
                print("-"*150)

            elif mg >= 1 and mana >= 400 and magia == "3":
                dano = nível * 10
                bosshp = bosshp - dano
                print()
                print(f"Você Congelou ele, mas não foi tão Eficaz, Afinal, Ele é um {roxo}Dragão{branco} de Fogo!!!")
                print(f"Mas Causou {roxo}{dano}{branco} de Dano e Gastou {verde1}400{branco} de Mana!")
                print()
                gasto = 400
                mana = mana - gasto
                print(f"{verde1}Mana Restante: {mana}{branco}")
                print()
                print("-"*150)

            else:
                print()
                print(f"{verde1}Mana{branco} Insuficiente!")
                print()
                print("-"*150)

        elif sorte >=51 and mana <= 199:
            print()
            print(f"{verde1}Mana{branco} Insuficiente!")
            print()
            print("-"*150)

    elif luta == "3" and classe != "mago":
        print()
        print("Apenas Magos podem usar Magias!")
        print()
        print("-"*150)

# Luta = Fugir

    elif luta == "2":
        sorte = random.randint(1, 100)
            
        if sorte <= 60:
            print()
            print(f"sua Tentativa de Fuga Falhou o {roxo}Dragão{branco}te Matou!!!")
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

# Luta = Bomba

    elif luta == "4":
        sorte = random.randint(1, 100)
            
        if sorte <= 30:
            import time

            bomba = 5
            while bomba > 0:
                print(bomba)
                bomba -= 1
                time.sleep(0.3)
            print("BOOM!!!")
            print("Você Errou a Bomba!")
            print("-"*150)

                
        elif sorte >=31:

            bomb = random.randint(1, 100)

            if bomb <= 40:
                import time

                bomba = 5
                while bomba > 0:
                    print(bomba)
                    bomba -= 1
                    time.sleep(0.3)
                dano = nível * 50
                bosshp = bosshp - dano
                print("BOOM!!!")
                print(f"Na hora que o {roxo}Dragão {branco}Abriu a Boca, Você lançou a Bomba na Garganta Dele!")
                print(f"Causando {roxo}{dano}{branco} de Dano!")

                print("-"*150)
                    
            elif bomb >= 41:
                import time

                bomba = 5
                while bomba > 0:
                    print(bomba)
                    bomba -= 1
                    time.sleep(0.3)
                dano = nível * 30
                bosshp = bosshp - dano
                print("BOOM!!!")
                print(f"Você lançou a Bomba no {roxo}Dragão{branco}, Machucou Muito!")
                print(f"Causando {roxo}{dano}{branco} de Dano!")
                print("-"*150)

# Ação Inválida

        else:
            print()
            print(f"Ação Inválida! Você demorou Para Responder e o {roxo}Dragão {branco}Obliterou a Vila!")
            print(f"{vermelho}GAME OVER!{branco}")
            print()
            print("-"*150)
            break

# Vitória
                    
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

    print(f"Seu saldo Agora é:{amarelo}", round(reais, 2), "Reais")
    print()
    print(f"{branco}-"*150)