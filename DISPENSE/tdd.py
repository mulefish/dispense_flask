import pymysql
from app import app
from db_config import mysql
from flask import flash, session, render_template, request, redirect, url_for
#from werkzeug import generate_password_hash, check_password_hash
from werkzeug.security import generate_password_hash, check_password_hash
		
def products():
	conn = mysql.connect()
	cursor = conn.cursor(pymysql.cursors.DictCursor)

	try:
		cursor.execute("SELECT * FROM product")
		rows = cursor.fetchall()
		# print(rows)
		for x in rows:
			print(x["image"])
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		print("Finally")

	
		
if __name__ == "__main__":
    
    products()