from mysql.connector import*
try:
    con=connect(
        host='localhost',
        user='root',
        password='ssap856'
    )
    print("Connection Established!")
except Error as e:
    print(e)

finally:
    con.close()