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

from utils import (
    save_parquet_excel,
    get_data_diretorio
)
from typing import Optional


def read_zip_file(name_cache:str, logger:Logger=getLogger()):
    
    print('helloo')
    print(name_cache)

    gdf= gpd.read_file(
        f'zip://{name_cache}'
    )

            
    logger.info("Arquivo lido com sucesso!")

    return gdf

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
            
def _prepare_cache_single(
    url:str, 
    name_feature:str, 
    cache_path:str,
    logger:Logger=getLogger()
) -> gpd.GeoDataFrame:

    file_dir = cache_path
    file_path = join(file_dir, name_feature + '.zip')
    gdf={}
    temporary_cache = join(cache_path,'temporary_cache')
    name_cache = join(temporary_cache, name_feature + '.zip')
    
    makedirs(cache_path, exist_ok=True)
    makedirs(temporary_cache, exist_ok=True)

    download_to_temporary_cache(url, name_cache, file_path)
    
    
    gdf= read_zip_file(file_path)
    logger.info("Leitura do arquivo concluída.")
    return gdf

def _create_paginated_url(url:str, max_features:int, start_index:str, sort_by:Optional[str]=None)->str:

    url = f"{url}&maxFeatures={max_features}&startIndex={start_index}"

    if sort_by is not None:
        url = url + f'&sortBy={sort_by}'

    return url

def _prepare_cache_paginated(url:str, name_feature:str, cache_path:str, logger:Logger=getLogger(), 
                             max_features=2000, sort_by:Optional[str]=None) -> gpd.GeoDataFrame:

    geodfs = []
    
    start_index=0
    page=1
    
    while True:
        url_req = _create_paginated_url(url, max_features, start_index, sort_by=sort_by)
        name_feature_req = f"{name_feature}_pg{page}"
        print(url_req)
        print(name_feature_req)
        gdf = _prepare_cache_single(
            url_req, 
            name_feature_req, 
            cache_path, 
            logger
        )
        print(gdf.shape)
        if len(gdf)<1:
            break
        geodfs.append(gdf)
        start_index+=max_features
        page+=1
    
    df = pd.concat(geodfs)

    save_parquet_excel(df, f'{name_feature}_concat', cache_path)
    
    
    
    return gpd.GeoDataFrame(df)


def _prepare_cache(
    url:str, 
    name_feature:str, 
    cache_path:str, 
    paginate=False,
    logger:Logger=getLogger(), 
    max_features=2000,
    sort_by:Optional[str]=None
) -> gpd.GeoDataFrame:

    #early return para quando nao faz sentido paginar
    if not paginate:
        return _prepare_cache_single(
            url, 
            name_feature, 
            cache_path, 
            logger
        )

    return _prepare_cache_paginated(
        url, 
        name_feature, 
        cache_path,
        logger,
        max_features,
        sort_by=sort_by
    )
   




    