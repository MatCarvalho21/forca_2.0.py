import unidecode

def fun_normalizador(palavra_escolhida):
    """
    vai receber a palavra do usuario e padronizá-la
    """
    palavra_modificada = unidecode.unidecode(palavra_escolhida.upper().strip())
    return palavra_modificada