# ** -- coding: utf-8 -- **
#!/usr/bin/env python

import pymysql.cursors

# Connect to the database
class ImageDB:
	
	def __init__(self):
		self.connection = pymysql.connect(host='10.10.10.9',
									 user='root',
									 password='find8all',
									 db='hr_jifen',
									 charset='utf8mb4',
									 cursorclass=pymysql.cursors.DictCursor)

	def insertImg(self,url,fid,size_type,filename):
		with self.connection.cursor() as cursor:
			# Create a new record
			sql = "INSERT INTO `ot_bingimage` (`url`, `fid`,`img_type`,`img_file_name`) VALUES ('%s', '%s', %d,'%s')" %  (url, fid, size_type,filename)
			cursor.execute(sql)

		# connection is not autocommit by default. So you must commit to save
		# your changes.
		self.connection.commit()

        def is_image_saved(self,file_name):
                with self.connection.cursor() as cursor:
                    sql="select count(*) as ic from ot_bingimage where img_file_name='%s'" % (file_name)
                    cursor.execute(sql)

                    row_one=cursor.fetchone()

                    return row_one['ic']>=1

	def __del__(self):
		self.connection.close()
		

if __name__ == '__main__':
	id=ImageDB()
	#id.insertImg('s1',10)
        print id.is_image_saved('/home/gm/opt/bingimg/1366x768/bing_wp_07-20-2018.jpg')
