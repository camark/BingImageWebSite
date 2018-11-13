#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

class RandomBingimage:
	def getRandomImage(self):
		db = MySQLdb.connect("10.10.10.9", "root", "find8all", "hr_jifen", charset='utf8' )

                # 使用cursor()方法获取操作游标 
                cursor = db.cursor()

                # 使用execute方法执行SQL语句
                cursor.execute("SELECT * from randombingimage")

               # 使用 fetchone() 方法获取一条数据
                data = cursor.fetchone()

		db.close()
		#print data
		return data[1]

if __name__ == '__main__':
	u=RandomBingimage()
	print u.getRandomImage()	
