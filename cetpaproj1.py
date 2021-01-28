from tkinter import *
from tkinter import messagebox
#from sqlite3 import *

class Gui:
    def __init__(self):
        import sqlite3

        self.connection= sqlite3.connect("may8.db")
        try:
            self.cursor=self.connection.cursor()
            self.cursor.execute("create table user(name varchar(30),password varchar(20),email varchar(30))")
            #self.connection.commit()

        except:
            pass
            self.login()
            self.register()
            self.name1 = v3.get()
            self.password1 = v4.get()
            self.email=v6.get()
            self.cursor.execute("insert into user values('{}','{}','{}')".format(self.name1, self.password1,self.email))
            self.connection.commit()
            self.cursor.execute("Select * from user")
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
            self.connection.close()

    def login(self):

        global scr
        global v1_verify
        global v2_verify
        global e1
        global e2
        self.scr=Tk()
        self.scr.config(bg='black')
        self.scr.geometry('1200x800+0+0')
        l = Label(self.scr, text="Welcome To Login Page", font=('times', 30, 'bold'), bg='black', fg='white')
        l.pack(side=TOP, fill=X)
        l3 = Label(self.scr, text="Here you get the solutions for living a  healthy life ", font=('times', 20, 'underline'), bg='blue', fg='white')
        l3.pack(side=TOP,fill=X)
        l4 = Label(self.scr,text='there is no line when it is online', font=('times', 20, 'underline'), bg='yellow', fg='red')
        l4.pack(side=TOP, fill=X)
        f = Frame(self.scr, bg='brown1')
        f.pack(fill=BOTH, expand=12)
        l1 = Label(f, text='Username', font=('times', 20, 'bold'), bg='white', fg='black')
        l1.place(x=200, y=100)
        l2 = Label(f, text='Password', font=('times', 20, 'bold'), bg='white', fg='black')
        l2.place(x=200, y=200)
        v1_verify = StringVar()
        e1 = Entry(f,textvariable=v1_verify ,font=('times', 20, 'bold'), bg='white', fg='black')
        e1.place(x=350, y=100)
        v2_verify = StringVar()
        e2 = Entry(f,textvariable=v2_verify, show='*', font=('times', 20, 'bold'), bg='white', fg='black')
        e2.place(x=350, y=200)

        b = Button(f, text='Register', font=('times', 20, 'bold'),bg='green',command=lambda: self.register())
        b.place(x=200, y=300)

        b1 = Button(f, text='Login', font=('times', 20, 'bold'), command=lambda: self.login_page(e1.get(),e2.get()))
        b1.place(x=400, y=300)
       # self.login_success()
    def register(self):
        global v3
        global v4
        global v6
        global scr1
        self.scr1 = Toplevel(self.scr)
        self.scr1.config(bg='black')
        self.scr1.geometry('1200x800+0+0')
        l = Label(self.scr1, text='WELCOME TO REGISTERATION', font=('times', 25, 'bold'), bg='black', fg='white')
        l.pack(side=TOP, fill=X)
        l = Label(self.scr1, text='Create an account', font=('times', 22, 'underline'), bg='yellow', fg='red')
        l.pack(side=TOP, fill=X)
        f1 = Frame(self.scr1, bg='blue')
        f1.pack(fill=BOTH, expand=12)
        l1 = Label(f1, text='Username', font=('times', 20, 'bold'), bg='white', fg='black')
        l1.place(x=200, y=100)
        l2 = Label(f1, text='Password', font=('times', 20, 'bold'), bg='white', fg='black')
        l2.place(x=200, y=200)
        l3 = Label(f1, text='Confirm password', font=('times', 20, 'bold'), bg='white', fg='black')
        l3.place(x=150, y=300)
        l4 = Label(f1, text='Email', font=('times', 20, 'bold'), bg='white', fg='black')
        l4.place(x=200, y=400)
        v3 = StringVar()
        e3 = Entry(f1,textvariable=v3, font=('times', 20, 'bold'), bg='white', fg='black')
        e3.place(x=350, y=100)
        v4 = StringVar()
        e4 = Entry(f1, textvariable=v4,show='*', font=('times', 20, 'bold'), bg='white', fg='black')
        e4.place(x=350, y=200)
        v5 = StringVar()
        e5 = Entry(f1, show='*',textvariable=v5 , font=('times', 20, 'bold'), bg='white', fg='black')
        e5.place(x=350, y=300)
        v6 = StringVar()
        e6 = Entry(f1, textvariable = v6,  font=('times', 20, 'bold'), bg='white', fg='black')
        e6.place(x=350, y=400)
        b1 = Button(f1, text='Submit', font=('times', 20, 'bold'), command=lambda: self.login())
        b1.place(x=400, y=500)
        self.scr1.mainloop()



        self.scr.mainloop()

    def login_page(self, u, p):
        #self.username1 = v1_verify.get()
        #self.password1 = v2_verify.get()

        d = self.cursor.execute('select count(*) from user where name=%r and password=%r' % (u, p))
        #m=self.cursor.execute('Select  name,password  from  user')
        #n=self.cursor.execute('Select password from user')
        if list(d)[0][0] != 0:
               self.login_success()
               print("logged in")
        else:
              messagebox.showinfo("login", "invalid credentials")


    def login_delete(self):
        #self.scr2.destroy()
        self.scr1.destroy()
        self.medical()

    def login_success(self):
         global scr2
         self.scr2=Toplevel(self.scr)
         self.scr2.title('success')
         self.scr2.config(bg='orange')
         self.scr2.geometry('400x400+0+0')
         l=Label(self.scr2, text='Registeration Successful', font=('times', 20, 'bold'), bg='yellow', fg='red')
         l.pack(side=TOP,fill=X)
         b=Button(self.scr2,text='ok', font=('times', 20, 'bold'), bg='white', fg='black',command=self.login_delete).pack()
         self.scr2.mainloop()




    def medical(self):
        global scr5
        global e4
        self.scr5 = Toplevel(self.scr)
        self.scr5.title('www.medicalshoponline.com')
        self.scr5.config(bg='black')
        self.scr5.geometry('400x400+0+0')
        l = Label(self.scr5, text='Medical Assistant', font=('times', 25, 'underline'), bg='blue',fg='white')
        l.pack(side=TOP, fill=X)
        l = Label(self.scr5, text='Online Medical best solution', font=('times', 25, 'underline'), bg='blue', fg='white')
        l.pack(side=TOP, fill=X)
        l = Label(self.scr5, text='Offer for 2 days only!', font=('times', 30, 'bold'), bg='red', fg='yellow')
        l.pack(side=TOP, fill=X)
        l = Label(self.scr5, text='25% off on each medical item', font=('times', 30, 'bold'), bg='red', fg='yellow')
        l.pack(side=TOP, fill=X)
        f2 = Frame(self.scr5, bg='DeepPink2')
        f2.pack(fill=BOTH, expand=12)
        v7=StringVar()
        e4 = Entry(f2, textvariable=v7, font=('times', 30, 'bold'), bg='white', width=50, fg='black')
        e4.place(x=300, y=100)
        b = Button(f2, text='Search', font=('times', 25, 'bold'), bg='blue', fg='white',activebackground='white',activeforeground='blue', command=lambda : self.webscrap(e4.get(),m))
        b.place(x=700, y=200)
        m=Message(f2)
        m.place(x=800,y=200)
        b = Button(f2, text='Send', font=('times', 25, 'bold'), bg='blue', fg='white', activebackground='white',activeforeground='blue', command=self.send_mail)
        b.place(x=500, y=200)
        self.scr5.mainloop()
    def webscrap(self,value,mes):
        try:
            if self.d:
                pass
        except:
                self.d=self.webscrap1(value)
        try:
            mes.config(text=next(self.d))
        except:
            mes.config(text='END')
            self.d=False


    def webscrap1(self,value):
        global a
        global body
        a=[]
        import requests as r
        import bs4 as b
        dt = r.request('get', 'https://www.1mg.com/search/all?name=%s' % value)
        s = b.BeautifulSoup(dt.text, 'html.parser')
        for i in s.findAll('div', {'class': 'col-md-3 col-sm-4 col-xs-6 style__container___jkjS2'}):
            try:
                dts = r.request('get', 'https://www.1mg.com' + i.find('a').get('href'))
                s1 = b.BeautifulSoup(dts.text, 'html.parser')
                a.append(s1.find('div', {'class': 'ProductDescription__product-description___1PfGf'}).text)
                yield a
            except :
               pass



    def send_mail(self):
        global scr6
        global entry1
        global entry2
        self.scr6 = Toplevel(self.scr5)
        self.scr6.title('www.gmail.com')
        self.scr6.config(bg='white')
        self.scr6.geometry('400x400+0+0')
        l = Label(self.scr6, bg='black',font=('times',25,'bold'), fg='white', text='Your message about details of product')
        l.pack(side=TOP, fill=X)
        f1 = Frame(self.scr6, bg='white')
        f1.pack(fill=BOTH, expand=12)

        l1 = Label(f1, text='From', font=('times', 25, 'bold'), relief='raised',bg='white', fg='black')
        l1.place(x=200, y=100)
        entry1 = Entry(f1, font=('times', 30, 'bold'), bg='white', width=40, fg='black')
        entry1.place(x=300, y=100)
        l2 = Label(f1, text='To', font=('times', 25, 'bold'), relief='raised',bg='white', fg='black')
        l2.place(x=200, y=200)
        entry2 = Entry(f1, font=('times', 30, 'bold'), bg='white', width=40, fg='black')
        entry2.place(x=300, y=200)
        l3 = Label(f1, text='Subject', font=('times', 25, 'bold'), relief='raised', bg='white', fg='black')
        l3.place(x=200, y=300)
        entry3 = Entry(f1, font=('times', 30, 'bold'), bg='white', width=40, fg='black')
        entry3.place(x=300, y=300)
        b = Button(self.scr6, text='Send', font=('times', 25, 'bold'), bg='blue', fg='white',command=lambda : self.mail(entry1.get(),entry2.get(),entry3.get()))
        b.place(x=400,y=400)

        self.scr6.mainloop()

    def mail(self,fr,t,sub):
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        obj=MIMEMultipart()
        obj['From']=fr
        obj['To']=t
        obj['subject']=sub
        obj.attach(MIMEText(str(a[:]),'plain'))
        client = smtplib.SMTP('smtp.gmail.com', 587)
        client.starttls()
        client.login(fr, 'shivanisri')
        client.sendmail(fr, t, obj.as_string())







Gui()