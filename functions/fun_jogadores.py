from fun_limpador import fun_limpador

def fun_jogadores():
    while True:
        print("Ótimo! Vamos começar escolhendo o modo de jogo. Abaixo estão suas opções:")
        print("\n1 - Inserir sua própria palavra ou frase.")
        print("2 - Usar uma das nossas base de dados.")
        comando = input("\nQual a sua escolha, jogador(a)? ")
        if comando == "1" or comando== "2":
            break
        else:
            fun_limpador()
            print("Selecione, por favor, um valor válido.\n")
    return int(comando)