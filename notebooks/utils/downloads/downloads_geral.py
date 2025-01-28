import geopandas as gpd
from os.path import join, exists
from os import makedirs
from logging import (
    Logger,
    getLogger,
)
import requests
from time import sleep
import shutil

def read_zip_file(name_cache:str, logger:Logger=getLogger()):
                gdf= gpd.read_file(
                    f'zip://{name_cache}'
                )
                        
                logger.info("Arquivo lido com sucesso!")


def save_zip_file(url:str, name_cache:str, logger:Logger=getLogger()):
    response = requests.get(url)
    if response.status_code==200:
        with open(name_cache, 'wb') as f:
            f.write(response.content)
            #f.close
        logger.info(
            f'Arquivo baixado com sucesso!{name_cache}'
        )

def download_to_temporary_cache(
        url:str, 
        name_cache:str,
        file_path:str,
        max_retries:int=5, 
        logger:Logger=getLogger()
):
    
    for i in range(max_retries):
        logger.info(f"""
            Tentativa ({i + 1}/{max_retries})""")
        try:
            save_zip_file(url, name_cache)
            shutil.copy(name_cache, file_path)
            
            if exists(name_cache):
                try:
                    read_zip_file(name_cache)
                    break
                except Exception as e:
                    logger.error(f"Erro ao salvar o arquivo: {e}")
        
        except requests.exceptions.RequestException as e:
            logger.error(f"Erro na requisição: {e}")
        except Exception as e:
            logger.error(f"Erro ao processar o arquivo: {e}")
                
        if i < max_retries -1:
                logger.warning(
                    f"Tentando novamente em 5 segundos..."
                )
                sleep(5)
        else:
            logger.warning(
                    """Limite de tentativas atingido.
                    Tentando ler arquivo em cache"""
                )
            
def _prepare_cache(url:str, name_feature:str, logger:Logger=getLogger()) -> gpd.GeoDataFrame:

    file_dir = join('data', 'cache')
    file_path = join(file_dir, name_feature + '.zip')
    gdf={}
    temporary_cache = join(file_dir,'temporary_cache')
    name_cache = join(temporary_cache, name_feature + '.zip')
    
    makedirs(file_dir, exist_ok=True)
    makedirs(temporary_cache, exist_ok=True)

    download_to_temporary_cache(url, name_cache, file_path)
    
    
    gdf= gpd.read_file(
        f'zip://{file_path}'
    )
    logger.info("Leitura do arquivo concluída.")
    return gdf