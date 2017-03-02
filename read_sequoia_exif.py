# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 12:58:48 2016

@author: btk596
"""
import exiftool
import glob

# findings:
#"EXIF:ExposureTime" varies
#"EXIF:DateTimeOriginal"
# "Composite:LightValue" varies
# "XMP:IrradianceCalibrationMeasurement" is constant
# "XMP:CalibrationMeasurement" is constant
# "XMP:VignettingPolynomial2DName" is constant
# "EXIF:FNumber" is constant
# "EXIF:ISO" is constant

#imgFile = r'C:\Users\btk596\Documents\software\exiftool-10.27\IMG_160815_163017_0001_GRE.TIF'
#files = [imgFile]
files = glob.glob(r'/Volumes/groupdirs/REMAINS/Field_data_2016/Iffiartafik_2016/Iffiartafik_uav/sequoia_100m/data/0014')

# NB if exiftool is not in windows PATH - then put path here:
# exiftool.ExifTool(executable_='full path')
with exiftool.ExifTool() as et:
    metadata = et.get_metadata_batch(files)
for d in metadata:
    #print("{:30.30} {:30.30}".format(d["SourceFile"][-30:],
    #                                 d["XMP:IrradianceCalibrationMeasurement"]))
    #print d["EXIF:ISO"]
    print d["EXIF:ExposureTime"]
    
#Irradiance Gain Index           : 1
#Irradiance Exposure Time        : 0.100000
##Irradiance Calibration Measurement: 0,600,14,1,1,600,323,37,2,600,5391,626,3,600,65535,15660
##Calibration Measurement         : 1,0.00311526479750779,464
#Vignetting Polynomial 2D Name   : 0,0,1,0,2,0,3,0,4,0,0,1,0,2,0,3,0,4,1,1,1,2,1,3,2,1,2,2,3,1
#Vignetting Polynomial 2D        : 0.7562020180280091,1.1264824215303069,-2.6696695964250181,3.0071531982772011,-1.4689567916235380,0.4082669339543161,-0.3184066771331092,-0.2274293062027746,0.1065379669565812,-1.0918397851886512,0.9974502466520518,0.0200064373266202,1.2678753224087242,-1.1064614371388299,-0.0784887541814723
#Exposure Time                   : 1/5417
#F Number                        : 2.2
#Spectral Sensitivity            : 550 nm
#ISO                             : 100
#Aperture Value                  : 2.2
#Max Aperture Value              : 2.2
#Focal Length                    : 4.0 mm
#Light Value                     : 14.7