import mysql.connector
mydb=mysql.connector.connect(host='localhost',\
                             user='root',\
                             passwd='tiger',\
                             database='test')

def calculate():
    mycursor=mydb.cursor()
    mycursor.execute('SELECT emp_id,basic_pay FROM eims')
    records=mycursor.fetchall()
    da=25
    hra=18
    ta=8
    pf=7
    for row in records:
        b=row[1]
        d=(b*da)/100
        h=(b*hra)/100
        t=(b*hra)/100
        total=b+d+h+t
        p=(total*pf)/100
        net=total-p
        data=(d,h,t,total,p,net,row[0])
        s= " Update eims set da= %s,  hra=%s, ta=%s, total_salary=%s, pf=%s, net_salary=%s where emp_id=%s"
        mycursor.execute(s,data)
        mydb.commit()
    mycursor.close()
        
    
def display_table():
    calculate()
    mycursor=mydb.cursor()
    print('HOW DO YOU WANT IT TO DISPLAY? \n')
    print(" 1.  ASCENDING ORDER OF Employee ID \n \
2.  ASCENDING ORDER OF  Name \n \
3.  ASCENDING ORDER OF Basic Pay \n \
4.  DESCENDING ORDER OF Employee ID  \n \
5.  DESCENDING ORDER OF Name \n \
6.   DESCENDING ORDER OF Basic Pay \n \
7.  DEPARTMENT WISE \n")
    ch=int(input('ENTER YOUR CHOICE: '))
    print('\n')
    if ch==1:
            mycursor.execute('SELECT * FROM eims ORDER BY emp_id')
    elif ch==2:
        mycursor.execute('SELECT * FROM eims ORDER BY emp_name')
    elif ch==3:
        mycursor.execute('SELECT * FROM eims ORDER BY basic_pay')
    elif ch==4:
        mycursor.execute('SELECT * FROM eims ORDER BY emp_id DESC')
    elif ch==5:
       mycursor.execute('SELECT * FROM eims ORDER BY emp_name DESC')
    elif ch==6:
        mycursor.execute('SELECT * FROM eims ORDER BY basic_pay DESC')
    elif ch==7:
        d=input('Enter the designation whose data you want to see.')
        mycursor.execute("SELECT * FROM eims WHERE designation=%s",(d,))
    else:
        print('WRONG CHOICE')
    records=mycursor.fetchall()
    print('\n')
    print('Number of row=',mycursor.rowcount,'\n')
    print("{0:10}      {1:3}      {2:15}      {3:^10}       {4:^9}       {5:^10}      {6:10}      {7:10}      {8:^10}       {9:12}".format("Emp_ID","Emp_Name","Designation","Basic_Pay","DA","HRA","TA","Total_Salary","PF","Net_Salary"))
    for x in records:
        print("{0:<5}        {1:^13}      {2:15}      {3:^10}       {4:^6}       {5:^10}      {6:10}      {7:11}      {8:^13}       {9:^12}".format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9]))
        
def update():
    oid=int(input('Enter the id of the employee : '))
    mycursor=mydb.cursor()
    mycursor.execute('SELECT * FROM eims WHERE emp_id=%s',(oid,))
    records=mycursor.fetchall()
    print("{0:5}   {1:9}   {2:15}   {3:8}   {4:6}   {5:6}   {6:5}    {7:15}   {8:5}   {9:7}".format("Emp ID","Emp Name","Designation","Basic Pay","DA","HRA","TA","Total Salary","PF","Net Salary"))    
    print()
    for x in records:
        print("{0:5}   {1:9}   {2:15}   {3:8}   {4:6}   {5:6}   {6:5}    {7:15}   {8:5}   {9:7}".format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9]))
    fc=input('Do you really want to update the data?(Y/N)').upper()
    if fc=='Y':
        print("10XX=Lawyer ,  11XX=Clerk ,  13XX=Manager ,  14XX=Analyst ,  18XX=HR ,  19XX=CEO")
        nid=int(input('Enter Employee Id : '))
        name=input('Enter name of the employee : ')
        d=input('Enter designation : ')
        b=int(input('Enter basic pay : '))
        data=(nid,name,d,b,oid)
        mycursor.execute('Update eims set emp_id=%s, emp_name=%s, designation=%s, basic_pay=%s where emp_id=%s',data)
        print('Data successfully updated')
    mydb.commit()
    mycursor.close()

def add():
    print('For entering the data : ')	
    print("10XX=Lawyer ,  11XX=Clerk ,  13XX=Manager ,  14XX=Analyst ,  18XX=HR ,  19XX=CEO")
    ID=int(input('Enter the four digit number : '))
    name=input(' Enter the employee name : ')
    designation=input(' Enter the designation : ')
    bp= int(input(' Enter Basic Pay : '))
    mycursor.execute("INSERT INTO eims VALUES ({},'{}','{}',{},{},{},{},{},{},{})".format(ID,name,designation,bp))
    mydb.commit()
    mycursor.close()
    print("Data  added successfully")

def delete():
    mycursor=mydb.cursor()
    ID=int(input('ENTER THE EMPLOYEE ID :'))
    mycursor.execute("DELETE FROM eims WHERE Rollno=%s",(ID,))
    mydb.commit()
    mycursor.close()
    print('RECORD DELETED \n')
    
def menu():
    ch="Y"
    while (ch=='Y'):
        print('\t \t \t  MENU: \n')
        print('\t \t \t \t1.  Display Table')
        print('\t \t \t \t2.  Add Records')
        print('\t \t \t \t3.  Delete Records')
        print('\t \t \t \t4.  Update Records')
        print('\t \t \t \t5. Exit \n')
        c=int(input('Enter your choice:  '))
        print('\n')
        if c==1:
            display_table()
        elif c==2:
           add()
        elif c==3:
            delete() 
        elif c==4:
            update()
        elif c==5:
            ch='N'
            print('Program Terminated')
        else:
            print('Wrong Choice')
menu()
mydb.close()        
        
