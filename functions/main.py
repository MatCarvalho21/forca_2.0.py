from fun_inicializador import fun_inicializador
from fun_jogadores import fun_jogadores
from fun_dificuldades import fun_dificuldades
from fun_escolha_palavra import fun_escolha_palavra

#VAI INICIAR O JOGO
fun_inicializador() 

#VAI DEFINIR A ESCOLHA DO MODO DE JOGO
escolha_do_modo = fun_jogadores()

#VAI DEFINIR A DIFICULDADE DO JOGO
escolha_da_dificuldade = fun_dificuldades()

#VAI DEFINIR A ESCOLHA DA PALAVRA
palavra_escolhida = fun_escolha_palavra(escolha_do_modo)