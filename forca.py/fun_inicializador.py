from fun_limpador import fun_limpador
from fun_centralizador import print_c

def fun_inicializador():
    """
    vai ser responsável por iniciar o jogo
    """
    while True:
        fun_limpador()
        print_c("FORCA.py 2.0")
        print()
        comando = input("Bem vindo ao jogo da forca! Você já sabe como funciona [s/n]? ")
        if comando.lower() == "n":
            fun_limpador()
            print_c("FORCA.py 2.0")
            print()
            print("Sugiro que você encerre o jogo e visite nosso repositório no Github.")
            print("Você vai encontrar todas as instruções no lá!")
            break
        elif comando.lower() == "s":
            fun_limpador()
            break
        else:
            continue