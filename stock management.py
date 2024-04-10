import mysql.connector
print('''
\t\t\t\t- - - - - - - - - - - - - - - - - - - - - - -
\t\t\t\t   STOCK MANAGEMENT
\t\t\t\t- - - - - - - - - - - - - - - - - - - - - - - ''')
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root")
mycursor=mydb.cursor()
mycursor.execute('create database if not exists stock_management;')
mycursor.execute('use stock_management')
mycursor.execute('create table if not exists login(username varchar(25) not null, password varchar(25) not null)')
mycursor.execute('create table if not exists purchase (odate date not null , name varchar(25) not null, pcode int not null,amount int not null)')
mycursor.execute('create table if not exists stock(pcode int not null, pname varchar(25) not null,quantity int not null, price int not null)')
mydb.commit()
z=0
mycursor.execute('select *from login')
for i in mycursor:
    z+=1
if(z==0):
    mycursor.execute("insert into login values('root','root')")
    mydb.commit()
while True:
    print('''
1.ADMIN
2.CUSTOMER
3.EXIT ''')
    ch=int(input('Enter your choice: '))
    if (ch==1):
        passs=input('Enter Password: ')
        mycursor.execute('select *from login')
        for i in mycursor:
            user,passwd=i
            if(passs==passwd):
                print('WELCOME')
            loop2='y'
            while(loop2=='y'or loop2=='Y'):
                print('''
        1. ADD NEW ITEM
        2. UPDATING PRICE
        3. DELETING ITEM
        4. DISPLAY ALL ITEMS
        5. TO CHANGE THE PASSWORD
        6. LOG OUT
         ''')
                ch=int(input('Enter your choice: '))
                if (ch==1):
                    loop='y'
                    while(loop=='y'or loop=='Y'):
                        pcode=int(input('Enter Product Code: '))
                        pname=input('Enter Product Name: ')
                        quantity=int(input('Enter Product Quantity: '))
                        price=int(input('Enter Product Price: '))
                        mycursor.execute("insert into stock values('"+str(pcode)+"','"+pname+"','"+str(quantity)+"','"+str(price)+"')")
                        mydb.commit()
                        print('Record Succesfully Entered')
                        loop=input('Do you want to enter more items (yes(y)/no(n)) : ')
                    loop2=input('Do you want to continue editing stock (yes(y)/no(n)) : ')
                elif(ch==2):
                    loop='y'
                    while(loop=='y'or loop=='Y'):
                        pcode=int(input('Enter Product Code: '))
                        new_price=int(input('Enter Product New Price: '))
                        mycursor.execute("update stock set price='"+str(new_price)+"'where pcode='"+str(pcode)+"'")
                        mydb.commit()
                        print('Record Succesfully Entered')
                        loop=input('Do you want to change price of any other stock item (yes(y)/no(n)) : ')
                    loop2=input('Do you want to continue editing stock (yes(y)/no(n)) : ')    
                elif(ch==3):
                    loop='y'
                    while(loop=='y' or loop=='Y'):
                        pcode=int(input('Enter Product Code: '))
                        mycursor.execute("delete from stock where pcode='"+str(pcode)+"'")
                        mydb.commit()
                        print('Record Succesfully Entered')
                        loop=input('Do you want to delete any other data (yes(y)/no(n)) : ')
                    loop2=input('Do you want to continue editing stock (yes(y)/no(n)) : ')
                elif(ch==4):
                    mycursor.execute('select*from stock')
                    print(''' pcode || pname || quantity || price ''')
                    for i in mycursor:
                        t_code,t_name,t_quan,t_price=i
                        print(f" {t_code} || {t_name} || {t_quan} || {t_price} ")
                elif(ch==5):
                    old_passs=input('Enter old password : ')
                    mycursor.execute('select * from login')
                    for i in mycursor:
                        username,password=i
                        if(old_passs==passs):
                            new_passs=input('Enter New Password : ')
                            mycursor.execute("update login set password='"+new_passs+"'")
                            mydb.commit()
                        print('Password Succesfully Changed')
                elif(ch==6):
                    break
            else:
                break

           
    elif(ch==2):
        print('''
    1. Item Bucket
    2. Payment
    3. View Available Items
    4. Go Back ''')
        ch2=int(input('Enter your choice : '))
        if (ch2==1):
            name=input('Enter Your Good Name : ')
            pcode=int(input('Enter Product Code : '))
            quantity=int(input('Enter Product Quantity : '))
            mycursor.execute("select * from stock where pcode='"+str(pcode)+"'")
            for i in mycursor:
                t_code,t_name,t_quan,t_price=i
            amount=t_price*quantity
            net_quan=t_quan-quantity
            mycursor.execute("update stock set quantity='"+str(net_quan)+"'where pcode='"+str(pcode)+"'")
            mycursor.execute("insert into purchase values(now(),'"+name+"','"+str(pcode)+"','"+str(amount)+"')")
            mydb.commit()
        elif(ch2==2):
            print(f"amount to be paid : {amount}")
        elif(ch2==3):
            print(" CODE || NAME || PRICE ")
            mycursor.execute("select * from stock")
            for i in mycursor:
                t_code,t_name,t_quan,t_price=i
                print(f" {t_code} || {t_name} || {t_price} ")
        elif(ch2==4):
            break
        elif(ch==3):
            break
