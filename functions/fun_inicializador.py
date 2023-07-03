from fun_limpador import fun_limpador

def fun_inicializador():
    while True:
        fun_limpador()
        comando = input("Bem vindo ao jogo da forca! Você já sabe como funciona? [y/n] ")
        if comando == "n":
            fun_limpador()
            print("Sugiro que você encerre o jogo e visite nosso repositório no Github.")
            print("Você vai encontrar todas as instruções no lá!")
        elif comando == "y":
            fun_limpador()
            break
        else:
            continue