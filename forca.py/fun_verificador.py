from unidecode import unidecode

def verificador_letra(palpite, palavra_em_tracinhos, palavra_normalizada):
    """
    verifica se o palpite está correto e retorna a palavra_tracinho modificada ou não
    """
    lista_elementos = list()
    for cada_elemento in palavra_normalizada:
        lista_elementos.append(cada_elemento)

    lista_tracinho = list()
    for cada_elemento in palavra_em_tracinhos:
        lista_tracinho.append(cada_elemento)

    for indice in range(0, len(lista_tracinho), 1):
        if lista_elementos[indice] == palpite:
            lista_tracinho[indice] = palpite
        else:
            pass
    
    return "".join(lista_tracinho)

def verificador_palavra(palpite, palavra_normalizada):
    """
    verifica se o palpite é igual à palavra e retorna um booleano
    """
    if unidecode(palpite.strip().upper()) == palavra_normalizada:
        return True
    else:
        return False