import os
import sys

def diretorio_teste():
    diretorio_atual = os.getcwd()
    diretorio_final = os.path.join(
        diretorio_atual,
        '..',
        '..',
        '..',
        '..'
    )
    
    root_path = os.path.abspath(
        diretorio_final
    )

    sys.path.append(root_path)
    print(root_path)
    
    return str(root_path)