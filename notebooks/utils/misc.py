import geopandas as gpd
from logging import (
    Logger,
    getLogger,
)

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