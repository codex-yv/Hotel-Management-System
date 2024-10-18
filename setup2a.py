try:
    from tkinter import*
    from tkinter import messagebox
    from mysql.connector import*
    win=Tk()
    
    file22=open("2sql.txt",'r')
    sqlp=file22.read()
    # print(sqlp)
    file22.close()
    def dbsetup():
        print("db setup entry!")
        global sqlp
        # screen.insert(END,"Setup has started--\n")
        # screen.after(2000,lambda:screen.insert(END,"Creating database hms\n"))
        try:
            conn = connect(
                host="localhost",  # Replace with your MySQL host if different
                user="root",       # Replace with your MySQL username
                password=sqlp  # Replace with your MySQL password
            )

            # Create a cursor object to interact with the database
            cursor = conn.cursor()
            
            print("Connected-1")

            # Specify the database name
            db_name = "hms"

            # Check if the database already exists
            cursor.execute("SHOW DATABASES LIKE %s", (db_name,))
            result = cursor.fetchone()

            if result:
                # screen.after(2000,lambda:screen.insert(END,f"Database {db_name} already exist.\n"))
                print("Database already exist!")
            else:
                # If not, create the database
                cursor.execute(f"CREATE DATABASE {db_name}")
                # screen.after(2000,lambda:screen.insert(END,f"Database {db_name} created Successfully.\n "))
                
            db_name2 = "sequrity"

            # Check if the database already exists
            cursor.execute("SHOW DATABASES LIKE %s", (db_name2,))
            result1 = cursor.fetchone()

            if result1:
                # screen.after(2000,lambda:screen.insert(END,f"Database {db_name2} already exist.\n"))
                print("databse already exist")
            else:
                # If not, create the database
                cursor.execute(f"CREATE DATABASE {db_name2}")
                # screen.after(2000,lambda:screen.insert(END,f"Database {db_name2} created Successfully.\n "))

        except Error as err:
            print(err)
            # screen.after(500,lambda err=err:screen.insert(END,f"ERROR:{err}\n"))

        finally:
            # Close cursor and connection
            cursor.close()
            conn.close()
            print("DB created!")
        
        
        try:
            connection = connect(
                host='localhost',          # e.g., 'localhost' or your MySQL server IP
                user='root',          # e.g., 'root' or your database user
                password=sqlp,  # your database password
                database='hms'   # your database name
            )

            if connection.is_connected():
                cursor = connection.cursor()
                # screen.after(2000,lambda:screen.insert(END,"Connection Establihed!\n"))
                
                # screen.after(500,lambda:screen.insert(END,"Creating table customer\n"))

                # SQL query to create the table
                create_table_query = """
                CREATE TABLE IF NOT EXISTS customer (
                    SLNO INT AUTO_INCREMENT PRIMARY KEY,
                    CUSTOMER_ID INT,
                    CUSTOMER_NAME varchar(50),
                    PHONE bigint,
                    ID_TYP varchar(15),
                    ID_NO varchar(30),
                    STATE varchar(35),
                    DISTRICT varchar(35),
                    ADULTS int,
                    CHILD int,
                    checkin date,
                    checkout date,
                    ROOM_NO varchar(10),
                    ROOM_TYP varchar(15),
                    COST bigint,
                    AGE_VERIFIED varchar(5),
                    TIME timestamp DEFAULT CURRENT_TIMESTAMP ,
                    UPDATED timestamp DEFAULT CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP
                );
                """
                
                # screen.after(2000,lambda:screen.insert(END,"Created column SLNO INT AUTO_INCREMENT PRIMARY KEY\n"))
                # screen.after(2000,lambda:screen.insert(END,"Created column CUSTOMER_ID INT\n"))
                # screen.after(2000,lambda:screen.insert(END,"Created column CUSTOMER_NAME varchar(50)\n"))
                # screen.after(2000,lambda:screen.insert(END,"Created column PHONE bigint\n"))
                # screen.after(2000,lambda:screen.insert(END,"Created column ID_TYP varchar(15)\n"))
                # screen.after(2000,lambda:screen.insert(END,"Created column ID_NO varchar(30)\n"))
                # screen.after(2000,lambda:screen.insert(END,"Created column STATE varchar(35)\n"))
                # screen.after(2000,lambda:screen.insert(END,"Created column DISTRICT varchar(35)\n"))
                # screen.after(2000,lambda:screen.insert(END,"Created column ADULTS int\n"))
                # screen.after(2000,lambda:screen.insert(END,"Created column CHILD int\n"))
                # screen.after(2000,lambda:screen.insert(END,"Created column checkin date\n"))
                # screen.after(2000,lambda:screen.insert(END,"Created column checkout date\n"))
                # screen.after(2000,lambda:screen.insert(END,"Created column ROOM_NO varchar(10)\n"))
                # screen.after(2000,lambda:screen.insert(END,"Created column ROOM_TYP varchar(15)\n"))
                # screen.after(2000,lambda:screen.insert(END,"Created column COST bigint\n"))
                # screen.after(2000,lambda:screen.insert(END,"Created column AGE_VERIFIED varchar(5)\n"))
                # screen.after(2000,lambda:screen.insert(END,"Created column TIME timestamp CURRENT_TIMESTAMP DEFAULT_GENERATED\n"))
                # screen.after(2000,lambda:screen.insert(END,"Created column UPDATED timestamp YES CURRENT_TIMESTAMP DEFAULT_GENERATED on update CURRENT_TIMESTAMP\n"))

                # Executing the query to create the table\n
                cursor.execute(create_table_query)
                # screen.after(2000,lambda:screen.insert(END,"Successfully Created customer table.\n"))
                
                # screen.after(500,lambda:screen.insert(END,"Creating table rooms.\n"))
                create_table2_query = """
                CREATE TABLE IF NOT EXISTS rooms (
                    SLNO INT AUTO_INCREMENT PRIMARY KEY,
                    ROOM_NO varchar(10),
                    ROOM_TYP varchar(20),
                    ROOM_SYM varchar(20),
                    C_STATUS varchar(20),
                    checkin date,
                    checkout date
                );
                """
                # screen.after(2000,lambda:screen.insert(END,"Created column SLNO INT AUTO_INCREMENT PRIMARY KEY\n"))
                # screen.after(2000,lambda:screen.insert(END,"Created column ROOM_NO varchar(10)\n"))
                # screen.after(2000,lambda:screen.insert(END,"Created column ROOM_TYP varchar(20)\n"))
                # screen.after(2000,lambda:screen.insert(END,"Created column ROOM_SYM varchar(20)\n"))
                # screen.after(2000,lambda:screen.insert(END,"Created column C_STATUS varchar(20)\n"))
                # screen.after(2000,lambda:screen.insert(END,"Created column checkin date\n"))
                # screen.after(2000,lambda:screen.insert(END,"Created column checkout date\n"))
                cursor.execute(create_table2_query)
                # screen.after(2000,lambda:screen.insert(END,"Successfully Created rooms table.\n"))
                
                # screen.after(500,lambda:screen.insert(END,"Creating table dining.\n"))
                create_table3_query = """
                CREATE TABLE IF NOT EXISTS dining (
                    SLNO INT AUTO_INCREMENT PRIMARY KEY,
                    FOOD varchar(50),
                    FOOD_TYP varchar(20)
                );
                """
                
                # screen.after(2000,lambda:screen.insert(END,"Created column SLNO INT AUTO_INCREMENT PRIMARY KEY\n"))
                # screen.after(2000,lambda:screen.insert(END,"Created column FOOD varchar(50)\n"))
                # screen.after(2000,lambda:screen.insert(END,"Created column FOOD_TYP varchar(20)\n"))
                cursor.execute(create_table3_query)
                # screen.after(2000,lambda:screen.insert(END,"Successfully Created dining table.\n"))
                
                # screen.after(500,lambda:screen.insert(END,"Creating table advbk\n"))
                create_table4_query = """
                CREATE TABLE IF NOT EXISTS advbk (
                    SLNO INT AUTO_INCREMENT PRIMARY KEY,
                    CUSTOMER_ID int,
                    CUSTOMER_NAME varchar(50),
                    PHONE bigint,
                    STATE varchar(35),
                    ADULTS int,
                    CHILD int,
                    checkin date,
                    checkout date,
                    ROOM_NO varchar(10),
                    COST bigint
                );
                """
                
                # screen.after(2000,lambda:screen.insert(END,"Created column SLNO INT AUTO_INCREMENT PRIMARY KEY\n"))
                # screen.after(2000,lambda:screen.insert(END,"Created column CUSTOMER_ID int\n"))
                # screen.after(2000,lambda:screen.insert(END,"Created column CUSTOMER_NAME varchar(50)\n"))
                # screen.after(2000,lambda:screen.insert(END,"Created column PHONE bigint\n"))
                # screen.after(2000,lambda:screen.insert(END,"Created column STATE varchar(35)\n"))
                # screen.after(2000,lambda:screen.insert(END,"Created column ADULTS int\n"))
                # screen.after(2000,lambda:screen.insert(END,"Created column CHILD int\n"))
                # screen.after(2000,lambda:screen.insert(END,"Created column checkin date\n"))
                # screen.after(2000,lambda:screen.insert(END,"Created column checkout date\n"))
                # screen.after(2000,lambda:screen.insert(END,"Created column COST bigint\n"))
                cursor.execute(create_table4_query)
                # screen.after(3000,lambda:screen.insert(END,"Successfully Created advbk table.\n\n"))
                
                # screen.after(3000,lambda:screen.insert(END,"#########-------Setup Completed-------#########.\n"))
                # screen.after(3000,lambda:screen.insert(END,"You may now run main.py file!!.\n\n"))
                
                

        except Error as e:
            print(e)

        finally:
            cursor.close()
            connection.close()
            print("Setup Complete!")
            # screen.after(500,lambda:screen.insert(END,"CONNECTION Closed!\n"))
            # dnbtn.pack(side=BOTTOM,pady=15)

    def dbsetup2():
        print("DB setup 2 started!")
        global sqlp
        try:
            connection1 = connect(
                host='localhost',          # e.g., 'localhost' or your MySQL server IP
                user='root',          # e.g., 'root' or your database user
                password=sqlp,  # your database password
                database='sequrity'   # your database name
            )
            cursor1=connection1.cursor()
            print("print connected- 2")
            # screen.after(500,lambda:screen.insert(END,"Creating table pvalue.\n"))
            create_table11_query = """
            CREATE TABLE IF NOT EXISTS pvalue (
                passwordd varchar(30)
            );
            """
            cursor1.execute(create_table11_query)
            # screen.after(2000,lambda:screen.insert(END,"Successfully Created pvalue table.\n"))
        except Error as ee:
            print(ee)
        finally:
            cursor1.close()
            connection1.close()
            # screen.after(500,lambda:screen.insert(END,"CONNECTION Closed!\n"))
            print("finally done!!")

            
        

    def ex():
        exit()
    def cn():
        try:
            file=open("hname.txt",'r+')
            file.write(hnval.get())
            
            # file2=open("sql.txt",'w')
            # if len(sqlval.get())!=0:
            #     file2.write(sqlval.get())
            # else:
            #     messagebox.showerror("SQL","Password can't be negative!")
            #     pass
            
        except FileNotFoundError:
            messagebox.showerror("File Error","File Not Found!")
        finally:
            file.close()
            # file2.close()
            # label1.pack_forget()
            # hname.pack_forget()
            # hentry.place_forget()
            # exbtn.pack_forget()
            # conbtn.pack_forget()
            # sqlf.pack_forget()
            # sqle.pack_forget()
            # screen.pack(pady=10,padx=10)
            dbsetup()
            dbsetup2()
        
        
      

    win.geometry("650x400")
    win.maxsize(650,400)
    win.minsize(650,400)
    win.title("SETUP-2")
    win.iconbitmap("setting.ico")
    win.config(bg="#e5e7e9")
    
    label1=Label(win,text="CODEX\n presents\n HOTEL MANAGEMENT SYSTEM",font=('Bahnschrift',18,'bold'),bg="#e5e7e9")
    label1.pack(pady=30)
    hname=LabelFrame(win,text="Your Hotel Name",font=('Bahnschrift',11,'bold'),fg='#1a5276',height=57,width=350,bg="#e5e7e9")
    hname.pack()
    hnval=StringVar()
    hentry=Entry(win,font=('Calibri (Body)',15),width=30,textvariable=hnval,bg="#e5e7e9",relief="flat")
    hentry.place(x=157,y=175)
    
    # sqlf=LabelFrame(win,text="Mysql Password",font=('Bahnschrift',11,'bold'),fg='#1a5276',height=57,width=350,bg="#e5e7e9")
    # sqlf.pack()
    # sqlval=StringVar()
    # sqle=Entry(win,font=('Calibri (Body)',15),width=30,textvariable=sqlval,bg="#e5e7e9",relief="flat")
    # sqle.place(x=157,y=235)
    
    exbtn=Button(win,text="Exit",font=('Bahnschrift',11,'bold'),bg="#cb4335",fg='white',width=20,
                 cursor="hand2",command=ex)
    exbtn.pack(side=RIGHT,anchor='se',pady=50,padx=30)
    conbtn=Button(win,text="Next",font=('Bahnschrift',11,'bold'),bg="#1a5276",fg='white',width=20,
                  cursor="hand2",command=cn)
    conbtn.pack(side=RIGHT,anchor='se',pady=50,padx=30)
    
    # screen=Text(win,relief=SUNKEN,bd=5,height=20,fg='#0b5345')
    
    # dnbtn=Button(win,text="Done",font=('Bahnschrift',11,'bold'),bg="#1a5276",fg='white',width=20,
    #               cursor="hand2",command=exit)
    

    
    win.mainloop()
    
    
except ImportError:
    print("\n+++++++++++++Please run setup1 before running this code!!+++++++++++++")