#############################################################
# User input:
inputDN = '/Volumes/RASMUS_1/Field_data_2016/Iffiartafik_2016/Iffiartafik_uav/sequoia_100m/atlas/07092016_processing_noreference/2016-08-15T16_30_53Z_BGREN_iffiartafik.tif'
outRef = '/Volumes/RASMUS_1/Field_data_2016/Iffiartafik_2016/Iffiartafik_uav/sequoia_100m/atlas/07092016_processing_noreference/2016-08-15T16_30_53Z_BGREN_iffiartafik_refl.tif'

#############################################################

import gdal
import numpy as np

ds = gdal.Open(inputDN, gdal.GA_ReadOnly)

drv = gdal.GetDriverByName('GTiff')

# prepare output tif
outTif = drv.Create(outRef, ds.RasterXSize, ds.RasterYSize, 4, gdal.GDT_Float32)
outTif.SetGeoTransform(ds.GetGeoTransform())
outTif.SetProjection(ds.GetProjection())

for bandNum in range(1,5):
    band = ds.GetRasterBand(bandNum)
    dn = band.ReadAsArray().astype(np.float32)
    ref = dn/32768
    outTif.GetRasterBand(bandNum).WriteArray(ref)

outTif = None
print 'finished'