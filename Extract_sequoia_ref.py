# Rasmus Fenger-Nielsen
# December 2016
# This script extracts the mean, std, pixel count and image exposure time from images based on pre-made masks of
# reference plates in the images. The ectracted information is saved to a csv file.
# The masks are prepared using the matlab script roi_seq_test.m.

#############################################################
# User input:

# Specify folder with all images
#inImgFolder = '/Volumes/RASMUS_1/Field_data_2016/Iffiartafik_2016/Iffiartafik_uav/sequoia_100m/data/0014'
inImgFolder = '/Volumes/RASMUS_1/Field_data_2016/Ersaa_2016/uav_ersaa/sequoia_60m/data/0003'
#inImgFolder = '/Volumes/RASMUS_1/Field_data_2016/Iffiartafik_2016/Iffiartafik_uav/sequoia_100m/agisoft/v3'
# Specify folder with all masks
inMaskFolder = '/Users/rasmus/Desktop/sequoia_mask'
# Specify output csv filename where extracted data is saved
outFileName = 'Extracted_sequoia_ref_data.csv'
#############################################################

import os
import glob
import numpy as np
from osgeo import gdal
import exiftool

outFilePath = os.path.join(inMaskFolder,outFileName)
resultList = [['Image name', 'Channel', 'Reference plate', 'Mean', 'Std', 'count', 'exposuretime']]

# make list of images and masks to be processed
imgList = glob.glob(inImgFolder + '/*.TIF')
maskList = glob.glob(inMaskFolder + '/*.TIF')

# loop through each mask
for mask in maskList:
    root,ext = os.path.splitext(mask)
    head,tail = os.path.split(root)
    imgFilename = tail[:-6] + ext
    imgPath = os.path.join(inImgFolder,imgFilename)

    # continue if the mask matches with a image in the inputfolder else inform user
    if any(imgFilename in img for img in imgList):
        # read mask
        dsMask = gdal.Open(mask, gdal.GA_ReadOnly)
        bandMask = dsMask.GetRasterBand(1)
        m = bandMask.ReadAsArray().astype(np.uint8)

        # read image
        dsImg = gdal.Open(imgPath, gdal.GA_ReadOnly)
        bandImg = dsImg.GetRasterBand(1)
        img = bandImg.ReadAsArray().astype(np.uint16)

        # extract masked values
        imgMasked = np.ma.array(img, mask=m)
        imgMaskedData = np.ma.compressed(imgMasked)
        imgMaskedMean = np.mean(imgMaskedData)
        imgMaskedStd = np.std(imgMaskedData)
        imgMaskedSize = np.size(imgMaskedData)

        # extract information from image exif file
        try:
            with exiftool.ExifTool() as et:
                metadata = et.get_metadata(imgPath)
                #print metadata["EXIF:ISO"]
                #print metadata["EXIF:FNumber"]
                exptime = metadata["EXIF:ExposureTime"]
        except:
            exptime = 'nodata'

        # Write to results
        resultList.append([imgFilename,imgFilename[23:26],tail[-1],imgMaskedMean,imgMaskedStd,imgMaskedSize,exptime])

    else:
        print 'Could not find file: ', imgFilename

# Save to file
np.savetxt(outFilePath, resultList, fmt="%s", delimiter=',')
print 'File saved: ', outFilePath
