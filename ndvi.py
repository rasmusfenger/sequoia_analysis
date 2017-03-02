import gdal
import numpy as np

#red = '/Users/rasmus/Desktop/sequoia_test/0004/IMG_160804_094639_0000_RED.TIF'
#nir = '/Users/rasmus/Desktop/sequoia_test/0004/IMG_160804_094639_0000_NIR.TIF'
#outFile = '/Users/rasmus/Desktop/sequoia_test/0004/ndvi.tif'

red = '/Users/rasmus/Desktop/sequoia_test/0005/IMG_160804_094653_0000_RED.TIF'
nir = '/Users/rasmus/Desktop/sequoia_test/0005/IMG_160804_094653_0000_NIR.TIF'
outFile = '/Users/rasmus/Desktop/sequoia_test/0005/ndvi.tif'

#red = '/Users/rasmus/Desktop/sequoia_test/0006/IMG_160804_094707_0000_RED.TIF'
#nir = '/Users/rasmus/Desktop/sequoia_test/0006/IMG_160804_094707_0000_NIR.TIF'
#outFile = '/Users/rasmus/Desktop/sequoia_test/0006/ndvi.tif'

dsRed = gdal.Open(red)
bandRed = dsRed.GetRasterBand(1)
aRed = bandRed.ReadAsArray().astype(np.float32)

dsNir = gdal.Open(nir)
bandNir = dsNir.GetRasterBand(1)
aNir = bandNir.ReadAsArray().astype(np.float32)

ndvi = (aNir - aRed) / (aNir + aRed)

drv = gdal.GetDriverByName('GTiff')
outTif = drv.Create(outFile, dsRed.RasterXSize, dsRed.RasterYSize, 1, gdal.GDT_Float32)
outTif.SetGeoTransform(dsRed.GetGeoTransform())
#outTif.SetProjection(ds.GetProjection())
outTif.GetRasterBand(1).WriteArray(ndvi)
#outTif.GetRasterBand(1).SetNoDataValue(nodataValue)
outTif = None

