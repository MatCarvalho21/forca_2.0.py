from fun_inicializador import fun_inicializador
from fun_jogadores import fun_jogadores
from fun_dificuldades import fun_dificuldades
from fun_escolha_palavra import fun_escolha_palavra
from fun_normalizador import fun_normalizador
from fun_jogadas import forca

while True:
    #VAI INICIAR O JOGO
    fun_inicializador() 

    #VAI DEFINIR A ESCOLHA DO MODO DE JOGO
    escolha_do_modo = fun_jogadores()

    #VAI DEFINIR A DIFICULDADE DO JOGO
    escolha_da_dificuldade = fun_dificuldades()

    #VAI DEFINIR A ESCOLHA DA PALAVRA
    palavra_escolhida = fun_escolha_palavra(escolha_do_modo)

    #VAI NORMALIZAR A PALAVRA ESCOLHIDA
    palavra_normalizada = fun_normalizador(palavra_escolhida)

    #VAI RODAR O JOGO EM SI
    forca(escolha_da_dificuldade, palavra_normalizada)

    comando = input("Você deseja jogar novamente [s/n]? ")
    if comando.upper() == "S":
        continue
    else:
        break
    