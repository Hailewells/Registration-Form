from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.geometry("1000x700")
load=Image.open('D:\\w4.JPG')
render=ImageTk.PhotoImage(load)
root.geometry("1000x700")
lbl=Label(root,image=render)
lbl.place(x=0,y=0)
root.title("Registration")
root.geometry("1000x700")
root.resizable(True,True)

def register():
    fullname_info=fullnameValue.get()
    gender_info=genderValue.get()
    age_info=ageValue.get()
    email_info=emailValue.get()
    phone_num_info=phonenumValue.get()
    collage_info=collageValue.get()
    role_info=roleValue.get()
    
    file=open(fullname_info +".txt","w")
    file.write(fullname_info +"\n")
    file.write(gender_info +"\n")
    file.write(age_info +"\n")
    file.write(email_info+"\n")
    file.write(phone_num_info+"\n")
    file.write(collage_info+"\n")
    file.write(role_info+"\n")
    file.close()

    fullnameEntry.delete(0,END)
    genderEntry.delete(0,END)
    ageEntry.delete(0,END)
    emailEntry.delete(0,END)
    phonenumEntry.delete(0,END)
    collageEntry.delete(0,END)
    roleEntry.delete(0,END)

    Label(text="Registration Success!!!",fg="purple",font=("calibri",11)).place(x=650,y=600)
Label(root,text="REGISTRATION FORM FOR \n ELECRTICAL ASSOCIATION MEMBERSHIP",font="arial 25").pack(pady=50)

Label(text="Full name",font=23).place(x=100,y=150)
Label(text="Gender",font=25).place(x=100,y=200)
Label(text="Age",font=25).place(x=100,y=250)
Label(text="Email",font=25).place(x=100,y=300)
Label(text="Phone num",font=25).place(x=90,y=350)
Label(text="Collage",font=25).place(x=100,y=400)
Label(text="Role",font=25).place(x=100,y=450)

#Entry
fullnameValue=StringVar()
genderValue=StringVar()
ageValue=StringVar()
emailValue=StringVar()
phonenumValue=StringVar()
collageValue=StringVar()
roleValue=StringVar()

fullnameEntry=Entry(root,textvariable=fullnameValue,width=30,bd=2,font=20)
genderEntry=Entry(root,textvariable=genderValue,width=30,bd=2,font=20)
ageEntry=Entry(root,textvariable=ageValue,width=30,bd=2,font=20)
emailEntry=Entry(root,textvariable=emailValue,width=30,bd=2,font=20)
phonenumEntry=Entry(root,textvariable=phonenumValue,width=30,bd=2,font=20)
collageEntry=Entry(root,textvariable=collageValue,width=30,bd=2,font=20)
roleEntry=Entry(root,textvariable=roleValue,width=30,bd=2,font=20)

fullnameEntry.place(x=200,y=150)
genderEntry.place(x=200,y=200)
ageEntry.place(x=200,y=250)
emailEntry.place(x=200,y=300)
phonenumEntry.place(x=200,y=350)
collageEntry.place(x=200,y=400)
roleEntry.place(x=200,y=450)



CheckValue=IntVar
Checkbtn=Checkbutton(text="Remember me?",variable=CheckValue)
Checkbtn.place(x=600,y=500)
Button(text="REGISTER",font=20,width=11,height=2,command=register).place(x=600,y=550)


root.mainloop()
