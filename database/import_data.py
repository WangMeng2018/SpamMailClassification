import pymysql
import os

# 打开数据库连接
db = pymysql.connect("localhost","root","","textclassify" )
 
# 使用cursor()方法获取操作游标 
cursor = db.cursor()

error_list = []
# 打开数据文件
f = open("E://学习//研究生学习//网络数据挖掘//大作业//垃圾短信分类//带标签短信.txt",'r', encoding='UTF-8')
i=0
lines = f.readlines()
for line in lines:
	i = i + 1
	d = line.split('\t')
	#print(d[0],d[1])
	# SQL 插入语句
	sql = "INSERT INTO experiment_text(id, label, content) \
		   VALUES ('%d', '%d', '%s')" % \
		   (i, int(d[0]), d[1])
	try:
	   # 执行sql语句
	   cursor.execute(sql)
	   # 执行sql语句
	   db.commit()
	except:
	   # 发生错误时回滚
	   print(i)
	   error_list.append(i)
	   db.rollback()
 
# 关闭数据库连接
db.close()
f.close()

w = open("E://学习//研究生学习//网络数据挖掘//大作业//垃圾短信分类//error.txt",'w')
for x in error_list:
	w.write(str(x)+'\n')
w.close()