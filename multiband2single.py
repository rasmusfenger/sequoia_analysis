#############################################################
# User input:
inFile = '/Volumes/RASMUS_1/Field_data_2016/Iffiartafik_2016/Iffiartafik_uav/sequoia_100m/agisoft/v3/iffiartafik_seq_100m_v3.tif'
outFolder = '/Volumes/RASMUS_1/Field_data_2016/Iffiartafik_2016/Iffiartafik_uav/sequoia_100m/agisoft/v3'

#############################################################

import os
import gdal

root,ext = os.path.splitext(inFile)
head,tail = os.path.split(root)
ds = gdal.Open(inFile, gdal.GA_ReadOnly)

drv = gdal.GetDriverByName('GTiff')

for bandNum in range(1,5):
    band = ds.GetRasterBand(bandNum)
    a = band.ReadAsArray()

    # make outputfile
    outFile = os.path.join(outFolder, tail + '_b' + str(bandNum) + '.tif')
    outTif = drv.Create(outFile, ds.RasterXSize, ds.RasterYSize, 1, gdal.GDT_UInt16)
    outTif.SetGeoTransform(ds.GetGeoTransform())
    outTif.SetProjection(ds.GetProjection())
    outTif.GetRasterBand(1).WriteArray(a)
    outTif = None

print 'finished'
