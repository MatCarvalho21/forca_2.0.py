from fun_limpador import fun_limpador
from fun_lista_de_palavras import fun_lista_de_palavras
from fun_centralizador import print_c

def fun_escolha_palavra(escolha_do_modo):
    """
    vai escolher qual palavra será utilizada no jogo
    """
    fun_limpador()

    if escolha_do_modo == 1:
        print_c("FORCA.py 2.0")
        print()
        palavra_escolhida = input("Digite a seguir a sua palavra: ")

    elif escolha_do_modo == 2:
        while True:
            print_c("FORCA,py 2.0")
            print()
            print("Vamos escolher o tema do seu jogo. Selecione uma das opções abaixo: \n")
            print("1 - Times da NBA")
            print("2 - Times da NFL")
            print("3 - Países\n")
            tema_escolhido = input("Qual a sua escolha, jogador(a)? ")
            if tema_escolhido == "1" or tema_escolhido == "2" or tema_escolhido == "3":
                break
            else:
                fun_limpador()
                print_c("INSIRA UM VALOR VÁLIDO!")
                print()
                continue
        
        palavra_escolhida = fun_lista_de_palavras(tema_escolhido)

    return palavra_escolhida