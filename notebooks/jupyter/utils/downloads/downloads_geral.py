import sys
import os
diretorio_atual = os.getcwd()
sys.path.append(os.path.join(diretorio_atual, '..', '..'))

import geopandas as gpd
import pandas as pd
from os.path import join, exists, abspath
from os import makedirs
from logging import (
    Logger,
    getLogger,
)
import requests
from time import sleep
import shutil

from utils import save_parquet_excel

def read_zip_file(name_cache:str, logger:Logger=getLogger()):
                gdf= gpd.read_file(
                    f'zip:///{name_cache}'
                )
                        
                logger.info("Arquivo lido com sucesso!")


def save_zip_file(
    url:str, 
    name_cache:str, 
    logger:Logger=getLogger()
):
    response = requests.get(url)
    if response.status_code==200:
        with open(name_cache, 'wb') as f:
            f.write(response.content)
            #f.close()
        logger.info(
            f'Arquivo baixado com sucesso!{name_cache}'
        )
    else:
        logger.error(
            f'''Falha no download. Status Code: {
                response.status_code
            }. URL: {url}'''
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
            name_cache = abspath(name_cache)
            save_zip_file(url, name_cache)
            shutil.copy(name_cache, file_path)
            assert exists(name_cache), f"Arquivo {name_cache} não encontrado"
            break
        
        except requests.exceptions.RequestException as e:
            logger.error(f"Erro na requisição: {e}")
        except Exception as e:
            logger.error(f"Erro ao processar o arquivo: {e}")
                
        if i < max_retries -1:
                logger.warning(
                    f"Tentando novamente em {i} segundos..."
                )
                sleep(5)
        else:
            logger.warning(
                    """Limite de tentativas atingido.
                    Tentando ler arquivo em cache"""
                )
            
def _prepare_cache_single(url:str, name_feature:str, logger:Logger=getLogger()) -> gpd.GeoDataFrame:

    project_path = os.path.abspath(os.path.join(os.getcwd(), '..', '..'))
    data_path = os.path.join(project_path, 'data')

    file_dir = join(data_path, 'cache')
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

def _create_paginated_url(url:str, max_features:int, start_index:str)->str:

    return f"{url}&maxFeatures={max_features}&startIndex={start_index}"

def _prepare_cache_paginated(url:str, name_feature:str, logger:Logger=getLogger(), max_features=2000) -> gpd.GeoDataFrame:

    geodfs = []
    
    start_index=0
    page=1
    
    while True:
        url_req = _create_paginated_url(url, max_features, start_index)
        name_feature_req = f"{name_feature}_pg{page}"
        print(url_req)
        print(name_feature_req)
        gdf = _prepare_cache_single(url_req, name_feature_req, logger)
        print(gdf.shape)
        if len(gdf)<1:
            break
        geodfs.append(gdf)
        start_index+=max_features
        page+=1
    
    df = pd.concat(geodfs)

    save_parquet(df, f'{name_feature}_concat', 'cache')
    
    
    
    return gpd.GeoDataFrame(df)


def _prepare_cache(url:str, name_feature:str, paginate=False, logger:Logger=getLogger(), max_features=2000) -> gpd.GeoDataFrame:

    #early return para quando nao faz sentido paginar
    if not paginate:
        return _prepare_cache_single(url, name_feature, logger)

    return _prepare_cache_paginated(url, name_feature, logger, max_features)
   




    