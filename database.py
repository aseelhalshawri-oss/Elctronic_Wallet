# connection with Database of "ew" 
import oracledb

class Database:

    def __init__(self):

        oracledb.init_oracle_client(lib_dir=r"C:\oracle\instantclient-basic-windows.x64-19.32.0.0.0dbru\instantclient_19_32")

        self.connection=oracledb.connect(
            user="ew",
            password="ew",
            dsn="localhost:1521/orcl"
        )
        self.cursor=self.connection.cursor()

    def close(self):
        self.connection.close()
