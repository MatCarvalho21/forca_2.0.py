from fun_limpador import fun_limpador
from fun_centralizador import print_c

def fun_dificuldades():
    """
    vai receber a dificuldade escolhida pelo usuário
    """
    fun_limpador()
    while True:
        print_c("FORCA.py 2.0")
        print()
        print("Vamos começar escolhendo o número de erros permitidos. Abaixo estão suas opções: \n")
        print("1 - Iniciante (10 erros)")
        print("2 - Experiente (5 erros)")
        print("3 - Dono do Jogo (3 erros)")
        escolha_de_dificuldade = input("\nQual a sua escolha, jogador(a)? ")

        if escolha_de_dificuldade == "1" or escolha_de_dificuldade == "2" or escolha_de_dificuldade == "3":
            break

        else:
            fun_limpador()
            print_c("INSIRA UM VALOR VÁLIDO!")
            print()
            continue

    return int(escolha_de_dificuldade)