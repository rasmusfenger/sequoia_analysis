#############################################################
# User input:
inputDN = '/Volumes/btk596/temp//iffiartafik_seq_100m_v3_warp.tif'
outRef = '/Volumes/btk596/temp//iffiartafik_seq_100m_v3_warp_refl.tif'

# DN/reflectance relation
# linear relation y = a*x + b
# 1. num in list = a, 2. = b

dnRef = {1: [9.13174993534e-06, -0.066967637738],
         2: [8.44461071549e-06, -0.027604568569],
         3: [1.2691265573e-05, -0.061648906527],
         4: [1.48535062234e-05, -0.0783022446058]}

# Iffiartafi emperical line Sequoia img 132
#dnRef = {1:[108614, 7442.7],
#         2:[115747, 3778.9],
#         3:[78168, 5031.6],
#         4:[66844, 5400.8]}

# Iffiartafi emperical line Sequoia mosaic v3
#dnRef = {1: [97749, 9162.5],
#         2: [107866, 9666.3],
#         3: [77366, 7612.2],
#         4: [61355, 8391.2]}
#############################################################

import gdal
import numpy as np
from seqfunc import *

ds = gdal.Open(inputDN, gdal.GA_ReadOnly)
drv = gdal.GetDriverByName('GTiff')

# prepare output tif
outTif = drv.Create(outRef, ds.RasterXSize, ds.RasterYSize, 4, gdal.GDT_Float32)
outTif.SetGeoTransform(ds.GetGeoTransform())
outTif.SetProjection(ds.GetProjection())

for bandNum in range(1,5):
    band = ds.GetRasterBand(bandNum)
    dn = band.ReadAsArray().astype(np.float32)
    ref = convertDN2refl(dn, dnRef[bandNum])
    outTif.GetRasterBand(bandNum).WriteArray(ref)

outTif = None
print 'finished'