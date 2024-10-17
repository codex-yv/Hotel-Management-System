from tkinter import*
from tkinter import ttk
from mysql.connector import*
from PIL import Image, ImageTk
from datetime import datetime,timedelta,date
from tkcalendar import*
from tabulate import tabulate 
from random import*
from mysql.connector import errorcode
from tkinter import messagebox
import os

# import time as wait

file22=open("2sql.txt",'r')
sqlp=file22.read()
file22.close()

file=open('login.txt','r+')
data=file.read()
if data == '0':
    file.write('1')
    def resize_image(image_path, size):  
        with Image.open(image_path) as img:
            img = img.resize(size)  
            return ImageTk.PhotoImage(img)
    
    c=1
    def show():
        password=value.get()
        global c
        if c%2==1:
            hider.config(text=password,fg='#fbfcfc',bg='#1f618d')
            hu_button.config(text="Hide")
            c=c+1
        elif c%2==0:
            hider.config(text='',bg='#154360')
            hu_button.config(text="Show")
            c=c+1
    
    def passwd():
        global sqlp
        password=[value.get()]
        if len(password[0])>=4 and len(password[0])<=30:
            thanks.config(text='Thanks for using our software!',font=('Bahnschrift',12),bg='#ecf0f1',fg='black')
            try:
                connection = connect(
                    host='localhost',
                    user='root',
                    password=sqlp,
                    database='sequrity')
            
                cursor = connection.cursor()
                insert_query = "INSERT INTO pvalue (passwordd) VALUES (%s)"
                values = (password)
                
                cursor.execute(insert_query, values)
                connection.commit() 
                thanks.config(text='Regitration Done! Restart the App.')
                

            except Error as e:
                print(f"Error: {e}")
                thanks.config(text='Error!--Contact:yourajverma960@gmail.com',font='8',bg='red',fg='white')

            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
        elif len(password[0])>=30:
            thanks.config(text='Password Should not contain more than 30 letters!',bg='red',fg='white',
                          font=('Bahnschrift',10))           
        else:
            thanks.config(text='Password Should contain at least 4 letters!',bg='red',fg='white',
                          font=('Bahnschrift',10,'bold'))
            


        
    register=Tk()
    register.geometry("450x500+550+150")
    register.config(bg='#154360')
    register.title("Registration")
    register.iconbitmap('verify.ico')
    register.resizable(False,False)


    img_siz=(100,100)
    img_path='logo.png'
    logo=resize_image(img_path,img_siz)
    logo_label=Label(register,image=logo,bg='#1f618d',relief=RAISED,bd='5')
    logo_label.pack(pady=50)

    # create password label frame--------
    c_password=LabelFrame(register,text='Create password',font=('Bahnschrift',12),height=60,width=290,bg='#154360',
                          bd=2,fg='#fbfcfc')
    c_password.pack()
    value=StringVar()
    p_entry=Entry(register,font=('Bahnschrift',12),bg='#154360',fg='#fbfcfc',show='*',
                  relief=FLAT,textvariable=value)
    p_entry.place(x=90,y=230,height=32,width=200)
    # value.set('Enter your password bla bla bla')

    hu_button=Button(register,text='Show',font=('Bahnschrift',12),bg='#154360',command=show,fg='#fbfcfc',
                     relief='flat',cursor='hand2')
    hu_button.place(x=310,y=230)

    hider=Label(register,text='',font=('Bahnschrift',12),height=1,width=25,bg='#154360')
    hider.place(x=90,y=274)

    reg_button=Button(register,text='Register',font=('Bahnschrift',14,'bold'),height=1,width=10,bg='#1abc9c',
                      fg='#fbfcfc',command=passwd,cursor='hand2')
    reg_button.pack(pady=50)
    
    thanks=Label(register,text='Thanks for using our software!',font=('Bahnschrift',12),bg='#ecf0f1')
    thanks.pack(side='bottom',fill=X,)

    register.mainloop()


else:
    l=[]
    foodopt2=[]
    bildict={}
    avaiopt=[]
    error=0
    def resize_image(image_path, size):  
        with Image.open(image_path) as img:
            img = img.resize(size)  
            return ImageTk.PhotoImage(img)
    
    c1=1
    def show2():
        password2=loginvalue.get()
        global c1
        if c1%2==1:
            hider2.config(text=password2,fg='#76448a',bg='#f2f3f4')
            hu_button2.config(text="Hide")
            c1=c1+1
        elif c1%2==0:
            hider2.config(text='',bg='#d1f2eb')
            hu_button2.config(text="Show")
            c1=c1+1
    
    def logentry():
        global sqlp
        
        conn =connect(
            host="localhost",
            user="root",
            password=sqlp,
            database="sequrity"
        )

        cursor1 = conn.cursor()
        cursor1.execute("SELECT passwordd FROM pvalue")

        
        row = cursor1.fetchone()

        if row:
            
            if row[0] == loginvalue.get():
                 hider2.config(text='')
                 loginvalue.set('')
                 desclog.config(text="Access Granted! NOTE:- PLEASE DO NOT CLOSE THIS WINDOW TILL THE TIME YOU ARE USING THE APP!",
                                bg='#28b463',fg='white')   
                 login.iconify()

                # ========================new main window====================

                 def resize_image(image_path, size):  
                    with Image.open(image_path) as img:
                        img = img.resize(size)  
                        return ImageTk.PhotoImage(img)
                 
                 def update_time():
                    # Get the current date and time
                    now = datetime.now()
                    formatted_date_time = now.strftime("%A, %d %B %Y %I:%M:%S %p")
                    time_label.config(text=formatted_date_time)
                    win.after(1000, update_time)

                 def enable_text_selection(event):
                    # Re-enable the text widget for selection
                    data_display.config(state=NORMAL)
                    data_display.tag_add('sel', '1.0', END)  # Select all text
                    data_display.config(state=DISABLED)
                 
                 def fetch_and_print_data(columns, table_name):
                    global sqlp
                    # Replace with your actual database connection details
                    config = {
                        'user': 'root',
                        'password': sqlp,
                        'host': 'localhost',
                        'database': 'hms',
                    }

                    # Connect to MySQL database
                    conn = connect(**config)

                    # Create a cursor object
                    cursor = conn.cursor()

                    # Construct the query to select specific columns
                    column_string = ', '.join(columns)
                    query = f'SELECT {column_string} FROM {table_name};'

                    # Execute the query
                    cursor.execute(query)

                    # Fetch all rows from the executed query
                    rows = cursor.fetchall()

                    # Get column names
                    column_names = [i[0] for i in cursor.description]

                    # Print the data in tabular form
                    sql_data=tabulate(rows, headers=column_names, tablefmt='grid')
                    data_display.insert(END,sql_data)

                    # Close the cursor and connection
                    cursor.close()
                    conn.close()
                 
                 def checkindate(event=None):
                     def setter():
                         c_checkin.set(cal.get_date())
                    
                        #  print(cal.get_date())
                         datewin.destroy()
                        #  print(cal.get_date())
                     datewin=Toplevel(win)
                     datewin.geometry("200x250+100+100")
                     datewin.title("Checkin")
                     cal=DateEntry(datewin,selectmode='day',year=2024, month=9, day=16)
                     cal.place(x=0,y=0,height=20,width=200)
                     but=Button(datewin,text='Set',height=1,width=10,fg='#f4f6f6',font=('Bahnschrift',12,'bold'),bg='#148f77',
                                command=setter)
                     but.place(x=50,y=210)

                 def checkoutdate(event=None):
                     def setter2():
                         c_checkout.set(cal.get_date())
                        
                        #  print(cal.get_date())
                         datewin.destroy()
                        #  print(cal.get_date())
                     datewin=Toplevel(win)
                     datewin.geometry("200x250+100+100")
                     datewin.title("Checkout")
                     cal=DateEntry(datewin,selectmode='day')
                     cal.place(x=0,y=0,height=20,width=200)
                     but=Button(datewin,text='Set',height=1,width=10,fg='#f4f6f6',font=('Bahnschrift',12,'bold'),bg='#148f77',
                                command=setter2)
                     but.place(x=50,y=210)
                    
                 def dob():
                     def setter3():
                         c_av.set(cal.get_date())
                         print(cal.get_date())
                         datewin.destroy()
                        #  print(cal.get_date())
                     datewin=Toplevel(win)
                     datewin.geometry("200x250+100+100")
                     datewin.title("DOB Verification")
                     cal=DateEntry(datewin,selectmode='day')
                     cal.place(x=0,y=0,height=20,width=200)
                     but=Button(datewin,text='Set',height=1,width=10,fg='#f4f6f6',font=('Bahnschrift',12,'bold'),bg='#148f77',
                                command=setter3)
                     but.place(x=50,y=210)

                 

                 def ageverify():
                     def calculate_age(birth_date_str):
                        try:
                            # Convert the birth date string to a datetime object
                            birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
                            
                            # Get today's date
                            today = datetime.now()
                            
                            # Calculate age
                            age = today.year - birth_date.year
                            
                            # Adjust age if the birth date hasn't occurred yet this year
                            if (today.month, today.day) < (birth_date.month, birth_date.day):
                                age -= 1
                            
                            return age
                        except ValueError:
                            info_status.config(text="Wrong VALUE inserted in DOB Verification,Please Recheck!",bg='red')


                    # Example usage
                     birth_date_str = c_av.get()
                     if '-' in birth_date_str:
                        age = calculate_age(birth_date_str)
                        if age>=18:
                            
                            info_status.config(text="Customer age is Eligible!",bg='#148f77')
                        else:
                            info_status.config(text="Customer age is not Eligible!",bg='red')
                     else:
                         info_status.config(text="Date Format is wrong Please recheck!",bg='red')

                 def check_room_availability(room_sym, checkin_date, checkout_date):
                    global sqlp
                    # Connect to the MySQL database
                    conn = connect(
                        host="localhost",
                        user="root",
                        password=sqlp,
                        database="hms"
                    )
                    
                    cursor = conn.cursor()
                    
                    # Query to check availability
                    query = """
                    SELECT *
                    FROM rooms
                    WHERE room_sym = %s
                    AND (%s BETWEEN checkin AND checkout
                        OR %s BETWEEN checkin AND checkout
                        OR (checkin BETWEEN %s AND %s)
                        OR (checkout BETWEEN %s AND %s));
                    """
                    
                    # Execute the query with the provided parameters
                    cursor.execute(query, (room_sym, checkin_date, checkout_date, checkin_date, checkout_date, checkin_date, checkout_date))
                    
                    # Fetch the result
                    result = cursor.fetchall()
                    
                    if result:
                        mess="Not Found"
                    else:
                        mess="Found"
                    
                    # Close the connection
                    cursor.close()
                    conn.close()
                    return mess

                                     
                 
                 def insertdata():
                     global sqlp
                     ans=check_room_availability(c_roomno.get(), c_checkin.get(), c_checkout.get())
                     if ans=="Not Found":
                         messagebox.showerror("Pre-Booked", f"The room no:{c_roomno.get()} is pre-booked on the choosen dates!")
                     elif ans=="Found":   
                        global error
                        error=0
                        try:
                            c_phone1=int(c_phone.get())
                            error=error+0
                        except ValueError:
                            info_status.config(text="Phone Number is not correct,Please Recheck!",bg='red')
                            error=error+1

                        
                        try:
                            c_adult1=int(c_adult.get())
                            c_child1=int(c_child.get())
                            error=error+0
                        except ValueError:
                            info_status.config(text="Child or Adult Numbers is not correct,Please Recheck!",bg='red')
                            error=error+1
                        
                        try:
                            c_cost1=int(c_cost.get())
                            error=error+0
                        except  ValueError:
                            info_status.config(text="Cost Value is not correct,Please Recheck!",bg='red')
                            error=error+1

                        try:
                            c_name1=int(c_name.get())
                            c_state1=int(c_state.get())
                            c_dis1=int(c_dis.get())
                            c_roomtyp1=int(c_roomtyp.get())
                            info_status.config(text="Wrong Data input,Please Recheck!",bg='red')
                            error=error+1
                        except ValueError:
                            error=error+0
                            


                        file_path = 'cid.txt'

                        def read_file_as_int_list(file_path):
                            try:
                                with open(file_path, 'r') as file:
                                    lines = file.readlines()
                                return [int(line.strip()) for line in lines if line.strip().isdigit()]
                            except FileNotFoundError:
                                info_status.config(text="File error has occured! Contact developer.",bg='red')
                                error=error+1
                            except ValueError:
                                info_status.config(text="File error has occured! Contact developer.",bg='red')
                                error=error+1

                        def append_to_file(file_path, integer_to_append):
                            with open(file_path, 'a') as file:
                                file.write(f"{integer_to_append}\n")

                        while True:
                            cid=randint(1000,10000)

                            file_contents = read_file_as_int_list(file_path)
                            
                            if cid not in file_contents:
                                append_to_file(file_path, cid)
                                cid1=cid
                                break


                        try:
                            c_name1=c_name.get()
                            c_id1=c_id.get()
                            idvar1=idvar.get()
                            c_state1=c_state.get()
                            c_dis1=c_dis.get()
                            c_roomtyp1=c_roomtyp.get()
                            c_roomno1=c_roomno.get()
                            c_checkin1=c_checkin.get()
                            c_checkout1=c_checkout.get()
                        except error as e:
                            print("namnmenwn",e)


                        birth_date_str = c_av.get()
                        if '-' in birth_date_str:
                            birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
                            # Get today's date
                            today = datetime.now()

                            # Calculate age
                            age = today.year - birth_date.year

                            # Adjust age if the birth date hasn't occurred yet this year
                            if (today.month, today.day) < (birth_date.month, birth_date.day):
                                age -= 1
                            if age>=18:
                                
                                info_status.config(text="Customer age is Eligible!",bg='#148f77')
                                cav="yes"
                            else:
                                info_status.config(text="Customer age is not Eligible!",bg='red')
                                error=error+1
                        else:
                            info_status.config(text="Date Format is wrong Please recheck!",bg='red')
                            error=error+1

                        if error==0:
                            try:
                                # Establish a database connection
                                connection =connect(
                                    host='localhost',        # e.g., 'localhost' or IP address
                                    database='hms', # e.g., 'test_db'
                                    user='root',     # e.g., 'root'
                                    password=sqlp  # e.g., 'password123'
                                )

                                if connection.is_connected():
                                    cursor = connection.cursor()
                                    # Define the SQL query to insert data
                                    sql_insert_query = """
                                    INSERT INTO CUSTOMER (CUSTOMER_ID, CUSTOMER_NAME, PHONE,ID_TYP,ID_NO,STATE,DISTRICT,ADULTS,CHILD,CHECKIN,CHECKOUT,ROOM_NO,ROOM_TYP,COST,AGE_VERIFIED)
                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                    """
                                    # Data to be inserted
                                    # yyyy-mm-dd 
                                    data = (cid1, c_name1.title(), c_phone1, idvar1, c_id1,c_state1.title(),c_dis1.title(),c_adult1,c_child1,c_checkin1,c_checkout1,c_roomno1,c_roomtyp1,c_cost1,cav)
                                    # Execute the query
                                    cursor.execute(sql_insert_query, data)
                                    connection.commit()
                                    sql_update_query = """UPDATE rooms SET c_status = 'occupied' WHERE room_sym = %s"""
                                    cursor.execute(sql_update_query, (roomnoo.get(),))
                                    connection.commit() 

                                    query = """UPDATE rooms
                                    SET checkin = %s, checkout = %s
                                    WHERE ROOM_SYM = %s"""

                                    # Data to be updated
                                    data = (c_checkin1, c_checkout1, c_roomno1)
                                    cursor.execute(query, data)
                                    connection.commit()
                                    
                                    
                                    cursor.execute('''
                                    SELECT room_sym FROM rooms 
                                    WHERE c_status = 'Available' 
                                    ORDER BY room_no
                                    ''')
                                    results = cursor.fetchall()

                                    # Create a list to hold the available room symbols
                                    available_rooms = [row[0] for row in results]
                                    if available_rooms:
                                        option1=available_rooms
                                        roomnoo.config(values=option1)
                                        roomscount=str(len(available_rooms))
                                        count_label2.config(text=roomscount)
                                    else:
                                        info_status.config(text="No Available Rooms",bg='red')
                                
                                    info_status.config(text="Data inserted successfully!",bg='#148f77')
                                    data_display.delete("1.0",END)
                                    columns_to_select = ['SLNO','CUSTOMER_ID', 'CUSTOMER_NAME','PHONE','ID_NO','STATE','DISTRICT','ID_TYP','ADULTS','CHILD','checkin','checkout','ROOM_NO','ROOM_TYP','COST','AGE_VERIFIED','TIME','UPDATED']  # Replace with the columns you want to select
                                    table_name = 'customer'  # Replace with your actual table name

                                    fetch_and_print_data(columns_to_select, table_name)


                            except Error as e:
                                info_status.config(text=f"Error{e}",bg='red')
                            finally:
                                if connection.is_connected():
                                    cursor.close()
                                    connection.close()
                        else:
                            info_status.config(text="Some error has occured! Please Recheck.",bg='red')


                    

                 def clear():
                     nameentry.delete(0,END)
                     phoneentry.delete(0,END)
                     identry.delete(0,END)
                     identry.delete(0,END)
                     c_adult.set('1')
                     c_child.set('0')
                     checkinentry.delete(0,END)
                     checkoutentry.delete(0,END)
                     c_roomno.set('Select')
                     c_roomtyp.set('Select')
                     stateentry.delete(0,END)
                     distentry.delete(0,END)
                     ageentry.delete(0,END)
                     idvar.set(value='Aadhar')
                     costentry.delete(0,END)

                 def fetch_customer_data():
                    global sqlp
                    config = {
                    'user': 'root',
                    'password': sqlp,
                    'host': 'localhost',
                    'database': 'hms',
                    'raise_on_warnings': True}


                    customer_id=int(searchval.get())
                                           

                    # Create a connection to the MySQL database
                    try:
                        connection = connect(**config)
                        cursor = connection.cursor()
                        query = "SELECT * FROM customer WHERE customer_id = %s"
                        customer_id=int(searchval.get())
                        cursor.execute(query, (customer_id,))
                        
                        # Fetch column names
                        column_names = [desc[0] for desc in cursor.description]
                        
                        # Fetch the row data
                        row = cursor.fetchone()

                        
                          # Clear existing text

                        data_display.config(state=NORMAL)
                        data_display.delete(1.0, END)
                        
                        if row:
                            data_display.insert(END, "Customer Details:\n")
                            for i, (column_name, value) in enumerate(zip(column_names, row)):
                                data_display.insert(END, f"{column_name}: {value}\n")
                            
                            status_found=f"customer found with customer_id {customer_id}"
                            info_status.config(text=status_found,bg='#148f77')
                            

                        else:
                            status_error=f"No customer found with customer_id {customer_id}"
                            info_status.config(text=status_error,bg='red')


                    except Error as err:
                        status_error1=f"Error: {err}"
                        data_display.insert(END,status_error1)
                    
                    finally:
                        # Close the cursor and connection
                        if cursor:
                            cursor.close()
                        if connection:
                            connection.close()

                
                      # Replace with the actual customer_id you want to query
                    
                 def display_reset():
                    data_display.config(state=NORMAL)
                    data_display.delete(1.0,END)
                    columns_to_select = ['SLNO','CUSTOMER_ID', 'CUSTOMER_NAME','PHONE','ID_NO','STATE','DISTRICT','ID_TYP','ADULTS','CHILD','checkin','checkout','ROOM_NO','ROOM_TYP','COST','AGE_VERIFIED','TIME','UPDATED']  # Replace with the columns you want to select
                    table_name = 'customer'  # Replace with your actual table name

                    fetch_and_print_data(columns_to_select, table_name)     
                    show_data.set('Show')
                    info_status.config(text="Date reset successfully!",bg='#148f77')



                 def applydisplay():
                     global sqlp
                     conn = connect(
                     host='localhost',
                     user='root',
                     password=sqlp,
                     database='hms')
                 
                     cursor = conn.cursor()
                     today = datetime.now()
                    #  today = datetime.now()

                    # Calculate the start and end of the week
                     start_of_week = today - timedelta(days=today.weekday())
                     end_of_week = start_of_week + timedelta(days=6)

                    #  Calculate the start and end of the month
                     start_of_month = today.replace(day=1)
                     next_month = start_of_month.replace(day=28) + timedelta(days=4)  # this will get us to the next month
                     end_of_month = next_month - timedelta(days=next_month.day)

                     # Calculate the start and end of the year
                     start_of_year = today.replace(month=1, day=1)
                     end_of_year = today.replace(month=12, day=31)

                     # Function to print data in a tabular format
                     def print_table(title, data, column_names):
                        data_display.config(state=NORMAL)
                        data_display.delete(1.0,END)
                        # print(f"\n{title}")
                        s=tabulate(data, headers=column_names, tablefmt='grid')
                        data_display.insert(END,s)
                        apply_status="Changes applied successfully!"
                        info_status.config(text=apply_status,bg='#148f77')

                     if show_data.get()=='This week':
                         cursor.execute('''
                            SELECT * FROM customer
                            WHERE checkin BETWEEN %s AND %s
                         ''', (start_of_week.date(), end_of_week.date()))
                         weekly_data = cursor.fetchall()

                         column_names = [i[0] for i in cursor.description]  # Get column names
                         print_table("Data for the week", weekly_data, column_names)
                     elif show_data.get()=='This month':
                         cursor.execute('''
                            SELECT * FROM customer
                            WHERE checkin BETWEEN %s AND %s
                         ''', (start_of_month.date(), end_of_month.date()))
                         monthly_data = cursor.fetchall()
                         column_names = [i[0] for i in cursor.description]
                         print_table("Data for the month", monthly_data, column_names)
                     elif show_data.get()=='This year':
                            
                         # Query for the year
                            cursor.execute('''
                                SELECT * FROM customer
                                WHERE checkin BETWEEN %s AND %s
                            ''', (start_of_year.date(), end_of_year.date()))
                            yearly_data = cursor.fetchall()
                            column_names = [i[0] for i in cursor.description]
                            print_table("Data for the year", yearly_data, column_names)
                     elif show_data.get()=='All':
                         data_display.config(state=NORMAL)
                         data_display.delete(1.0,END)
                         columns_to_select = ['SLNO','CUSTOMER_ID', 'CUSTOMER_NAME','PHONE','ID_NO','STATE','DISTRICT','ID_TYP','ADULTS','CHILD','checkin','checkout','ROOM_NO','ROOM_TYP','COST','AGE_VERIFIED','TIME','UPDATED']  # Replace with the columns you want to select
                         table_name = 'customer'  # Replace with your actual table name
                         fetch_and_print_data(columns_to_select, table_name)
                     elif show_data.get()=='Today':
                         # Query for today
                        cursor.execute('''
                            SELECT * FROM customer
                            WHERE checkin = %s
                        ''', (today,))
                        today_data = cursor.fetchall()
                        column_names = [i[0] for i in cursor.description]  # Get column names
                        print_table("Data for today", today_data, column_names)

                     else:
                         option_error=f"No option with {show_data.get()}"
                         info_status.config(text=option_error,bg='red')

                        
                 def deldata():
                     global sqlp
                     try:
                        conn = connect(
                        host='localhost',
                        user='root',
                        password=sqlp,
                        database='hms')
                        if conn.is_connected():
                            cursor = conn.cursor()
                            idd=int(deleteentry.get())
                            
                            # Define the DELETE SQL query
                            delete_query = "DELETE FROM customer WHERE customer_id = %s"
                            
                            # Execute the query
                            cursor.execute(delete_query, (idd,))
                            
                            # Commit the transaction
                            conn.commit()
                            
                            del_info=f"Record with customer_id {idd} has been deleted."
                            info_status.config(text=del_info,bg='#148f77')
                            data_display.config(state=NORMAL)
                            data_display.delete(1.0,END)
                            columns_to_select = ['SLNO','CUSTOMER_ID', 'CUSTOMER_NAME','PHONE','ID_NO','STATE','DISTRICT','ID_TYP','ADULTS','CHILD','checkin','checkout','ROOM_NO','ROOM_TYP','COST','AGE_VERIFIED','TIME','UPDATED']  # Replace with the columns you want to select
                            table_name = 'customer'  # Replace with your actual table name

                            fetch_and_print_data(columns_to_select, table_name)
                            deleteentry.delete(0,END)
                            
                        
                     except Error:
                         status_error="Customer ID not found!"
                         info_status.config(text=status_error,bg='red')
                     finally:
                        # Close the cursor and connection
                        if cursor:
                            cursor.close()
                        if conn and conn.is_connected():
                            conn.close()
                         
                 def insert_rooms():
                        global sqlp
                        
                     # Connect to the MySQL database
                        try:
                            conn = connect(
                                host='localhost',       # Replace with your host
                                user='root',   # Replace with your MySQL username
                                password=sqlp,# Replace with your MySQL password
                                database='hms' # Replace with your database name
                            )
                            cursor = conn.cursor()

                            def insert_dataa(room_no, room_typ, room_sym, c_status):
                                try:
                                    # Check if the room already exists
                                    cursor.execute('SELECT COUNT(*) FROM rooms WHERE room_no = %s', (room_no,))
                                    count = cursor.fetchone()[0]

                                    if count > 0:
                                        info_status.config(text="Room Already Exist!.",bg='red')
                                    else:
                                        # Insert new room details
                                        cursor.execute('''
                                        INSERT INTO rooms (room_no, room_typ, room_sym, c_status) 
                                        VALUES (%s, %s, %s, %s)
                                        ''', (room_no, room_typ, room_sym, c_status))
                                        conn.commit()
                                        cursor.execute('SELECT COUNT(*) FROM rooms')
                                        total_rooms = cursor.fetchone()[0]
                                        count_label1.config(text=str(total_rooms))

                                        cursor.execute('''
                                        SELECT room_sym FROM rooms 
                                        WHERE c_status = 'Available' 
                                        ORDER BY room_no
                                        ''')
                                        results = cursor.fetchall()

                                        # Create a list to hold the available room symbols
                                        available_rooms = [row[0] for row in results]
                                        if available_rooms:
                                            option1=available_rooms
                                            roomnoo.config(values=option1)
                                            roomscount=str(len(available_rooms))
                                            count_label2.config(text=roomscount)

                                        else:
                                            info_status.config(text="No Available Rooms",bg='red')


                                        
                                        info_status.config(text="Room inserted successfully!",bg='#148f77')

                                except Error as err:
                                    e=f"Error: {err}"
                                    info_status.config(text=e,bg='red')

                            # Example usage

                            room_sym=addroomen.get()+selroomtyp.get()
                            insert_dataa(addroomen.get(), selroomtyp.get(), room_sym, 'Available')
                             # This should trigger the "Room already exists" message

                        except Error as err:
                            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                                info_status.config(text="Something is wrong with your Data.",bg='red')
                            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                                info_status.config(text="Database does not exist.",bg='red')
                            else:
                                info_status.config(text="Error.",bg='red')
                        finally:
                            # Close the database connection
                            if conn.is_connected():
                                cursor.close()
                                conn.close()


                 def del_rooms():
                        global sqlp
                     # Connect to the MySQL database
                        try:
                            conn =connect(
                                host='localhost',       # Replace with your host
                                user='root',   # Replace with your MySQL username
                                password=sqlp,# Replace with your MySQL password
                                database='hms' # Replace with your database name
                            )
                            cursor = conn.cursor()

                            def delete_room(room_no):
                                try:
                                    # Check if the room exists
                                    cursor.execute('SELECT COUNT(*) FROM rooms WHERE room_no = %s', (room_no,))
                                    count = cursor.fetchone()[0]

                                    if count == 0:         
                                        info_status.config(text="Room does not Exist.",bg='red')
                                    else:
                                        # Delete the room
                                        cursor.execute('DELETE FROM rooms WHERE room_no = %s', (room_no,))
                                        conn.commit()

                                        cursor.execute('SELECT COUNT(*) FROM rooms')
                                        total_rooms = cursor.fetchone()[0]
                                        count_label1.config(text=str(total_rooms))

                                        cursor.execute('''
                                        SELECT room_sym FROM rooms 
                                        WHERE c_status = 'Available' 
                                        ORDER BY room_no
                                        ''')
                                        results = cursor.fetchall()

                                        # Create a list to hold the available room symbols
                                        available_rooms = [row[0] for row in results]
                                        if available_rooms:
                                            option1=available_rooms
                                            roomnoo.config(values=option1)
                                            roomscount=str(len(available_rooms))
                                            count_label2.config(text=roomscount)
                                        else:
                                            info_status.config(text="No Available Rooms",bg='red')


                                        m=f"Deleted room number: {room_no}"
                                        info_status.config(text=m,bg='#148f77')

                                except Error as err:
                                    e=f"Error: {err}"
                                    info_status.config(text=e,bg='red')

                            # Example usage
                            delete_room(delroomen.get())  # Attempt to delete room '101'
                            

                        except Error as err:
                            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                                info_status.config(text="Something is wrong with your Data.",bg='red')
                            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                                info_status.config(text="Database does not exist.",bg='red')
                            else:
                                info_status.config(text="Error.",bg='red')
                        finally:
                            # Close the database connection
                            if conn.is_connected():
                                cursor.close()
                                conn.close()

                 def chkoutbtn():
                     global sqlp
                     cId=chkout.get()
                     def update_room_status(search_data):
                        try:
                            # Connect to the MySQL database
                            connection = connect(
                                host='localhost',        # e.g., 'localhost'
                                database='hms',# replace with your database name
                                user='root',    # replace with your MySQL username
                                password=sqlp  # replace with your MySQL password
                            )

                            if connection.is_connected():
                                cursor = connection.cursor(dictionary=True)

                                # Query to find the room
                                select_query = """
                                SELECT * FROM rooms 
                                WHERE (room_no = %s OR room_sym = %s) AND c_status = 'occupied'
                                """
                                cursor.execute(select_query, (search_data, search_data))
                                room_result = cursor.fetchone()

                                if room_result :
                                    # Update the c_status to 'available'
                                    update_query = """
                                    UPDATE rooms 
                                    SET c_status = 'available' 
                                    WHERE (room_no=%s OR room_sym=%s)
                                    """
                                    cursor.execute(update_query, (search_data, search_data),)  # Assuming 'id' is the primary key
                                    connection.commit()

                                    sql = "UPDATE rooms SET checkin = NULL WHERE (room_no = %s OR room_sym = %s)"
                                    cursor.execute(sql, (search_data,search_data))
                                    connection.commit()

                                    sql1 = "UPDATE rooms SET checkout = NULL WHERE (room_no = %s OR room_sym = %s)"
                                    cursor.execute(sql1, (search_data,search_data))
                                    connection.commit()

                                    info_status.config(text="Data found. Room updated:",bg='#148f77')


                                    cursor11=connection.cursor()
                                    cursor11.execute('''
                                    SELECT room_sym FROM rooms 
                                    WHERE c_status = 'Available' 
                                    ORDER BY room_no
                                    ''')
                                    results = cursor11.fetchall()

                                    # Create a list to hold the available room symbols
                                    available_rooms = [row[0] for row in results]
                                    if available_rooms:
                                        option1=available_rooms
                                        roomnoo.config(values=option1)
                                        roomscount=str(len(available_rooms))
                                        count_label2.config(text=roomscount)
                                    else:
                                        info_status.config(text="No Available Rooms",bg='red')
                                else:
                                    info_status.config(text="No matching data found or room is not occupied.",bg='red')

                        except Error as e:
                            m=f"Error: {e}"
                            info_status.config(text=m,bg='red')

                        finally:
                            try:
                                if connection.is_connected():
                                    cursor.close()
                                    cursor11.close()
                                    connection.close()
                            except UnboundLocalError:
                                pass

                     # Example usage
                     search_value = cId 
                     update_room_status(search_value)
                         
                                                                       
                 win=Toplevel(login)
                 win.geometry("1380x700+80+50")
                 win.title('Hotel Management System')
                 win.iconbitmap('hotel.ico')
                 win.config(bg='#ebf5fb')

                #  ====================== started to ctrate tab from here ==================
                 tabs=ttk.Notebook(win)
                 tabs.pack()
                 style = ttk.Style()
                 style.configure('TNotebook.Tab', font=('Bahnschrift',12,'bold'))

                #  =================== customer tab start from here ================================

                 cus_frame=Frame(tabs,bg='#e5e7e9',height=690,width=1380)
                 cus_frame.pack(fill='both',expand=1)
                 header_frame1=Frame(cus_frame,height=59,bg='#7fb3d5')
                 header_frame1.pack(fill=X,padx=2)
                 
                 
                 cus_label=Label(header_frame1,text='CUSTOMER',font=('Copperplate Gothic Bold',14),relief='groove',height=2,
                                 width=20,bd=5,bg='#f39c12',fg='white')
                 cus_label.place(x=2,y=2)

                 cus_path='customer.png'
                 cus_size=(30,30)
                 cus_img=resize_image(cus_path,cus_size)

                 cus_img_lab=Label(header_frame1,image=cus_img,bg='#f39c12')
                 cus_img_lab.place(x=50,y=8)
                 t_rooms=Label(header_frame1,text='Total Rooms',font=('Copperplate Gothic Bold',14),relief='groove',height=2,
                                 width=20,bd=5,bg='#2e86c1',fg='white',justify=LEFT)
                 t_rooms.place(x=320,y=2)

                 a_rooms=Label(header_frame1,text='Available Rooms',font=('Copperplate Gothic Bold',14),relief='groove',height=2,
                                 width=20,bd=5,bg='#2e86c1',fg='white')
                 a_rooms.place(x=635,y=2)


                 time_label=Label(header_frame1,text='',font=('Copperplate Gothic Bold',13),relief='groove',height=2,
                            width=34,bd=5,bg='#2e86c1',fg='white')
                 time_label.place(x=948,y=5)


                 update_time()

                 count_frame=Frame(cus_frame,height=40,bg='#e5e7e9',relief='flat')
                 count_frame.pack()

                 count_label1=Label(count_frame,text='0',font=('Copperplate Gothic Bold',14),relief='flat',bg='#e5e7e9')
                 count_label2=Label(count_frame,text='900',font=('Copperplate Gothic Bold',14),relief='flat',bg='#e5e7e9')
                 count_frame.columnconfigure([0, 1], weight=1)
                 count_frame.rowconfigure(0, weight=1)
                 count_label1.grid(row=0, column=0, sticky="ew",padx=60)
                 count_label2.grid(row=0, column=1, sticky="ew",padx=200)


                 info_frame=Frame(cus_frame,bg='#f4f6f6',width=500,height=550)
                 info_frame.place(x=1,y=100)

                 info_status=Label(info_frame,text='Fill the information of the customer.',font=('Bahnschrift',12,'bold'),
                                   bg='green',fg='white',height=1,width=55)
                 info_status.place(x=1,y=1)

                 namelabel=LabelFrame(info_frame,text='Customer Name',font=('Bahnschrift',12,'bold'),bg='#f4f6f6',fg='#148f77',bd=3,relief=SUNKEN)
                 namelabel.place(x=1,y=30,height=50,width=250)
                #  ==========================================================================
                 c_name=StringVar()
                 nameentry=Entry(info_frame,font=("Calibri (Body)",11,'bold'),bg='#f4f6f6',relief='flat',textvariable=c_name)
                 nameentry.place(x=5,y=51,width=240,height=25)
                #  ==========================================================================

                 phonelabel=LabelFrame(info_frame,text='Phone Number',font=('Bahnschrift',12,'bold'),bg='#f4f6f6',fg='#148f77',bd=3,relief=SUNKEN)
                 phonelabel.place(x=256,y=30,height=50,width=240)
                #  ==========================================================================
                 c_phone=StringVar()
                 phoneentry=Entry(info_frame,font=("Calibri (Body)",11,'bold'),bg='#f4f6f6',relief='flat',textvariable=c_phone)
                 phoneentry.place(x=260,y=51,width=231,height=25)
                #  ==========================================================================

                 idlabel=LabelFrame(info_frame,text='ID Proof',font=('Bahnschrift',12,'bold'),bg='#f4f6f6',fg='#148f77',bd=3,relief=SUNKEN)
                 idlabel.place(x=1,y=90,height=50,width=250)
                 #  ==========================================================================
                 c_id=StringVar()
                 identry=Entry(info_frame,font=("Calibri (Body)",11,'bold'),bg='#f4f6f6',relief='flat',textvariable=c_id)
                 identry.place(x=5,y=110,width=240,height=25)
                #  ==========================================================================

                #  ==========================================================================
                 idvar=StringVar(value='Aadhar')
                              
                 idtyp1=Radiobutton(info_frame,text='Aadhar',font=('Bahnschrift',10,'bold'),bg='#148f77',value='Aadhar',variable=idvar,cursor='hand2')
                 idtyp1.place(x=265,y=110)

                 idtyp2=Radiobutton(info_frame,text='DL',font=('Bahnschrift',10,'bold'),bg='#148f77',value='DL',variable=idvar,cursor='hand2')
                 idtyp2.place(x=350,y=110)

                 idtyp3=Radiobutton(info_frame,text='PAN',font=('Bahnschrift',10,'bold'),bg='#148f77',value='PAN',variable=idvar,cursor='hand2')
                 idtyp3.place(x=410,y=110)
                 #  ==========================================================================

                 

                 statelabel=LabelFrame(info_frame,text='State',font=('Bahnschrift',12,'bold'),bg='#f4f6f6',fg='#148f77',bd=3,relief=SUNKEN)
                 statelabel.place(x=1,y=150,height=50,width=250)
                 #  ==========================================================================
                 c_state=StringVar()
                 stateentry=Entry(info_frame,font=("Calibri (Body)",11,'bold'),bg='#f4f6f6',relief='flat',textvariable=c_state)
                 stateentry.place(x=5,y=168,width=240,height=25)
                 #  ==========================================================================

                 districtlabel=LabelFrame(info_frame,text='District',font=('Bahnschrift',12,'bold'),bg='#f4f6f6',fg='#148f77',bd=3,relief=SUNKEN)
                 districtlabel.place(x=256,y=150,height=50,width=244)
                 #  ==========================================================================
                 c_dis=StringVar()
                 distentry=Entry(info_frame,font=("Calibri (Body)",11,'bold'),bg='#f4f6f6',relief='flat',textvariable=c_dis)
                 distentry.place(x=260,y=168,width=231,height=25)
                 #  ==========================================================================

                 adultlabel=LabelFrame(info_frame,text='Adults',font=('Bahnschrift',12,'bold'),bg='#f4f6f6',fg='#148f77',bd=3,relief=SUNKEN)
                 adultlabel.place(x=1,y=210,height=50,width=200)
                 #  ==========================================================================
                 c_adult=StringVar()
                 adultspin=Spinbox(info_frame,from_=1,to=10,wrap=True,relief=FLAT,font=("Calibri (Body)",11,'bold'),bg='#f4f6f6',
                                   cursor='hand2',textvariable=c_adult)
                 adultspin.place(x=70,y=230,width=128,height=25)
                 #  ==========================================================================


                 childlabel=LabelFrame(info_frame,text='Child',font=('Bahnschrift',12,'bold'),bg='#f4f6f6',fg='#148f77',bd=3,relief=SUNKEN)
                 childlabel.place(x=205,y=210,height=50,width=200)
                 #  ==========================================================================
                 c_child=StringVar()
                 childspin=Spinbox(info_frame,from_=0,to=10,wrap=True,relief=FLAT,font=("Calibri (Body)",11,'bold'),bg='#f4f6f6',
                                   cursor='hand2',textvariable=c_child)
                 
                 childspin.place(x=270,y=230,width=128,height=25)
                 #  ==========================================================================

                 staylabel=LabelFrame(info_frame,text='Stay',font=('Bahnschrift',12,'bold'),bg='#f4f6f6',fg='#148f77',bd=3)
                 staylabel.place(x=1,y=270,height=120,width=450)

                 checkin=Label(info_frame,text='Check-In',font=('Bahnschrift',12,'bold'),bg='#f4f6f6')
                 checkin.place(x=25,y=300)
                 #  ==========================================================================
                 c_checkin=StringVar()
                 checkinentry=Entry(info_frame,font=("Calibri (Body)",11,'bold'),bg='#f4f6f6',relief='groove',bd=5,textvariable=c_checkin)
                 checkinentry.place(x=5,y=330,height=25,width=130)
                 checkinbutton=Button(info_frame,text='SELECT',font=('Bahnschrift',10,'bold'),bg='#148f77',fg='white',cursor='hand2',command=checkindate)
                 checkinbutton.place(x=35,y=360,height=20)
                 #  ==========================================================================
                 

                 checkout=Label(info_frame,text='Check-Out',font=('Bahnschrift',12,'bold'),bg='#f4f6f6')
                 checkout.place(x=185,y=300)
                 #  ==========================================================================
                 c_checkout=StringVar()
                 checkoutentry=Entry(info_frame,font=("Calibri (Body)",11,'bold'),bg='#f4f6f6',relief='groove',bd=5,textvariable=c_checkout)
                 checkoutentry.place(x=155,y=330,height=25,width=130)
                 checkoutbutton=Button(info_frame,text='SELECT',font=('Bahnschrift',10,'bold'),bg='#148f77',fg='white',cursor='hand2',command=checkoutdate)
                 checkoutbutton.place(x=195,y=360,height=20)
                 #  ==========================================================================

                 roomno=Label(info_frame,text='Room No.',bg='#f4f6f6',font=('Bahnschrift',12,'bold'))
                 roomno.place(x=350,y=300)
                 #  ==========================================================================

                 def situation1():
                    global sqlp
                    try:
                        conn =connect(
                            host='localhost',       # Replace with your host
                            user='root',   # Replace with your MySQL username
                            password=sqlp,# Replace with your MySQL password
                            database='hms' # Replace with your database name
                        )
                        cursor = conn.cursor()

                        # Query to select room_sym where c_status is 'Available', ordered by room_no
                        cursor.execute('''
                        SELECT room_sym FROM rooms 
                        WHERE c_status = 'Available' 
                        ORDER BY room_no
                        ''')
                        results = cursor.fetchall()

                        # Create a list to hold the available room symbols
                        available_rooms = [row[0] for row in results]

                        # Print the list of available rooms

                        cursor.execute('SELECT COUNT(*) FROM rooms')
                        total_rooms = cursor.fetchone()[0]
                        count_label1.config(text=str(total_rooms))

                        if available_rooms:
                            option1=available_rooms
                            roomscount=str(len(available_rooms))
                            count_label2.config(text=roomscount)


                        else:
                            option1=["No rooms Available!"]
                            info_status.config(text="No Available Rooms",bg='red')

                    except Error as err:
                        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                            print("Something is wrong with your username or password.")
                        elif err.errno == errorcode.ER_BAD_DB_ERROR:
                            print("Database does not exist.")
                        else:
                            print(err)
                    finally:
                        # Close the database connection
                        if conn.is_connected():
                            cursor.close()
                            conn.close()
                    
                    return option1

                 option1=situation1()
                #  situation2()
                #  option1=[100,101,102,103,104,105,106,107,108,109,110]

                 c_roomno=StringVar()
                 roomnoo=ttk.Combobox(info_frame,value=option1,font=("Calibri (Body)",11,'bold'),textvariable=c_roomno)
                 roomnoo.place(x=325,y=330,width=100)
                 roomnoo.set('Select')
                 #  ==========================================================================


                 roomtyplabel=LabelFrame(info_frame,text='Room Type',font=('Bahnschrift',12,'bold'),bg='#f4f6f6',fg='#148f77',bd=3)
                 roomtyplabel.place(x=1,y=400,height=50,width=200)
                 #  ==========================================================================

                 option2=['AC','NON-AC','Others']
                 c_roomtyp=StringVar()
                 roomtyp=ttk.Combobox(info_frame,value=option2,font=("Calibri (Body)",11,'bold'),textvariable=c_roomtyp)
                 roomtyp.place(x=5,y=420)
                 roomtyp.set('Select')
                 #  ==========================================================================

                 costlabel=LabelFrame(info_frame,text='Cost',font=('Bahnschrift',12,'bold'),bg='#f4f6f6',fg='#148f77',bd=3,relief=SUNKEN)
                 costlabel.place(x=205,y=400,height=50,width=200)
                 #  ==========================================================================
                 c_cost=StringVar()

                 costentry=Entry(info_frame,font=("Calibri (Body)",11,'bold'),bg='#f4f6f6',relief='flat',textvariable=c_cost)
                 costentry.place(x=210,y=420,height=25,width=160)
                 #  ==========================================================================

                 agelabel=LabelFrame(info_frame,text='Age Verification',font=('Bahnschrift',12,'bold'),bg='#f4f6f6',fg='#148f77',bd=3,relief=SUNKEN)
                 agelabel.place(x=1,y=458,height=50,width=200)
                 #  ==========================================================================
                 c_av=StringVar()
                 ageentry=Entry(info_frame,font=("Calibri (Body)",11,'bold'),bg='#f4f6f6',relief='flat',textvariable=c_av)
                 ageentry.place(x=5,y=480,height=25,width=180)
                 c_av.set("yyyy-mm-dd")
                 #  ==========================================================================
                 ageverbutton=Button(info_frame,text='Verify',font=('Bahnschrift',11,'bold'),bg='#148f77',fg='white',cursor='hand2',command=ageverify)
                 ageverbutton.place(x=300,y=472,height=30)

                 bookbutton=Button(info_frame,text='Book',font=('Bahnschrift',12,'bold'),bg='#148f77',fg='white',cursor='hand2',command=insertdata)
                 bookbutton.place(x=100,y=520,height=30,width=100)

                 clearbutton=Button(info_frame,text='Clear',font=('Bahnschrift',12,'bold'),bg='red',fg='white',cursor='hand2',command=clear)
                 clearbutton.place(x=300,y=520,height=30,width=100)

                 
                 data_frame=Frame(cus_frame,bg='blue',width=870,height=355)
                 data_frame.place(x=503,y=100)

                 operational_frame=Frame(data_frame,height=42,width=870,bg='#f4f6f6',relief='groove',bd='5')
                 operational_frame.place(x=0,y=0)
                 

                 searchbutt=Button(operational_frame,text='Search',bg='#f4f6f6',font=('Bahnschrift',12,'bold'),fg='#148f77',relief='flat',
                               cursor='hand2',command=fetch_customer_data)
                 searchbutt.place(x=1,y=3,height=17)

                 searchval=StringVar()

                 searchentry=Entry(operational_frame,font=("Calibri (Body)",11,'bold'),bg='#f4f6f6',textvariable=searchval)
                 searchentry.place(x=63,y=1,height=25,width=150)

                 resetbutt=Button(operational_frame,font=('Bahnschrift',12,'bold'),text="Reset",bg='#148f77',fg='white',cursor='hand2',command=display_reset)
                 resetbutt.place(x=240,y=3,width=100,height=25)

                 savebutt=Button(operational_frame,font=('Bahnschrift',12,'bold'),text='Save',bg='#148f77',fg='white',cursor='hand2')
                 savebutt.place(x=370,y=3,width=100,height=25)

                 printbutt=Button(operational_frame,font=('Bahnschrift',12,'bold'),text='Print',bg='Red',fg='white',cursor='hand2')
                 printbutt.place(x=500,y=3,width=100,height=25)

                 delete=Button(operational_frame,text='Delete',bg='#f4f6f6',font=('Bahnschrift',12,'bold'),fg='#148f77',relief='flat',
                               cursor='hand2',command=deldata)
                 delete.place(x=633,y=3,height=17)

                 deleteentry=Entry(operational_frame,font=("Calibri (Body)",11,'bold'),bg='#f4f6f6')
                 deleteentry.place(x=700,y=3,height=25,width=150)

                #  mydata=StringVar

                 data_display=Text(data_frame,height=18,width=106,bg='#f4f6f6',wrap='none')
                 data_display.place(x=1,y=43)
                #  data_display.insert(END,"THis is some selectable text")
                 columns_to_select = ['SLNO','CUSTOMER_ID', 'CUSTOMER_NAME','PHONE','ID_NO','STATE','DISTRICT','ID_TYP','ADULTS','CHILD','checkin','checkout','ROOM_NO','ROOM_TYP','COST','AGE_VERIFIED','TIME','UPDATED']  # Replace with the columns you want to select
                 table_name = 'customer'  # Replace with your actual table name

                 fetch_and_print_data(columns_to_select, table_name)
                 
                 data_display.bind('<Button-1>', enable_text_selection)
                 scrollbary=Scrollbar(data_frame,orient='vertical',command=data_display.yview,bg='#148f77')
                 scrollbary.place(x=854,y=44,height=307,width=15)
                 data_display['yscrollcommand']=scrollbary.set

                 scrollbarx=Scrollbar(data_frame,orient='horizontal',command=data_display.xview,bg='#148f77')
                 scrollbarx.place(x=1,y=337,height=16,width=850)
                 data_display['xscrollcommand']=scrollbarx.set





                 
                 update_frame=Frame(cus_frame,width=870,height=197,bd=3,bg='#f4f6f6')
                 update_frame.place(x=503,y=457)  

                 modifylf=LabelFrame(update_frame,text="Modification Area",bg='#f4f6f6',bd='3',font=('Bahnschrift',12,'bold'),fg='#148f77',relief=SUNKEN)     
                 modifylf.place(x=5,y=3,height=183,width=350) 

                 option3=['All','Today','This week','This month','This Year']

                 show_data=ttk.Combobox(update_frame,value=option3,font=("Calibri (Body)",11,'bold'))
                 show_data.place(x=13,y=28)
                 show_data.set('Show')

                 applybutt=Button(update_frame,font=('Bahnschrift',12,'bold'),text='Apply',bg='#148f77',fg='white',cursor='hand2',
                                  command=applydisplay)
                 applybutt.place(x=220,y=28,width=100,height=25)

                 option4=['All','Customer Name','Phone','ID proof','Checkin','Checkout','Room Type','Room No']

                 modify_data=ttk.Combobox(update_frame,value=option4,font=("Calibri (Body)",11,'bold'))
                 modify_data.place(x=13,y=60)
                 modify_data.set('Modify')
                 proceedbutt=Button(update_frame,font=('Bahnschrift',12,'bold'),text='Proceed',bg='#148f77',fg='white',cursor='hand2')
                 proceedbutt.place(x=220,y=60,width=100,height=25)

                 checkoutlabel=Label(update_frame,text="Enter room no.(ONLY DIGITS) or Customer ID:",bg='#f4f6f6',bd='3',font=('Bahnschrift',12,'bold'),fg='#148f77')
                 checkoutlabel.place(x=13,y=90)

                 chkout=StringVar()

                 checkoutentry2=Entry(update_frame,font=("Calibri (Body)",11,'bold'),bg='#f4f6f6',textvariable=chkout)
                 checkoutentry2.place(x=13,y=130)

                 checkoutbutton2=Button(update_frame,font=('Bahnschrift',12,'bold'),text='Checkout',bg='#148f77',fg='white',cursor='hand2',
                                        command=chkoutbtn)
                 checkoutbutton2.place(x=220,y=130,width=100,height=25)



                
                 add_rooms=LabelFrame(update_frame,text="Add Rooms",bg='#f4f6f6',bd='3',font=('Bahnschrift',12,'bold'),fg='#148f77',relief=SUNKEN)
                 add_rooms.place(x=360,y=3,height=183,width=250)
                 
                 roomlabel=Label(update_frame,text="Enter room no.:",bg='#f4f6f6',bd='3',font=('Bahnschrift',12,'bold'),fg='#148f77')
                 roomlabel.place(x=365,y=28)
                 addroomen=StringVar()
                 roomlabelentry=Entry(update_frame,font=("Calibri (Body)",11,'bold'),bg='#f4f6f6',textvariable=addroomen)
                 roomlabelentry.place(x=490,y=35,height=20,width=100)
                 selroomtyp=StringVar()
                 roomtype=Label(update_frame,text="Select room type:",bg='#f4f6f6',bd='3',font=('Bahnschrift',12,'bold'),fg='#148f77')
                 roomtype.place(x=365, y=65)
                 option2=['AC','NON-AC','Others'] 
                 roomtypee=ttk.Combobox(update_frame,value=option2,font=("Calibri (Body)",11,'bold'),textvariable=selroomtyp)
                 roomtypee.place(x=500,y=70,width=100)
                 roomtypee.set('Select')
                 addrooms=Button(update_frame,font=('Bahnschrift',12,'bold'),text='Add',bg='#148f77',fg='white',cursor='hand2',command=insert_rooms)
                 addrooms.place(x=450,y=110,width=100)

                 delroom=LabelFrame(update_frame,text="Delete Rooms",bg='#f4f6f6',bd='3',font=('Bahnschrift',12,'bold'),fg='#148f77',relief=SUNKEN)
                 delroom.place(x=615,y=3,height=183,width=250)

                 delroomlabel=Label(update_frame,text="Enter room no.:",bg='#f4f6f6',bd='3',font=('Bahnschrift',12,'bold'),fg='#148f77')
                 delroomlabel.place(x=625,y=28)
                 delroomen=StringVar()
                 delroomlabelentry=Entry(update_frame,font=("Calibri (Body)",11,'bold'),bg='#f4f6f6',textvariable=delroomen)
                 delroomlabelentry.place(x=750,y=35,height=20,width=100)
                 delrooms=Button(update_frame,font=('Bahnschrift',12,'bold'),text='Delete',bg='#148f77',fg='white',cursor='hand2',command=del_rooms)
                 delrooms.place(x=675,y=110,width=100)







                #  =======================room availability and booking starts from here ==================

                 def arooms():
                    availbtn.place_forget()
                    availcombo.place(x=335,y=257)
                    def fetch_rooms(checkin_date, checkout_date):
                        global avaiopt, sqlp
                        avaiopt.clear()
                        try:
                            # Establish a connection to the database
                            connection =connect(
                                host='localhost',         # Replace with your MySQL host
                                user='root',         # Replace with your MySQL username
                                password=sqlp, # Replace with your MySQL password
                                database='hms'  # Replace with your database name
                            )

                            if connection.is_connected():

                                # Prepare the SQL query
                                query = """
                                SELECT room_sym
                                FROM rooms
                                WHERE (
                                    checkin IS NULL 
                                    and checkout IS NULL 
                                    OR NOT (
                                        (checkin BETWEEN %s AND %s) 
                                        OR (checkout BETWEEN %s AND %s)
                                        OR (%s BETWEEN checkin AND checkout)
                                        OR (%s BETWEEN checkin AND checkout)
                                    )
                                )
                                """

                                # Execute the query with parameters
                                cursor = connection.cursor()
                                cursor.execute(query, (checkin_date, checkout_date, checkin_date, checkout_date, checkin_date, checkout_date))

                                # Fetch the results
                                rooms = cursor.fetchall()

                                # Check if there are any rooms available
                                if rooms:
                                    for room in rooms:
                                        avaiopt.append(room[0]) # Printing the room_sym
                                else:
                                    avaiopt.append("No rooms available")

                        except Error as e:
                            messagebox.showerror("Database Error",f"Connection Error:{e}")

                        finally:
                            if connection.is_connected():
                                cursor.close()
                                connection.close()

                    # Example usage
                    checkin = c_cin.get()    # Replace with the desired check-in date
                    checkout = c_cout.get()   # Replace with the desired checkout date
                    fetch_rooms(checkin, checkout)
                    availcombo.config(value=avaiopt)


                 def cindate(event=None):
                     def setter1():
                         c_cin.set(cal.get_date())
                    
                        #  print(cal.get_date())
                         datewin.destroy()
                        #  print(cal.get_date())
                     datewin=Toplevel(win)
                     datewin.geometry("200x250+100+100")
                     datewin.title("Checkin")
                     cal=DateEntry(datewin,selectmode='day',year=2024, month=9, day=16)
                     cal.place(x=0,y=0,height=20,width=200)
                     but=Button(datewin,text='Set',height=1,width=10,fg='#f4f6f6',font=('Bahnschrift',12,'bold'),bg='#148f77',
                                command=setter1)
                     but.place(x=50,y=210)

                 def coutdate(event=None):
                     def setter3():
                         c_cout.set(cal.get_date())
                        
                        #  print(cal.get_date())
                         datewin.destroy()
                        #  print(cal.get_date())
                     datewin=Toplevel(win)
                     datewin.geometry("200x250+100+100")
                     datewin.title("Checkout")
                     cal=DateEntry(datewin,selectmode='day')
                     cal.place(x=0,y=0,height=20,width=200)
                     but=Button(datewin,text='Set',height=1,width=10,fg='#f4f6f6',font=('Bahnschrift',12,'bold'),bg='#148f77',
                                command=setter3)
                     but.place(x=50,y=210)
                
                 def fetch_data():
                    global sqlp
                    advbkdisplay.config(state=NORMAL)
                    try:
                        # Connect to MySQL database
                        conn = connect(
                            host='localhost',
                            user='root',
                            password=sqlp,
                            database='hms'
                        )
                        
                        # Create a cursor to interact with the database
                        cursor = conn.cursor()

                        # Define the query to fetch data from the table
                        query = "SELECT * FROM advbk"

                        # Execute the query
                        cursor.execute(query)

                        # Fetch column names and rows
                        columns = [desc[0] for desc in cursor.description]
                        rows = cursor.fetchall()

                        # Clear the text widget before inserting new data
                        advbkdisplay.delete(1.0, END)

                        # Using tabulate to format the data
                        table = tabulate(rows, headers=columns, tablefmt='grid')

                        # Insert the formatted table into the text widget
                        advbkdisplay.insert(END, table)

                    except Error as err:
                        messagebox.showerror("Datbase Error ",f"error:{err}")
                    finally:
                        # Close the cursor and connection
                        cursor.close()
                        conn.close()
                        advbkdisplay.config(state=DISABLED)

                 def insert_checkin_checkout(room_sym, checkin_date, checkout_date):
                    global sqlp
                    try:
                        # Establish the connection to the database
                        connection = connect(
                            host='localhost',        # Replace with your host (e.g., 'localhost')
                            user='root',    # Replace with your MySQL username
                            password=sqlp,  # Replace with your MySQL password
                            database='hms'  # Replace with your database name
                        )

                        if connection.is_connected():
                            cursor = connection.cursor()

                            # Check if a record with the given room_sym exists
                            check_query = "SELECT * FROM rooms WHERE room_sym = %s"
                            cursor.execute(check_query, (room_sym,))
                            existing_record = cursor.fetchone()

                            if existing_record:
                                # Update existing record with new checkin and checkout dates
                                update_query = """
                                UPDATE rooms
                                SET checkin = %s, checkout = %s
                                WHERE room_sym = %s
                                """
                                cursor.execute(update_query, (checkin_date, checkout_date, room_sym))
                            else:
                                messagebox.showerror("Room Error",f"Room not available:{room_sym}")

                            # Commit the transaction
                            connection.commit()
                            

                    except Error as e:
                        print(f"Error occurred: {e}")

                    finally:
                        if connection.is_connected():
                            cursor.close()
                            connection.close()
                         


                 def advbk():
                     global sqlp
                     if len(aname.get())==0 or len(aphn.get())==0 or len(astate.get())==0 or len(acst.get())==0 or len(a_adult.get())==0 :
                        pass
                     else:
                         def insert_data_to_mysql(col1_data, col2_data, col3_data, col4_data, col5_data, col6_data, col7_data, col8_data,col9_data):
                            try:
                                connection = connect(
                                    host='localhost',  
                                    user='root',       
                                    password=sqlp,
                                    database='hms' 
                                )

                                if connection.is_connected():
                              

                                    # Create a cursor object using the connection
                                    cursor = connection.cursor()

                                    # SQL Insert query
                                    insert_query = """
                                    INSERT INTO advbk (CUSTOMER_NAME, PHONE, STATE, ADULTS, CHILD, checkin, checkout, ROOM_NO,COST)
                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
                                    """

                                    # Data to be inserted into the table
                                    data_tuple = (col1_data, col2_data, col3_data, col4_data, col5_data, col6_data, col7_data, col8_data,col9_data)

                                    # Execute the insert query
                                    cursor.execute(insert_query, data_tuple)

                                    # Commit the transaction
                                    connection.commit()
                                    

                            except Error as e:
                                messagebox.showerror("Database error",f"Error occurred: {e}")

                            finally:
                                # Closing the cursor and connection
                                if connection.is_connected():
                                    cursor.close()
                                    connection.close()
                             

                        # Example usage: 
                        # Data for 8 columns
                         try:
                            col1_data = aname.get().title()
                            col2_data = int(aphn.get())
                            col3_data = astate.get().title()
                            col4_data = int(a_adult.get())
                            col5_data = int(a_child.get())
                            col6_data = c_cin.get()
                            col7_data = c_cout.get()
                            col8_data = rval.get()
                            col9_data= int(acst.get())

                            insert_data_to_mysql(col1_data, col2_data, col3_data, col4_data, col5_data, col6_data, col7_data, col8_data,col9_data)
                            fetch_data()
                            insert_checkin_checkout( rval.get(), c_cin.get(), c_cout.get())
                            availbtn.place(x=335,y=257)
                            availcombo.place_forget()
                         except ValueError:
                             messagebox.showerror("Wrong Input","You must fill the valid credential!")

                 def clr():
                    aname.set("")
                    aphn.set('')
                    astate.set('')
                    a_adult.set('1')
                    a_child.set('0')
                    acst.set('')
                    c_cin.set('')
                    c_cout.set('')
                    availbtn.place(x=335,y=257)
                    availcombo.place_forget()



                    

                 
                 room_frame=Frame(tabs,bg='#e5e7e9',height=690,width=1380)
                 room_frame.pack(fill='both',expand=1)

                 header_frame2=Frame(room_frame,height=50)
                 header_frame2.pack(fill=X,padx=2)
                 
                 
                 room_label=Label(header_frame2,text='Room Availability & Booking',font=('Copperplate Gothic Bold',14),relief='groove',height=2,
                                 width=35,bd=5,bg='#f39c12',fg='white')
                 room_label.place(x=2,y=2)

                 room_path='booking.png'
                 room_size=(30,30)
                 room_img=resize_image(room_path,room_size)

                 room_img_lab=Label(header_frame2,image=room_img,bg='#f39c12')
                 room_img_lab.place(x=50,y=8)

                 aframe=Frame(room_frame,bg='#a9cce3',relief='sunken',bd=5)
                 aframe.place(x=5,y=57,height=410,width=540)

                 nlabel=Label(aframe,text="Name:",font=('Bahnschrift',12,'bold'),bg="#a9cce3",fg="#154360")
                 nlabel.place(x=5,y=5)
                 aname=StringVar()
                 nentry=Entry(aframe,relief='sunken',width=35,font=("Calibri (Body)",11),textvariable=aname)
                 nentry.place(x=60,y=8)

                 plabel=Label(aframe,text="Phone:",font=('Bahnschrift',12,'bold'),bg="#a9cce3",fg="#154360")
                 plabel.place(x=5,y=50)
                 aphn=StringVar()
                 pentry=Entry(aframe,relief='sunken',width=20,font=("Calibri (Body)",11),textvariable=aphn)
                 pentry.place(x=60,y=53)

                 slabel=Label(aframe,text="State:",font=('Bahnschrift',12,'bold'),bg="#a9cce3",fg="#154360")
                 slabel.place(x=230,y=50)

                 astate=StringVar()

                 sentry=Entry(aframe,relief='sunken',width=25,font=("Calibri (Body)",11),textvariable=astate)
                 sentry.place(x=287,y=53)

                 alabel=Label(aframe,text='Adults:',font=('Bahnschrift',12,'bold'),bg="#a9cce3",fg="#154360")
                 alabel.place(x=5,y=95)
            
                 a_adult=StringVar()
                 aspin=Spinbox(aframe,from_=1,to=10,wrap=True,relief=FLAT,font=("Calibri (Body)",11,'bold'),bg='#f4f6f6',
                                   cursor='hand2',textvariable=a_adult)
                 aspin.place(x=60,y=98,width=128,height=25)
            


                 clabel=Label(aframe,text='Child:',font=('Bahnschrift',12,'bold'),bg="#a9cce3",fg="#154360")
                 clabel.place(x=210,y=95)
       
                 a_child=StringVar()
                 cspin=Spinbox(aframe,from_=0,to=10,wrap=True,relief=FLAT,font=("Calibri (Body)",11,'bold'),bg='#f4f6f6',
                                   cursor='hand2',textvariable=a_child)
                 
                 cspin.place(x=265,y=98,width=128,height=25)

                 rlabel=Label(aframe,text="Cost:",font=('Bahnschrift',12,'bold'),bg="#a9cce3",fg="#154360")
                 rlabel.place(x=5,y=140)

                 acst=StringVar()

                 rentry=Entry(aframe,relief='sunken',width=15,font=("Calibri (Body)",11),textvariable=acst)
                 rentry.place(x=55,y=143)

                 avail=LabelFrame(aframe,text="Room Availability",font=('Bahnschrift',12,'bold'),bg="#a9cce3",fg="#154360")
                 avail.place(x=5,y=195,height=140,width=521)

                 cin=Label(aframe,text='Check-In',font=('Bahnschrift',12,'bold'),bg="#a9cce3",fg="#154360")
                 cin.place(x=45,y=230)
                 #  ==========================================================================
                 c_cin=StringVar()
                 cinentry=Entry(aframe,font=("Calibri (Body)",11,'bold'),bg='#f4f6f6',relief='groove',bd=5,textvariable=c_cin)
                 cinentry.place(x=25,y=260,height=25,width=130)
                 cinbutton=Button(aframe,text='SELECT',font=('Bahnschrift',10,'bold'),bg='#154360',fg='white',cursor='hand2',command=cindate)
                 cinbutton.place(x=55,y=290,height=20)
                 #  ==========================================================================
                 

                 cout=Label(aframe,text='Check-Out',font=('Bahnschrift',12,'bold'),bg="#a9cce3",fg="#154360")
                 cout.place(x=205,y=230)
                 #  ==========================================================================
                 c_cout=StringVar()
                 coutentry=Entry(aframe,font=("Calibri (Body)",11,'bold'),bg='#f4f6f6',relief='groove',bd=5,textvariable=c_cout)
                 coutentry.place(x=175,y=260,height=25,width=130)
                 coutbutton=Button(aframe,text='SELECT',font=('Bahnschrift',10,'bold'),bg='#154360',fg='white',cursor='hand2',command=coutdate)
                 coutbutton.place(x=215,y=290,height=20)

                 availbtn=Button(aframe,text="Show available Rooms",font=('Bahnschrift',10,'bold'),bg='#154360',fg='white',
                 cursor='hand2',command=arooms)
                 availbtn.place(x=335,y=257,height=25)

                 rval=StringVar()

                 availcombo=ttk.Combobox(aframe,value=avaiopt,font=("Calibri (Body)",11,'bold'),textvariable=rval)
                 rval.set(value='Available Rooms')

                 bbtn=Button(aframe,text="Book",font=('Bahnschrift',10,'bold'),bg='#154360',fg='white',
                             cursor='hand2',command=advbk)
                 bbtn.place(x=150,y=350,height=25,width=80)

                 cbtn=Button(aframe,text="Clear",font=('Bahnschrift',10,'bold'),bg='#c0392b',fg='white',
                 cursor='hand2',command=clr)
                 cbtn.place(x=250,y=350,height=25,width=80)

                 bframe=Frame(room_frame,bg='#a9cce3',relief='sunken',bd=5)
                 bframe.place(x=545,y=57,height=410,width=830)

                 advbkdisplay=Text(bframe,wrap='none',state=DISABLED)
                 advbkdisplay.place(x=3,y=3,height=387,width=807)

                 ascrollbary=Scrollbar(bframe,orient='vertical',command=advbkdisplay.yview,bg='#148f77')
                 ascrollbary.place(x=807,y=3,height=387,width=10)
                 advbkdisplay['yscrollcommand']=ascrollbary.set

                 ascrollbarx=Scrollbar(bframe,orient='horizontal',command=advbkdisplay.xview,bg='#148f77')
                 ascrollbarx.place(x=3,y=387,height=10,width=800)
                 advbkdisplay['xscrollcommand']=ascrollbarx.set

                 fetch_data()


                #  ===================Dining starts from here ========================

                 

                 def clearr():
                     displayord.delete('1.0',END)

                 
                 def addf():
                     global bildict
                     try:
                        
                        format=f"{(fordered.get()).title()}, foodtyp:{ftyp.get()},COST:{float(fcost.get())},{quantity.get()},QNT:{quant.get()}\n"
                        displayord.insert(END,format)
                        bildict[float(fcost.get())]=float(quant.get())
                        status_bar.config(text="Ordered Added!",bg="#148f77")
                     except ValueError:
                         status_bar.config(text="Wrong Value Given!",bg="red")

                 def rest():
                     cus_entry.delete(0,END)
                     chooser.set(value='Stayer')
                     fordered.set(value="Select the Ordered food")
                     cost_entry.delete(0,END)
                     ftyp.set(value='Food Type')
                     quantity.set(value='Full')
                     quant.set(1)
                
                 def insertt():
                     global foodopt2
                     host = 'localhost'
                     user = 'root'
                     database = 'hms'
                     if ftyp.get()!='Food Type':
                        def get_starter_foods(valll):
                            global sqlp
                            # Establish the connection
                            try:
                                conn = connect(
                                    host=host,
                                    user=user,
                                    password=sqlp,
                                    database=database
                                )
                                


                                # Create a cursor object to execute SQL queries
                                cursor = conn.cursor()

                                # SQL query to select the food items where food_type = 'starter'
                                query = f"SELECT food FROM dining WHERE food_typ = '{valll}'"

                                # Execute the query
                                cursor.execute(query)

                                # Fetch all the rows from the query result
                                result = cursor.fetchall()

                                # If no items are found, return a list with "Not available"
                                if not result:
                                    return ["Not available"]

                                # Extract the food items into a list
                                food_list = [row[0] for row in result]  # Extract the first column (food)

                                # Sort the list in alphabetical order
                                food_list_sorted = sorted(food_list)

                                return food_list_sorted

                            except Error as err:
                                print(f"Error: {err}")
                                return None
                            
                            finally:
                                # Close the cursor and connection
                                if conn.is_connected():
                                    cursor.close()
                                    conn.close()
        
                        starter_foods = get_starter_foods(ftyp.get())
                        foodopt2=starter_foods
                        foodbox.config(value=foodopt2)

                    
                     else:
                         pass

                            
                 dining_frame=Frame(tabs,bg='#7d3c98',height=690,width=1380)
                 dining_frame.pack(fill='both',expand=1)

                 header_frame3=Frame(dining_frame,height=50,bg="#CCCCFF")
                 header_frame3.pack(fill=X,padx=2)
                 
                 
                 din_label=Label(header_frame3,text='Dining',font=('Copperplate Gothic Bold',14),relief='groove',height=2,
                                 width=20,bd=5,bg='#f39c12',fg='white')
                 din_label.place(x=2,y=2)

                #  ====================================== order area =========================

                 orders_frame=Frame(dining_frame,relief=SUNKEN,bd=3,bg="#CCCCFF")
                 orders_frame.place(x=2,y=52,height=350,width=900)

                 status_bar=Label(orders_frame,text="Fill the information below.",font=('Bahnschrift',12,'bold'),
                                  bg='green',fg='white')
                 status_bar.pack(fill=X)

                 cus_order=LabelFrame(orders_frame,text="Customer Order",font=('Bahnschrift',12,'bold'),fg='#148f77',bg="#CCCCFF")
                 cus_order.place(x=1,y=30,height=310,width=889)

                 cus_name=Label(orders_frame,text="Customer Name:",font=('Bahnschrift',12,'bold'),fg='#148f77',bg="#CCCCFF")
                 cus_name.place(x=5,y=80)

                 cname=StringVar()

                 cus_entry=Entry(orders_frame,font=("Calibri (Body)",11),textvariable=cname,relief="sunken",bd=1)
                 cus_entry.place(x=140,y=80,height=25,width=200)

                 chooser=StringVar(value='Stayer')

                 stayer=Radiobutton(orders_frame,text="Stayer",font=('Bahnschrift',12),value='Stayer',variable=chooser,
                                    bg="#148f77",relief=RAISED)
                 stayer.place(x=350,y=80)
                 nstayer=Radiobutton(orders_frame,text="Non-Stayer",font=('Bahnschrift',12),value='Non-Stayer',variable=chooser,
                                     bg="#148f77",relief=RAISED)
                 nstayer.place(x=450,y=80)

                 foodopt=['Starter','Main Course','Dessert','Others']
                 ftyp=StringVar()

                 foodtyp=ttk.Combobox(orders_frame,values=foodopt,font=('Bahnschrift',12),textvariable=ftyp)
                 foodtyp.place(x=5,y=130,width=150)

                 foodtyp.set('Food Type')

                 fapplybtn=Button(orders_frame,text="Apply",font=('Bahnschrift',12),bg="#148f77",fg="white",command=insertt)
                 fapplybtn.place(x=170,y=130,height=25,width=100)

                 fordered=StringVar()
                 foodbox=ttk.Combobox(orders_frame,values=foodopt2,font=('Bahnschrift',12),textvariable=fordered)
                 foodbox.place(x=280,y=130,height=25,width=280)
                 fordered.set(value="Select the Ordered food")

                 cost=Label(orders_frame,text='Cost:',font=('Bahnschrift',12),fg="#148f77",bg="#CCCCFF")
                 cost.place(x=5,y=180)

                 fcost=StringVar()
                 cost_entry=Entry(orders_frame,font=("Calibri (Body)",11),textvariable=fcost,relief="sunken",bd=1)
                 cost_entry.place(x=70,y=180,height=25,width=100)

                 quantity=StringVar(value='Full')

                 full=Radiobutton(orders_frame,text="Full",font=('Bahnschrift',12),value='Full',variable=quantity,
                                    bg="#148f77",relief=RAISED)
                 full.place(x=230,y=180)
                 half=Radiobutton(orders_frame,text="Half",font=('Bahnschrift',12),value='Half',variable=quantity,
                                     bg="#148f77",relief=RAISED)
                 half.place(x=300,y=180)

                 quantity2=Label(orders_frame,text="Quantity:",font=('Bahnschrift',12),fg="#148f77",bg="#CCCCFF")
                 quantity2.place(x=375,y=180)

                 quant=IntVar()

                 quantnum=Spinbox(orders_frame,from_=1,to=500,textvariable=quant)
                 quantnum.place(x=450,y=185,width=100)
                
                 orderbtn=Button(orders_frame,text="Add",font=('Bahnschrift',12),bg="#148f77",fg="white",command=addf)
                 orderbtn.place(x=350,y=230,height=25,width=100)

                 resetbtn=Button(orders_frame,text="Reset",font=('Bahnschrift',12),bg="Red",fg="white",command=rest)
                 resetbtn.place(x=460,y=230,height=25,width=100)

                 displayord=Text(orders_frame,relief='sunken')
                 displayord.place(x=570,y=50,height=250,width=300)

                 displayscroll=Scrollbar(orders_frame,orient='vertical',command=displayord.yview)
                 displayscroll.place(x=870,y=50,height=250,width=15)
                 displayord['yscrollcommand']=displayscroll.set

                 dclear=Button(orders_frame,text="Clear",font=('Bahnschrift',12),bg="red",fg="white",command=clearr)
                 dclear.place(x=780,y=310,height=25,width=100)



                 #  ====================================== billing area =========================

                 def save_file():
                    global l
                    # Get the file name from the entry widget
                    try:
                        file_name = l[-1]
                    except IndexError:
                        pass
                    
                    try:
                        if not file_name:
                            messagebox.showerror("Error", "Please provide a file name.")
                            return

                        # Ask the user to select a folder to save the file
                        folder_path = "C:\\Users\kumkum\\Desktop\\Hotel management system\\cinfo"

                        # If the user cancels the folder selection, return
                        if not folder_path:
                            messagebox.showerror("Error", "No folder selected.")
                            return

                        # Construct the full path to save the file
                        file_path = f"{folder_path}/{file_name}.txt"

                        # Get the content of the Text widget
                        text_data = biltext.get("1.0", END)

                        # Save the content to the specified file
                        try:
                            with open(file_path, 'w') as file:
                                file.write(text_data)
                            messagebox.showinfo("Success", f"File saved as {file_path}")
                        except Exception as e:
                            messagebox.showerror("Error", f"Failed to save file: {e}")
                    except UnboundLocalError:
                        pass

                
                 def bilclearr():
                     biltext.config(state=NORMAL)
                     biltext.delete("1.0",END)
                     biltext.config(state=DISABLED)
                
                 def search_file():

                    biltext.config(state=NORMAL)
                    # Get the filename from the entry widget (without the extension)
                    filename = bentry.get()
                    folder_path = "C:\\Users\\kumkum\\Desktop\\Hotel management system\\cinfo"

                    # Append the .txt extension to the filename
                    file_path = os.path.join(folder_path, f"{filename}.txt")

                    # Check if the file exists
                    if os.path.exists(file_path):
                        # If file exists, read and display content in the text widget
                        with open(file_path, 'r') as file:
                            file_content = file.read()
                            biltext.delete(1.0, END)  # Clear existing content
                            biltext.insert(END, file_content)  # Insert new content
                    else:
                        # If file is not found, show an error message
                        messagebox.showerror("Error", "File not found or invalid file type.")
                    
                    biltext.config(state=DISABLED)
                    bclr.set("")


                 

                 billing_frame=Frame(dining_frame,bg="#CCCCFF",relief=SUNKEN,bd=3)
                 billing_frame.place(x=910,y=52,height=605,width=463)

                 biltext=Text(billing_frame,height=34,width=54,relief='sunken',state=DISABLED)
                 biltext.place(x=1,y=1)

                 bilscrollbary=Scrollbar(billing_frame,orient='vertical',command=biltext.yview,bg='#148f77')
                 bilscrollbary.place(x=438,y=1,height=545,width=20)
                 biltext['yscrollcommand']=bilscrollbary.set

                 bsvae=Button(billing_frame,text="Save",font=('Bahnschrift',12),bg="#148f77",fg="white",
                              command=save_file,height=1,width=8,relief='raised',bd=2,cursor='hand2')
                 bsvae.pack(side=LEFT,anchor='sw',padx=3,pady=5)

                 bprint=Button(billing_frame,text="Print",font=('Bahnschrift',12),bg="#148f77",fg="white",
                               command=exit,height=1,width=8,relief='raised',bd=2,cursor='hand2')
                 bprint.pack(side=LEFT,anchor='sw',padx=3,pady=5)                 

                 bclear=Button(billing_frame,text="Clear",font=('Bahnschrift',12),bg="#148f77",fg="white",
                               command=bilclearr,height=1,width=8,relief='raised',bd=2,cursor='hand2')
                 bclear.pack(side=LEFT,anchor='sw',padx=3,pady=5)

                 bsearch=Button(billing_frame,text="Search",font=('Bahnschrift',12),bg="#148f77",fg="white",
                                command=search_file,height=1,width=8,relief='raised',bd=2,cursor='hand2')
                 bsearch.pack(side=LEFT,anchor='sw',padx=3,pady=5)

                 bclr=StringVar()

                 bentry=Entry(billing_frame,font=("Calibri (Body)",11),textvariable=bclr)
                 bentry.pack(side=LEFT,anchor='sw',pady=10,padx=3)



                #  ==============================total area========================================
                 
                 def bilclear():
                     totaldis.config(state=NORMAL)
                     extrabil.set(value=0)
                     totaldis.delete(0,END)
                     totaldis.config(state=DISABLED)

                 def bilttl():
                     global bildict
                     totaldis.config(state=NORMAL)
                     billist=[]
                     for key,value in bildict.items():
                         product=key*value
                         billist.append(product)

                     total=float(sum(billist))+float(extrabil.get())
                     tcost.set(total)
                     billist=[]
                     bildict={}
                     totaldis.config(state=DISABLED)

                
                 
                 def billgen():
                     global l

                     biltext.config(state=NORMAL)
                     biltext.delete("1.0",END)
                     now = datetime.now()

                    # Format the date in yyyy-mm-dd format
                     current_date = now.strftime("%Y-%m-%d")

                    # Format the time in hh:mm:ss format
                     current_time = now.strftime("%H:%M:%S")

                     file_path = 'fcid.txt'

                     def read_file_as_int_list(file_path):
                        try:
                            with open(file_path, 'r') as file:
                                lines = file.readlines()
                            return [int(line.strip()) for line in lines if line.strip().isdigit()]
                        except FileNotFoundError:
                            info_status.config(text="File error has occured! Contact developer.",bg='red')
                            error=error+1
                        except ValueError:
                            info_status.config(text="File error has occured! Contact developer.",bg='red')
                            error=error+1

                     def append_to_file(file_path, integer_to_append):
                        with open(file_path, 'a') as file:
                            file.write(f"{integer_to_append}\n")

                     while True:
                        iid=randint(1000,10000)

                        file_contents = read_file_as_int_list(file_path)
                        
                        if iid not in file_contents:
                            append_to_file(file_path, iid)
                            cid1=iid
                            l.append(cid1)
                            break
                     
                     bill=displayord.get("1.0",END)
                     
                     hfile=open("hname.txt",'r+')
                     hname=hfile.read()
                     hfile.close()

                     format=f"\t{hname}\nDate:{current_date}\t\tTime:{current_time}\nContact:yourajverma@gmail.com\n\nCustomer ID:{cid1}\nCustomer Name:{(cname.get()).title()}\t\t{chooser.get()}\n\n{bill}\n\nTotal Cost:{totaldis.get()}"
                     biltext.insert(END,format)
                     
                     cus_entry.delete(0,END)
                     chooser.set(value='Stayer')
                     fordered.set(value="Select the Ordered food")
                     cost_entry.delete(0,END)
                     ftyp.set(value='Food Type')
                     quantity.set(value='Full')
                     quant.set(1)
                     totaldis.config(state=NORMAL)
                     extrabil.set(value=0)
                     totaldis.delete(0,END)
                     totaldis.config(state=DISABLED)
                     biltext.config(state=DISABLED)
                     displayord.delete('1.0',END)
                                         

                 total_frame=Frame(dining_frame,relief=SUNKEN,bd=3,bg="#CCCCFF")
                 total_frame.place(x=455,y=407,height=250,width=445)

                 total_area=LabelFrame(total_frame,text="Total Area",font=('Bahnschrift',12),fg="#148f77",height=237,width=439,bg="#CCCCFF")
                 total_area.place(x=1,y=1)
                 
                 extracost=Label(total_frame,text="Extra Cost:",font=('Bahnschrift',12),fg="#148f77",bg="#CCCCFF")
                 extracost.place(x=5,y=30)
                 
                 extrabil=StringVar()

                 extradis=Entry(total_frame,textvariable=extrabil)
                 extradis.place(x=100,y=30)
                 extrabil.set(value=0)

                 tcost=StringVar()

                 totalcost=Label(total_frame,text="Total Cost:",font=('Bahnschrift',12),fg="#148f77",bg="#CCCCFF")
                 totalcost.place(x=5,y=60)
                 totaldis=Entry(total_frame,textvariable=tcost,state=DISABLED)
                 totaldis.place(x=100,y=60)


                 totalbtn=Button(total_frame,text="Total",font=('Bahnschrift',12),bg="#148f77",fg="white",command=bilttl)
                 totalbtn.place(x=25,y=110,height=35,width=100)

                 genbill=Button(total_frame,text="Generate Bill",font=('Bahnschrift',12),bg="#2e86c1",fg="white",command=billgen)
                 genbill.place(x=170,y=110,height=35,width=100)

                 bilclr=Button(total_frame,text="Clear",font=('Bahnschrift',12),bg="#e74c3c",fg="white",command=bilclear)
                 bilclr.place(x=310,y=110,height=35,width=100)
                 

                 #  ====================================== food area =========================

                 def addata():
                     def insert_data(food_name, food_typ):
                        global sqlp
                        try:
                            # Establish a connection to the MySQL database
                            conn = connect(
                                host='localhost',  
                                user='root',       
                                password=sqlp,
                                database='hms'     
                            )

                            if conn.is_connected():
                                cursor = conn.cursor()

                                
                                select_query = "SELECT food, food_typ FROM dining WHERE food = %s"
                                cursor.execute(select_query, (food_name,))
                                existing_record = cursor.fetchone()

                                if existing_record:
                                  
                                    status_bar.config(text="Inserted food Already exist!",bg="red")
                                else:
                        
                                    insert_query = "INSERT INTO dining (food, food_typ) VALUES (%s, %s)"
                                    data = (food_name, food_typ)
                                    cursor.execute(insert_query, data)
                                    conn.commit()
                                    status_bar.config(text="New Food Inserted!",bg="Green")
                                    fenval.set("")
                                    foodtyp1.set('Food Type')


                        except Error as e:
                            pass
                        
                        finally:
                     
                            if conn.is_connected():
                                cursor.close()
                                conn.close()

     
                     if len(fenval.get())!=0 and ftyp1.get()!='Food Type':
                        insert_data((fentry.get()).title(), ftyp1.get())
                     else:
                         status_bar.config(text="Please Enter Valid Parameters!",bg="red")
                         
                     

                 food_frame=Frame(dining_frame,relief=SUNKEN,bd=3,bg="#CCCCFF")
                 food_frame.place(x=2,y=407,height=250,width=450)

                 addlbl=LabelFrame(food_frame,text="Add food",font=('Bahnschrift',12),fg="#148f77",height=237,width=439,bg="#CCCCFF")
                 addlbl.place(x=1,y=1)

                 fname=Label(food_frame,text="Food Name:",font=('Bahnschrift',12),fg="#148f77",bg="#CCCCFF")
                 fname.pack(side=LEFT,anchor='nw',padx=10,pady=25)

                 fenval=StringVar()

                 fentry=Entry(food_frame,font=("Calibri (Body)",11),textvariable=fenval,width=35)
                 fentry.pack(side=LEFT,anchor='nw',pady=25)

                 foodopt1=['Starter','Main Course','Dessert','Others']
                 ftyp1=StringVar()

                 foodtyp1=ttk.Combobox(food_frame,values=foodopt1,font=('Bahnschrift',12),textvariable=ftyp1)
                 foodtyp1.place(x=10,y=70)

                 foodtyp1.set('Food Type')

                 fadd=Button(food_frame,text="Add Food",font=('Bahnschrift',12),bg="#148f77",fg="white",command=addata)
                 fadd.place(x=230,y=70,height=25,width=100)

                #  ======================================================================
                 

                 dining_path='food.png'
                 dining_size=(30,30)
                 dining_img=resize_image(dining_path,dining_size)

                 din_img_lab=Label(header_frame3,image=dining_img,bg='#f39c12')
                 din_img_lab.place(x=55,y=8)

                # #  =========================Stats starts from here ==============================

                #  stats_frame=Frame(tabs,bg='#e5e7e9',height=690,width=1380)
                #  stats_frame.pack(fill='both',expand=1)

                #  header_frame3=Frame(stats_frame,height=50)
                #  header_frame3.pack(fill=X,padx=2)
                 
                 
                #  stats_label=Label(header_frame3,text='Statstics',font=('Copperplate Gothic Bold',14),relief='groove',height=2,
                #                  width=20,bd=5,bg='#f39c12',fg='white')
                #  stats_label.place(x=2,y=2)

                #  stats_path='marketing.png'
                #  stats_size=(30,30)
                #  stats_img=resize_image(stats_path,stats_size)

                #  stats_img_lab=Label(header_frame3,image=stats_img,bg='#f39c12')
                #  stats_img_lab.place(x=50,y=8)

                #  ===========================setting starts from here ==========================

                 setting_frame=Frame(tabs,bg='#e5e7e9',height=690,width=1380)
                 setting_frame.pack(fill='both',expand=1)
                 
                 
                 sett_label=Label(setting_frame,text='Settings',font=('Copperplate Gothic Bold',14),relief='groove',height=2,
                                 width=20,bd=5,bg='#f39c12',fg='white')
                 sett_label.place(x=2,y=2)

                 sett_path='settings.png'
                 sett_size=(30,30)
                 sett_img=resize_image(sett_path,sett_size)

                 set_img_lab=Label(setting_frame,image=sett_img,bg='#f39c12')
                 set_img_lab.place(x=50,y=8)

                 devframe=Label(setting_frame,text="This Section is under development!",font=('Copperplate Gothic Bold',14))

                 devframe.place(x=100,y=100)

                 
                 

                #  =====================All tabs are added here =============================


                 tabs.add(cus_frame,text='Customer')
                 tabs.add(room_frame,text='Room Availability & Bokking')
                 tabs.add(dining_frame,text='Dining')
                #  tabs.add(stats_frame,text='Stats')
                 tabs.add(setting_frame,text='Settings')

                 win.mainloop()
            else:
                hider2.config(text='Wrong Password',fg='red',bg='#d1f2eb')

            

        cursor1.close()
        conn.close()

    # ============== LOGIN GEOMETRY ================
    try:
        login=Tk()
        login.geometry("1380x700+80+50")
        login.title('Login')
        login.iconbitmap('user.ico')
        login.config(bg='#d1f2eb')

        # ===================TITLE AND LINE ======================

        title=Label(login,text='HOTEL MANAGEMENT SYSTEM',font=('Copperplate Gothic Bold',36),bg='#d1f2eb',fg='#76448a',height=1)
        title.pack(pady=10)
        line_canvas=Canvas(login,bg='#d1f2eb',height=20,width=950)
        line_canvas.place(x=200,y=80)
        coor=0,5,1100,5
        line=line_canvas.create_line(coor,fill='#148f77',width=2)

        # ========================== LOGIN IMAGE =========================

        user_img_size=(100,100)
        user_img_path='user1.png'
        user_img=resize_image(user_img_path,user_img_size)
        user_logo=Label(login,image=user_img,bg='#d1f2eb')
        user_logo.pack(pady=100)
        
        login_label=Label(login,text='LOGIN',font=('High Tower Text',18,'bold'),bg='#d1f2eb',fg='#76448a')
        login_label.place(x=645,y=290)

        # ====================== password Entry frame ================================

        e_password=LabelFrame(login,text='Enter Password',font=('Bahnschrift',12),height=60,width=290,bg='#d1f2eb',
                            bd=2,fg='#76448a')
        e_password.place(x=550,y=340)

        loginvalue=StringVar()
        login_pass_entry=Entry(login,font=('Bahnschrift',12),bg='#d1f2eb',fg='#76448a',show='*',
                    relief=FLAT,textvariable=loginvalue)
        login_pass_entry.place(x=555,y=360,height=32,width=200)

        hu_button2=Button(login,text='Show',font=('Bahnschrift',12),bg='#d1f2eb',command=show2,fg='#76448a',
                        relief='flat',cursor='hand2',width=7)
        hu_button2.place(x=758,y=360)

        hider2=Label(login,text='',font=('Bahnschrift',12),height=1,width=25,bg='#d1f2eb')
        hider2.place(x=555,y=405)

        log_button=Button(login,text='Login',font=('Bahnschrift',14,'bold'),height=1,width=10,bg='#1abc9c',
                        fg='#76448a',command=logentry,cursor='hand2')
        log_button.pack(pady=57)

        desclog=Label(login,text='',bg='#d1f2eb',font=('Bahnschrift',12,'bold'))
        desclog.pack(fill=X,side=BOTTOM)

        login.mainloop()
    except ReferenceError:
        pass
    
file.close()
