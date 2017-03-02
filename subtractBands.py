#############################################################
# User input:
f1 = '/Volumes/btk596/temp/iffiartafik_seq_100m_v3_warp_clip_filt5.tif'
f2 = '/Volumes/btk596/temp/2016-08-15T16_30_53Z_BGREN_iffiartafik_filt5.tif'
outFolder = '/Volumes/btk596/temp/subtract'
#############################################################

import os
import gdal
from seqfunc import *
import numpy as np

root,ext = os.path.splitext(f1)
head,tail = os.path.split(root)
ds1 = gdal.Open(f1, gdal.GA_ReadOnly)
ds2 = gdal.Open(f2, gdal.GA_ReadOnly)

drv = gdal.GetDriverByName('GTiff')

# Iffiartafi emperical line Sequoia img 132
dnRef = {1:[9.13174993534e-06, -0.066967637738],
         2:[8.44461071549e-06, -0.027604568569],
         3:[1.2691265573e-05, -0.061648906527],
         4:[1.48535062234e-05, -0.0783022446058]}

for bandNum in range(1,5):
    band1 = ds1.GetRasterBand(bandNum)
    a1 = band1.ReadAsArray().astype(np.float32)

    band2 = ds2.GetRasterBand(bandNum)
    a2 = band2.ReadAsArray().astype(np.float32)

    a1 = convertDN2refl(a1, dnRef[bandNum])
    a2 = convertAtlas2refl(a2)

    aSubtract = a1-a2

    # make outputfile
    outFile = os.path.join(outFolder, tail + '_subtract_b' + str(bandNum) + '.tif')
    outTif = drv.Create(outFile, ds1.RasterXSize, ds1.RasterYSize, 1, gdal.GDT_Float32)
    outTif.SetGeoTransform(ds1.GetGeoTransform())
    outTif.SetProjection(ds1.GetProjection())
    outTif.GetRasterBand(1).WriteArray(aSubtract)
    outTif = None

print 'finished'
