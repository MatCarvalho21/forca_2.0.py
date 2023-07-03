import unidecode

def fun_normalizador(palavra_escolhida):
    palavra_modificada = unidecode(palavra_escolhida.upper().strip())
    return palavra_modificada