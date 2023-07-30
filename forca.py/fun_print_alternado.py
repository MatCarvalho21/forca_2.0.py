def print_a(palavra_qualquer):
    """
    vai receber uma string e printá-la inserindo um espaço em branco entre os caracteres
    """
    lista_de_letras = list()
    for cada_letra in palavra_qualquer:
        lista_de_letras.append(cada_letra)

    palavra_qualquer_alternada = " ".join(lista_de_letras)

    print(palavra_qualquer_alternada)