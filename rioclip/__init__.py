
import rasterio as rio
import rasterio.warp
from rasterio.coords import BoundingBox
from affine import Affine


__version__ = '0.0.1'


def clip(srcpath, tarpath, dstpath):
    """
    Clip the target image to the extent of the source image.
    """
    
    with rio.drivers():
        
        with rio.open(srcpath, 'r') as src:
            srcmeta = src.meta.copy()
            srcbounds = src.bounds
        
        with rio.open(tarpath, 'r') as tar:
            tarmeta = tar.meta.copy()
            
            # Update the bounds if projections do not match
            if src.crs != tar.crs:
                x, y = srcbounds[0::2], srcbounds[1::2]
                bounds = rasterio.warp.transform(src.crs, tar.crs, x, y)
                bounds = [ point for axis in bounds for point in axis ]
                keys = ['left', 'right', 'bottom', 'top']
                srcbounds = BoundingBox(**dict(zip(keys, bounds)))
            
            window = tar.window(*srcbounds)
            count = tarmeta["count"]
            taraff = tar.affine
            
            height = window[0][1] - window[0][0]
            width = window[1][1] - window[1][0]
            tarmeta.update(width=width, height=height)
            
            with rio.open(dstpath, 'w', **tarmeta) as dst:
                
                dst.transform = Affine(taraff.a, taraff.b, srcbounds.top, taraff.d, taraff.e, srcbounds.left)
                
                for bidx in range(1, count + 1):
                    band = tar.read(bidx, window=window)
                    dst.write_band(bidx, band)