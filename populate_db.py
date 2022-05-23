import pymysql
from db_config import mysql
		
def log(msg):
    print(msg)

def clean_up():
	log("clean_up")
	conn = mysql.connect()
	cursor = conn.cursor(pymysql.cursors.DictCursor)
	cursor.execute("drop table if exists flower;")
	cursor.execute("drop table if exists pre_rolls;")

def flower():
    log("flower")
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql = """
    CREATE TABLE flower (
    id MEDIUMINT NOT NULL AUTO_INCREMENT,
    strain varchar(255) not null, 
    type varchar(255) not null, 
    farm varchar(255) not null, 
    weight_in_grams decimal(4,2) not null, 
    thc_percent decimal(4,2) not null, 
    cbd_percent decimal(4,2) not null, 
    harvest varchar(10) not null, 
    description varchar(255) not null, 
    price decimal(4,2) not null, 
    PRIMARY KEY (id)
    );
    """
    cursor.execute(sql)



def pre_rolls():
    log("pre_rolls")
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql = """
    CREATE TABLE pre_rolls (
    id MEDIUMINT NOT NULL AUTO_INCREMENT,
    brand varchar(255) not null, 
    type varchar(255) not null, 
    strain varchar(255) not null, 
    number_of_joints int(4) not null, 
    thc_percent decimal(4,2) not null, 
    cbd_percent decimal(4,2) not null, 
    harvest varchar(10) not null, 
    description varchar(255) not null, 
    price decimal(4,2) not null, 
    PRIMARY KEY (id)
    );
    """
    cursor.execute(sql)



def pre_rolls_populate():
    log("pre_roll_populate")
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    x = "INSERT INTO pre_rolls (brand, type, strain, number_of_joints, thc_percent, cbd_percent, harvest, description, price ) VALUES "
    ary = [
        """("Estraweeda","Indica","Blue City Diesel",10, 19.3, 0.2,	"12/13/18","", 25)""",
        """("Estraweeda","Sativa","Ken's Glue",10,	18.9,	0.03,	"8/8/18", "", 25 )"""

    ]
    for a in ary:
        sql = "{}{}".format(x,a)
        cursor.execute(sql)
        # print(sql)
        conn.commit()

def flower_populate():
    log("flower_populate")
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    x = "INSERT INTO flower (strain, type, farm, weight_in_grams, thc_percent, cbd_percent, harvest, description, price ) VALUES "
    ary = [
        """("Peanut Butter Pie","Indica","Noble",1.09, 27.3, 0.09, "10/22/19", "Indoor/outdoor terpenes",12.00)""",
        """("Sunset Sherbert","Hybrid","HighWinds",	1.01,28.4,0.1, "11/5/19","Indoor/outdoor, terpenes",11.00)""", 
        """("Headdog","Hybrid","Heros of the Farm",1.04,26.64,0.07, "7/14/19","Indoor/outdoor, terpenes",8.00)""",
        """("OG KB","Indica","Makru Farms", 1.04,	25.03,	0.09,"10/21/19","Indoor/outdoor, terpenes",10.00)""",
        """("Lost Cause","Sativa","Trichome",	1.08,	22.06,	0,"10/31/19","Indoor/outdoor, terpenes",9.00 )"""    
    ]
    for a in ary:
        sql = "{}{}".format(x,a)
        cursor.execute(sql)
        # print(sql)
        conn.commit()


if __name__ == "__main__":
    clean_up()
    flower()
    flower_populate()
    pre_rolls()
    pre_rolls_populate()