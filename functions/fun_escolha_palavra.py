from fun_limpador import fun_limpador
from fun_lista_de_palavras import fun_lista_de_palavras

def fun_escolha_palavra(escolha_do_modo):
    fun_limpador()

    if escolha_do_modo == 1:
        palavra_escolhida = input("Digite a seguir a sua palavra: ")

    elif escolha_do_modo == 2:
        while True:
            print("Vamos escolher o tema do seu jogo. Selecione uma das opções abaixo: \n")
            print("1 - Times da NBA\n")
            tema_escolhido = input("\nQual a sua escolha, jogador(a)? ")
            if tema_escolhido == "1":
                break
            else:
                fun_limpador()
                continue
        
        palavra_escolhida = fun_lista_de_palavras(tema_escolhido)

    return palavra_escolhida