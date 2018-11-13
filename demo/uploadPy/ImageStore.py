# ** -- coding: utf-8 -- **
#!/usr/bin/env python

from weed import operation
from ImageDB import ImageDB

class ImageStore:
	def __init__(self,size_type):		
		self.wo = operation.WeedOperation()
		self.db = ImageDB()
                self.size_type=size_type
	
        def storeImg(self,filename):
		wor = self.wo.put(filename)
		
                #print wor
		public_url=wor.url.replace('localhost','10.10.10.126')
		fid=wor.fid
		
		#print public_url
                self.db.insertImg(public_url,fid,self.size_type,filename)
		

if __name__ == '__main__':
	ist=ImageStore(1)
	ist.storeImg('u3.jpg')
