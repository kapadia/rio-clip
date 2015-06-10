

import rasterio as rio


__version__ = '0.0.1'


def crop(srcpath, tarpath, dstpath):
    """
    Crop the target image to the extent of the source image.
    """
    
    with rio.drivers():
        
        with rio.open(srcpath, 'r') as src:
            source_metadata = src.meta
            source_bounds = src.bounds
        
        with rio.open(tarpath, 'r') as tar:
            target_metadata = tar.meta
            
            window = tar.window(*source_bounds)
            count = target_metadata["count"]
            
            with rio.open(dstpath, "w", **source_metadata) as dst:
                
                for bidx in range(1, count + 1):
                    band = tar.read(bidx, window=window)
                    dst.write_band(bidx, band)