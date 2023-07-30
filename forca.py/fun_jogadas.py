from fun_design import design
from fun_centralizador import print_c
from fun_limpador import fun_limpador
from fun_tracinhos import tracinhos
from fun_verificador import verificador_letra, verificador_palavra
from fun_print_alternado import print_a


def forca(nivel_de_dificulade, palavra_normalizada):
    """
    cordena todo o corpo das jogadas
    """
    numero_de_erros = 0
    palavra_em_tracinhos = tracinhos(palavra_normalizada)

    if nivel_de_dificulade == 1:
        while True:
            fun_limpador()
            print_c("FORCA.py 2.0")
            print()

            print_c(f"Número de Erros: {numero_de_erros}")
            print()

            print_c("--> Chute apenas uma letra de cada vez, para chutar a palavra inteira, apenas tecle enter! <--")
            print()

            design(nivel_de_dificulade, numero_de_erros)
            print()

            print_a(palavra_em_tracinhos)
            print()

            #ULTIMA CHANCE
            if numero_de_erros == 10:
                print("Você estourou o limite de erros. Você tem mais uma chance para tentar adivinhar!")
                print()
                palpite3 = input("Qual o seu palpite (tem que ser a palavra inteira)? ")
                confirmacao = verificador_palavra(palpite3, palavra_normalizada)
                if confirmacao == True:
                    palavra_em_tracinhos = palavra_normalizada
                else:
                    numero_de_erros += 1
            
            #VITÓRIA
            if palavra_em_tracinhos == palavra_normalizada:
                fun_limpador()
                print_c("FORCA.py 2.0")
                print()
                print_c(f"VOCÊ VENCEU! A PALAVRA ERA {palavra_normalizada}.")
                print()
                break
            
            #DERROTA
            if numero_de_erros == 11:
                fun_limpador()
                print_c("FORCA.py 2.0")
                print()
                print_c(f"VOCÊ PERDEU! A PALAVRA ERA {palavra_normalizada}.")
                print()
                break
            
            #PALPITE PRINCIPAL
            palpite = input("Qual o seu palpite? ").upper().strip()

            #PALPITE PALAVRA
            if palpite == "":
                print()
                palpite2 = input("Então você já descobriu?! Qual o seu plapite? ")
                confirmacao = verificador_palavra(palpite2, palavra_normalizada)

                if confirmacao == True:
                    palavra_em_tracinhos = palavra_normalizada
                else:
                    numero_de_erros += 1

                continue
            
            #CHUTE INVALIDO
            elif len(palpite) > 1:
                numero_de_erros += 1
                continue
            
            #CHUTE CORRETO
            elif palpite in palavra_normalizada:
                palavra_em_tracinhos = verificador_letra(palpite, palavra_em_tracinhos, palavra_normalizada)

            #CHUTE ERRADO
            else:
                numero_de_erros += 1
                continue

    elif nivel_de_dificulade == 2:
        while True:
            fun_limpador()
            print_c("FORCA.py 2.0")
            print()

            print_c(f"Número de Erros: {numero_de_erros}")
            print()

            print_c("--> Chute apenas uma letra de cada vez, para chutar a palavra inteira, apenas tecle enter! <--")
            print()

            design(nivel_de_dificulade, numero_de_erros)
            print()

            print_a(palavra_em_tracinhos)
            print()

            #ULTIMA CHANCE
            if numero_de_erros == 5:
                print("Você estourou o limite de erros. Você tem mais uma chance para tentar adivinhar!")
                print()
                palpite3 = input("Qual o seu palpite (tem que ser a palavra inteira)? ")
                confirmacao = verificador_palavra(palpite3, palavra_normalizada)
                if confirmacao == True:
                    palavra_em_tracinhos = palavra_normalizada
                else:
                    numero_de_erros += 1
            
            #VITÓRIA
            if palavra_em_tracinhos == palavra_normalizada:
                fun_limpador()
                print_c("FORCA.py 2.0")
                print()
                print_c(f"VOCÊ VENCEU! A PALAVRA ERA {palavra_normalizada}.")
                print()
                break
            
            #DERROTA
            if numero_de_erros == 6:
                fun_limpador()
                print_c("FORCA.py 2.0")
                print()
                print_c(f"VOCÊ PERDEU! A PALAVRA ERA {palavra_normalizada}.")
                print()
                break
            
            #PALPITE PRINCIPAL
            palpite = input("Qual o seu palpite? ").upper().strip()

            #PALPITE PALAVRA
            if palpite == "":
                print()
                palpite2 = input("Então você já descobriu?! Qual o seu plapite? ")
                confirmacao = verificador_palavra(palpite2, palavra_normalizada)

                if confirmacao == True:
                    palavra_em_tracinhos = palavra_normalizada
                else:
                    numero_de_erros += 1

                continue
            
            #CHUTE INVALIDO
            elif len(palpite) > 1:
                numero_de_erros += 1
                continue
            
            #CHUTE CORRETO
            elif palpite in palavra_normalizada:
                palavra_em_tracinhos = verificador_letra(palpite, palavra_em_tracinhos, palavra_normalizada)

            #CHUTE ERRADO
            else:
                numero_de_erros += 1
                continue
    
    else:
        while True:
            fun_limpador()
            print_c("FORCA.py 2.0")
            print()

            print_c(f"Número de Erros: {numero_de_erros}")
            print()

            print_c("--> Chute apenas uma letra de cada vez, para chutar a palavra inteira, apenas tecle enter! <--")
            print()

            design(nivel_de_dificulade, numero_de_erros)
            print()

            print_a(palavra_em_tracinhos)
            print()

            #ULTIMA CHANCE
            if numero_de_erros == 3:
                print("Você estourou o limite de erros. Você tem mais uma chance para tentar adivinhar!")
                print()
                palpite3 = input("Qual o seu palpite (tem que ser a palavra inteira)? ")
                confirmacao = verificador_palavra(palpite3, palavra_normalizada)
                if confirmacao == True:
                    palavra_em_tracinhos = palavra_normalizada
                else:
                    numero_de_erros += 1
            
            #VITÓRIA
            if palavra_em_tracinhos == palavra_normalizada:
                fun_limpador()
                print_c("FORCA.py 2.0")
                print()
                print_c(f"VOCÊ VENCEU! A PALAVRA ERA {palavra_normalizada}.")
                print()
                break
            
            #DERROTA
            if numero_de_erros == 4:
                fun_limpador()
                print_c("FORCA.py 2.0")
                print()
                print_c(f"VOCÊ PERDEU! A PALAVRA ERA {palavra_normalizada}.")
                print()
                break
            
            #PALPITE PRINCIPAL
            palpite = input("Qual o seu palpite? ").upper().strip()

            #PALPITE PALAVRA
            if palpite == "":
                print()
                palpite2 = input("Então você já descobriu?! Qual o seu plapite? ")
                confirmacao = verificador_palavra(palpite2, palavra_normalizada)

                if confirmacao == True:
                    palavra_em_tracinhos = palavra_normalizada
                else:
                    numero_de_erros += 1

                continue
            
            #CHUTE INVALIDO
            elif len(palpite) > 1:
                numero_de_erros += 1
                continue
            
            #CHUTE CORRETO
            elif palpite in palavra_normalizada:
                palavra_em_tracinhos = verificador_letra(palpite, palavra_em_tracinhos, palavra_normalizada)

            #CHUTE ERRADO
            else:
                numero_de_erros += 1
                continue