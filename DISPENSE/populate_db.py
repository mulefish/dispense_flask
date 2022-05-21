import pymysql
from app import app
from db_config import mysql
from flask import flash, session, render_template, request, redirect, url_for
#from werkzeug import generate_password_hash, check_password_hash
from werkzeug.security import generate_password_hash, check_password_hash


def drop_tables():
	conn = mysql.connect()
	cursor = conn.cursor(pymysql.cursors.DictCursor)
	cursor.execute("drop table if exists product")
	cursor.execute("drop table if exists flower")
	cursor.execute("drop table if exists customers")
	cursor.execute("drop table if exists pre_rolls")

	print("Dropped tables")
		
def products():
	conn = mysql.connect()
	cursor = conn.cursor(pymysql.cursors.DictCursor)

	sql = """
    CREATE TABLE `product` (
	`id` int unsigned COLLATE utf8mb4_unicode_ci NOT NULL AUTO_INCREMENT,
	`name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
	`code` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
	`image` text COLLATE utf8mb4_unicode_ci NOT NULL,
	`price` double COLLATE utf8mb4_unicode_ci NOT NULL,
	PRIMARY KEY (`id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;
    """

	cursor.execute(sql)
	print("Created product table")
	
def flower():
	conn = mysql.connect()
	cursor = conn.cursor(pymysql.cursors.DictCursor)

	sql = """
CREATE TABLE `flower` (
	`id` int unsigned COLLATE utf8mb4_unicode_ci NOT NULL AUTO_INCREMENT,
	`strain` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
	`type` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `farm` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `weight_in_grams` decimal(4,2) COLLATE utf8mb4_unicode_ci NOT NULL,
    `thc_percent` decimal(4,2) COLLATE utf8mb4_unicode_ci NOT NULL,
    `cbd_percent` decimal(4,2) COLLATE utf8mb4_unicode_ci NOT NULL,
    `harvest date` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `description` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `price` decimal(4,2) COLLATE utf8mb4_unicode_ci NOT NULL,
	PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;
    """

	cursor.execute(sql)
	print("Created flower table")


def pre_rolls():
	conn = mysql.connect()
	cursor = conn.cursor(pymysql.cursors.DictCursor)

	sql = """
CREATE TABLE `pre_rolls` (
	`id` int unsigned COLLATE utf8mb4_unicode_ci NOT NULL AUTO_INCREMENT,
	`brand` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
	`type` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `strain` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `number_of_joints` int(4) COLLATE utf8mb4_unicode_ci NOT NULL,
    `thc_percent` decimal(4,2) COLLATE utf8mb4_unicode_ci NOT NULL,
    `cbd_percent` decimal(4,2) COLLATE utf8mb4_unicode_ci NOT NULL,
    `harvest date` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `description` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `price` decimal(4,2) COLLATE utf8mb4_unicode_ci NOT NULL,
	PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;
    """

	cursor.execute(sql)
	print("Created pre_rolls table")



if __name__ == "__main__":
    drop_tables()    
    products()
    flower()
    pre_rolls()