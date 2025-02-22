import geopandas as gpd
from logging import (
    Logger,
    getLogger,
)
import os

def diretorio(diretorio_atual:str)-> str:
    diretorio = os.path.abspath(
        os.path.join(
            diretorio_atual,
            '..',
            '..',
        )
    )
    return diretorio

def get_data_diretorio(project_path:str)->str:
    
    data_path = os.path.join(
        project_path,
        '..',
        '..',
        'data'
    )
    
    
    return str(data_path)

def check_crs(
    gdf, 
    logger:Logger=getLogger()
) -> gpd.GeoDataFrame():

    for i in range(2):
        if gdf.crs == ('EPSG:31983'):
            logger.info(f"""O crs do gdf está correto!
            {gdf.crs}""")
            return gdf
            break

        else:
            logger.warning(
                f"O crs do gdf não está correto:{gdf.crs}"
            )
            logger.info("Tentando converter!")
            gdf=gdf.to_crs('EPSG:31983')
            logger.info(f"Novo crs: {gdf.crs}")
            return gdf


    
    