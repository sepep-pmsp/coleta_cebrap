import os
import geopandas as gpd
from geopandas import GeoSeries, GeoDataFrame
from os import makedirs
from os.path import join, exists
import pyproj

def save_parquet(
    gdf:gpd.GeoDataFrame,
    fname:str,
    project_path:str,
    data_subpath:str='',
    
    **kwargs
) -> None:

    
    data_path = os.path.join(project_path, 'data', 'assets')


    
    full_path = join(data_path, data_subpath)
    if not exists(full_path):
        makedirs(full_path)

    gdf.to_parquet(
        join(full_path, f'{fname}.parquet'),
        index=False
    )