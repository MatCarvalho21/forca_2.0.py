def tracinhos(palavra_formatada):
    """
    recebe uma string e retorna uma string de underlines de mesmo tamanho
    """
    lista_de_tracinhos = list()
    for cada_caractere in palavra_formatada:
        if cada_caractere == " " or cada_caractere == "-":
            lista_de_tracinhos.append(f"{cada_caractere}")
        else:
            lista_de_tracinhos.append("_")

    palavra_tracinho = "".join(lista_de_tracinhos)
    return palavra_tracinho