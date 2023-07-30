import shutil

def print_c(mensagem):
    """
    centraliza as mensagens no terminal
    """
    print(mensagem.center(shutil.get_terminal_size().columns))