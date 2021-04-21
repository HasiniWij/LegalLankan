import pymysql  # used to communicate with the database
import pandas as pd  # when queried from the database the result is put into a dataframe


# Database connection is formed  through this file (Insert, select,update)
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

    def insertToDB(self, sql, val):
        cur = self.conn.cursor()
        cur.execute(sql, val)
        self.conn.commit()
        cur.close()

    def updateDB(self, sql):
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()
        cur.close()
