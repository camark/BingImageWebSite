# ** -- coding: utf-8 -- **
#!/usr/bin/env python

import datetime
from urllib import urlopen, urlretrieve
from xml.dom import minidom
import os


#Variables:
idx = '0' #defines the day of the picture: 0 = today, 1 = yesterday, ... 20.
# saveDir = 'D:/ProgrammingStuff/GitHub/bing-wallpaper/images/' #in Windows you might put two \\ at the end
# saveDir = 'D:/Dropbox/Dropbox/BingImage/'
# saveDir = 'D:/Common/BingImage/'
saveDir = '/home/gm/opt/bingimg/'

operatingSystem = 'windows' #windows or linux (gnome)



#Methods for setting a picture as Wallpaper
def setWindowsWallpaper(picPath):
    cmd = 'REG ADD \"HKCU\Control Panel\Desktop\" /v Wallpaper /t REG_SZ /d \"%s\" /f' %picPath
    os.system(cmd)
    os.system('rundll32.exe user32.dll, UpdatePerUserSystemParameters')
    return


def setGnomeWallpaper(picPath):
    os.system('gsettings set org.gnome.desktop.background picture-uri file://' + picPath)
    return


#Getting the XML File
usock = urlopen(
    'http://www.bing.com/HPImageArchive.aspx?format=xml&idx=' + idx + '&n=1&mkt=ru-RU') #ru-RU, because they always have 1920x1200 resolution pictures
xmldoc = minidom.parse(usock)
#Parsing the XML File
for element in xmldoc.getElementsByTagName('url'):
    url = 'http://www.bing.com' + element.firstChild.nodeValue

    #Get Current Date as fileName for the downloaded Picture
    now = datetime.datetime.now()
    picPath = saveDir + "1920X1200/"+ now.strftime('bing_wp_%m-%d-%Y') + '.jpg'
    picPath_small = saveDir + "1366X768/" + now.strftime('bing_wp_%m-%d-%Y') + '.jpg'

    #Download and Save the Picture
    #Get a higher resolution by replacing the file name
    if not os.path.isfile(picPath):
        urlretrieve(url.replace('_1366x768', '_1920x1200'), picPath)
        urlretrieve(url, picPath_small)
    else:
            print "File exists."

    #Set Wallpaper:
    # if operatingSystem == 'windows':
        # setWindowsWallpaper(picPath)
    # elif operatingSystem == 'linux' or operatingSystem == 'gnome':
        # setGnomeWallpaper(picPath)
