from tkinter import *
from tkcalendar import DateEntry
from tkinter import messagebox as mb
import datetime
import csv
root=Tk()
root.geometry('520x540')
root.title('Registration Form')
root.configure(background='grey')

def msg():
    course=evar.get()
    gender=rvar.get()
    if(gender==1 or gender==2):
        if (e1.index("end")==0):
            mb.showwarning("Missing details","enter your name")
        elif (e2.index("end")==0):
            mb.showwarning("Missing details","enter your email id")
        elif(e3.index("end")==0):
            mb.showwarning("Missing details","enter your contact number")
        else:
            mb.showinfo("Success","Registration done successfully for the course"+course)
    else:
        mb.showinfo("Missing details","enter your gender")

def save():
    g=rvar.get()
    course=evar.get()
    db=dob.get_date()
    d=db.strftime("%d/%m/%Y")
    now=datetime.datetime.now()
    if (g==1):
        gender="male"
    else:
        gender="female"

    s='\n'+now.strftime("%d-%m-%Y%H:%M")+'\t'+e1.get()+'\t'+e2.get()+'\t'+e3.get()+'\t'+d+'\t'+gender+'\t'+course
    f=open(('regdetails.txt'),'a')
    f.write(s)
    f.close()
def saveinfo():
    save()
    msg()
l0=Label(root,text="Course Registration Form",width=25,font=("times",20,"bold"),bg="blue",fg="white")
l0.place(x=70,y=50)

l1=Label(root,text="Full name",width=20,font=("times",12,"bold"),anchor="w",bg="grey")
l1.place(x=70,y=130)
e1=Entry(root,width=30,bd=2)
e1.place(x=240,y=130)

l2=Label(root,text="Email",width=20,font=("times",12,"bold"),anchor="w",bg="grey")
l2.place(x=70,y=180)
e2=Entry(root,width=30,bd=2)
e2.place(x=240,y=180)

l4=Label(root,text="DOB",width=20,font=("times",12,"bold"),anchor="w",bg="grey")
l4.place(x=70,y=230)
dob=DateEntry(root,width=27,background="brown",foreground="white",date_pattern="dd/mm/y",borderwidth=3)
dob.place(x=240,y=230)

l5=Label(root,text="Gender",width=20,font=("times",12,"bold"),anchor="w",bg="grey")
l5.place(x=70,y=280)
rvar=IntVar()
r1=Radiobutton(root,text="Male",variable=rvar,value=1,font=("times",12),bg="grey")
r1.place(x=235,y=280)
r2=Radiobutton(root,text="Female",variable=rvar,value=2,font=("times",12),bg="grey")
r2.place(x=315,y=280)

l3=Label(root,text="Contactno",width=20,font=("times",12,"bold"),anchor="w",bg="grey")
l3.place(x=70,y=320)
e3=Entry(root,width=30,bd=2)
e3.place(x=240,y=320)

l6=Label(root,text="Select course",width=20,font=("times",12,"bold"),anchor="w",bg="grey")
l6.place(x=70,y=370)
evar=StringVar()
evar.set("Select course")

option=("Python","Javascript","Perl","Java")
o=OptionMenu(root,evar,*option)
o.config(font=("times",11),bd=3)
o.place(x=240,y=365,width=190)

b1=Button(root,text="Submit",command=saveinfo,width=15,bg="green",fg="white",font=("times",12,"bold"))
b1.place(x=120,y=440)

b2=Button(root,text="Cancel",command=root.destroy,width=15,bg="red",fg="white",font=("times",12,"bold"))
b2.place(x=320,y=440)
root.mainloop()