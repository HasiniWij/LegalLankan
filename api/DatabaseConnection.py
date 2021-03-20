import pymysql
import pandas as pd
class DatabaseConnection:

    def __init__(self, dbname):
        host = "classified-legislation.cfb1te3o5nxb.ap-south-1.rds.amazonaws.com"
        port = 3306
        user = "admin"
        password = "legalLankan2020"
        self.conn = pymysql.connect(host=host, user=user, port=port, passwd=password, db=dbname)

    def get_details(self,sql):
        sql_result = pd.read_sql(sql, con=self.conn)
        return sql_result

