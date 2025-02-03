import geopandas as gpd
from geopandas import GeoSeries, GeoDataFrame
from os import makedirs
from os.path import join, exists
import pyproj

def save_csv_parquet(
    gdf:gpd.GeoDataFrame,
    data_path:str, 
    fname:str,
    data_subpath:str=None,
    **kwargs
) -> None:
    
    full_path = join(data_path, data_subpath)
    if not exists(full_path):
        makedirs(full_path)

    
    gdf.to_csv(
        join(full_path, f'{fname}.csv'),
        index=False, 
        encoding='utf-8'
    )

    gdf.to_parquet(
        join(full_path, f'{fname}.parquet'),
        index=False
    )