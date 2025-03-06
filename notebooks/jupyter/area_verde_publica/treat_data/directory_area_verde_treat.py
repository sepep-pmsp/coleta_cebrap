import sys
import os
diretorio_atual = os.getcwd()
sys.path.append(os.path.join(
    diretorio_atual, 
    '..',
    '..'
))

def get_data_diretorio(project_path:str)->str:
    
    data_path = os.path.join(
        project_path,
        '..',
        '..',
        'data'
    )
    return str(data_path)

    

def diretorio(diretorio_atual:str)-> str:
    diretorio = os.path.abspath(
        os.path.join(
            diretorio_atual,
            '..',
            '..',
        )
    )
    return diretorio

def definir_diretorio():
    '''
    Esta função faz com que os notebooks definam o path para a pasta jupyter.
    '''
    diretorio_atual = os.getcwd()
    diretorio_final = diretorio(diretorio_atual)

    sys.path.append(os.path.join(diretorio_final))

    return str(diretorio_final)