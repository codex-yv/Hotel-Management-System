from mysql.connector import*
file22=open("2sql.txt",'r')
sqlp=file22.read()
# print(sqlp)
file22.close()
try:
    con=connect(
        host='localhost',
        user='root',
        password=sqlp
    )
    print("Connection Established!")
except Error as e:
    print(e)

finally:
    con.close()