from fun_centralizador import print_c

def design(nivel_escolhido, numero_de_erros):
    """
    printa o desenho da forca de acordo com o numero de erros e o nivel de dificuldade
    """

    #ESTÁGIOS
    e00 = '  __________________   \n ||                    \n ||                    \n ||                    \n ||                    \n ||                    \n ||                    \n ||                    \n ||                    \n ||                    \n_||_                   '
    e01 = '  __________________   \n ||                |   \n ||                    \n ||                    \n ||                    \n ||                    \n ||                    \n ||                    \n ||                    \n ||                    \n_||_                   '
    e02 = '  __________________   \n ||                |   \n ||                |   \n ||                    \n ||                    \n ||                    \n ||                    \n ||                    \n ||                    \n ||                    \n_||_                   '
    e03 = '  __________________   \n ||                |   \n ||                |   \n ||                |   \n ||                    \n ||                    \n ||                    \n ||                    \n ||                    \n ||                    \n_||_                   '
    e04 = '  __________________   \n ||                |   \n ||                |   \n ||                |   \n ||                |   \n ||                    \n ||                    \n ||                    \n ||                    \n ||                    \n_||_                   '
    e05 = '  __________________   \n ||                |   \n ||                |   \n ||                |   \n ||                |   \n ||                O   \n ||                    \n ||                    \n ||                    \n ||                    \n_||_                   '
    e06 = '  __________________   \n ||                |   \n ||                |   \n ||                |   \n ||                |   \n ||                O/  \n ||                    \n ||                    \n ||                    \n ||                    \n_||_                   '
    e07 = '  __________________   \n ||                |   \n ||                |   \n ||                |   \n ||                |   \n ||               \O/  \n ||                    \n ||                    \n ||                    \n ||                    \n_||_                   '
    e08 = '  __________________   \n ||                |   \n ||                |   \n ||                |   \n ||                |   \n ||               \O/  \n ||                |   \n ||                    \n ||                    \n ||                    \n_||_                   '
    e09 = '  __________________   \n ||                |   \n ||                |   \n ||                |   \n ||                |   \n ||               \O/  \n ||                |   \n ||                 \  \n ||                    \n ||                    \n_||_                   '
    e10 = '  __________________   \n ||                |   \n ||                |   \n ||                |   \n ||                |   \n ||               \O/  \n ||                |   \n ||               / \  \n ||                    \n ||                    \n_||_                   '
    
    lista_de_design = [e00, e01, e02, e03, e04, e05, e06, e07, e08, e09, e10]
    
    #COMANDOS
    if nivel_escolhido == 1: #VÃO SER PERMITIDOS 10 ERROS
        print_c(lista_de_design[numero_de_erros])

    elif nivel_escolhido == 2: #VÃO SER PERMITIDOS 5 ERROS
        print_c(lista_de_design[numero_de_erros*2])

    elif nivel_escolhido == 3: #VÃO SER PERMITIDOS 3 ERROS
        lista_reserva = [e00, e04, e07, e10]
        print_c(lista_reserva[numero_de_erros])

    return None