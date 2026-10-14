import oracledb

oracledb.init_oracle_client(lib_dir=r"C:\oracle\instantclient-basic-windows.x64-19.32.0.0.0dbru\instantclient_19_32")

db_user = "ew"
db_password = "ew"
db_host = "localhost"
db_port = 1521
db_service = "orcl"

print("pending of connection")
print(f"DSN : {db_host} : {db_port}/{db_service}")

try:
    connection= oracledb.connect(
        user=db_user,
        password=db_password,
        dsn=f"{db_host}:{db_port}/{db_service}"
    )
    print("connected successfully")

    cursor =connection.cursor()
    # cursor.execute("SELECT 'Hello EW' FROM DUAL")
    # print("Result : ",cursor.fetchall()[0][0])

    cursor.close()
    connection.close()
    print("closed successfully")

except Exception as e:
    print(f"FALSE : {e}")
