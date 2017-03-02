#############################################################
# User input:
inTif = '/Volumes/RASMUS_1/Field_data_2016/Iffiartafik_2016/Iffiartafik_uav/sequoia_100m/agisoft/v3/iffiartafik_seq_100m_v3_refl_rect1.tif'
outNDVI = '/Volumes/RASMUS_1/Field_data_2016/Iffiartafik_2016/Iffiartafik_uav/sequoia_100m/agisoft/v3/iffiartafik_seq_100m_v3_refl_rect1_ndvi.tif'

#############################################################

import gdal
import numpy as np

ds = gdal.Open(inTif, gdal.GA_ReadOnly)

bandRed = ds.GetRasterBand(2)
aRed = bandRed.ReadAsArray().astype(np.float32)

bandNir = ds.GetRasterBand(4)
aNir = bandNir.ReadAsArray().astype(np.float32)

ndvi = (aNir - aRed) / (aNir + aRed)

# save to output tif
drv = gdal.GetDriverByName('GTiff')
outTif = drv.Create(outNDVI, ds.RasterXSize, ds.RasterYSize, 1, gdal.GDT_Float32)
outTif.SetGeoTransform(ds.GetGeoTransform())
outTif.SetProjection(ds.GetProjection())
outTif.GetRasterBand(1).WriteArray(ndvi)
outTif = None

print 'finished'