import pymysql
import pandas as pd
import mysql.connector


class DatabaseConnection:

    def __init__(self, dbname):
        self.host = "classified-legislation.cfb1te3o5nxb.ap-south-1.rds.amazonaws.com"
        self.port = 3306
        self.user = "admin"
        self.password = "legalLankan2020"
        self.conn = pymysql.connect(host=self.host, user=self.user, port=self.port, passwd=self.password, db=dbname)

    def selectFromDB(self, sql):
        sql_result = pd.read_sql(sql, con=self.conn)
        return sql_result

    def insertToDB(self, sql,val):
        mydb = mysql.connector.connect(
            host=self.host,
            port = self.port,
            user = self.user,
            password = self.password
        )
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        mydb.commit()

    def updateDB(self, sql):
        mydb = mysql.connector.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password
        )

        mycursor = mydb.cursor()
        mycursor.execute(sql)
        mydb.commit()