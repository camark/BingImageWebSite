# ** -- coding: utf-8 -- **
#!/usr/bin/env python

from ImageStore import ImageStore
#from ImageDB import ImageDB
import os

base_dir='/home/gm/opt/bingimg/'

dir_1366 = base_dir + '1366X768'
dir_1920 = base_dir + '1920X1200'

dir_dict={dir_1366:1,dir_1920:2}


for (vdir,vtype) in dir_dict.items():
	ist = ImageStore(vtype)
	for f in os.listdir(vdir):
		filename=vdir+'/'+f
		#print filename
                if (not ist.db.is_image_saved(filename)) and os.path.getsize(filename)>0:
		    ist.storeImg(filename)


