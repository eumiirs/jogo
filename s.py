import time
import sys
import random
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def animacao_slot():
    frutas = ["🍒", "🍋", "🍉"]
    ganhou = random.random() < 0.1  # 10% de chance de ganhar

    for i in range(15):
        linha = " | ".join(random.choice(frutas) for _ in range(3))
        sys.stdout.write("\r🎰 Girando... " + linha + " ")
        sys.stdout.flush()
        time.sleep(0.1)

    if ganhou:
        # Vitória real (três frutas iguais)
        fruta = random.choice(frutas)
        resultado = f"{fruta} | {fruta} | {fruta}"
        sys.stdout.write(f"\r🎰 Resultado final: {resultado}   \n")
        sys.stdout.flush()
        print("🏆🎉 PARABÉNS!!! DESSA VEZ VOCÊ GANHOU!!! 🎉🏆")
        return True
    else:
        # Perdeu
        linha = " | ".join(random.choice(frutas) for _ in range(3))
        sys.stdout.write(f"\r🎰 Resultado final: {linha}   \n")
        sys.stdout.flush()
        print("😅 Que pena... você perdeu dessa vez!")
        return False

def main():
    saldo = int(input("Informe seu saldo inicial (R$): "))

    rodada = 1
    while True:
        while saldo > 0:
            limpar_tela()
            print("=== Jogo do Caça-Níquel ===\n")
            print(f"Rodada: {rodada}")
            print(f"Saldo atual: R$ {saldo}\n")

            try:
                aposta = int(input("Quanto deseja apostar? R$ "))
            except ValueError:
                print("Aposta inválida!")
                time.sleep(1)
                continue

            if aposta > saldo or aposta <= 0:
                print("Aposta inválida!")
                time.sleep(1)
                continue

            print("\nPuxando a alavanca 🎰...")
            time.sleep(1)
            # chama a animação
            ganhou = animacao_slot()  
            if ganhou:
                saldo += aposta * 2
                 # exemplo: ganha o dobro da aposta
                print(f"💰 Você ganhou R$ {aposta*2}! Saldo atual: R$ {saldo}")
            else:
                saldo -= aposta
                print(f"💸 Você perdeu R$ {aposta}! Saldo restante: R$ {saldo}")

            rodada += 1
            time.sleep(2)

        # Quando o saldo chega a zero
        limpar_tela()
        print("💀 Seu saldo chegou a ZERO. 💀\n")
        print("Deseja recarregar ou sair do jogo?")
        print("1 - Recarregar saldo")
        print("2 - Sair do jogo")

        escolha = input("Escolha 1 ou 2: ")
        if escolha == "1":
            try:
                recarga = int(input("Informe o valor para recarregar: R$ "))
                if recarga > 0:
                    saldo += recarga
                    print(f"✅ Saldo recarregado! Novo saldo: R$ {saldo}")
                    time.sleep(2)
                else:
                    print("Valor inválido!")
                    time.sleep(1)
            except ValueError:
                print("Valor inválido!")
                time.sleep(1)
        elif escolha == "2":
            print("Saindo do jogo... Até a próxima! 👋")
            break
        else:
            print("Opção inválida!")
            time.sleep(1)

if __name__ == "__main__":
    main()
