from fun_limpador import fun_limpador
from fun_centralizador import print_c

def fun_jogadores():
    """
    descobre qual tipo de palavra será utilizado pelo usuário
    """
    while True:
        print_c("FORCA.py 2.0")
        print()
        print("Ótimo! Vamos começar escolhendo o modo de jogo. Abaixo estão suas opções:")
        print("\n1 - Inserir sua própria palavra ou frase.")
        print("2 - Usar uma das nossas base de dados.")
        comando = input("\nQual a sua escolha, jogador(a)? ")
        if comando == "1" or comando== "2":
            break
        else:
            fun_limpador()
            print_c("INSIRA UM VALOR VÁLIDO!")
            print()
            continue
    return int(comando)