import sys
import os
diretorio_atual = os.getcwd()
sys.path.append(os.path.join(
    diretorio_atual, 
    '..',
    '..'
))

from utils import diretorio

def definir_diretorio():
    '''
    Esta função faz com que os notebooks definam o path para a pasta jupyter.
    '''
    diretorio_atual = os.getcwd()
    diretorio_final = diretorio(diretorio_atual)

    sys.path.append(os.path.join(diretorio_final))

    return str(diretorio_final)



