import tkinter as tk


#DEF PARA MAKITA ANG PASSWORD
window =  tk.Tk()

# una

window.title("Punzalan HO exam")
window.geometry("800x500")
window.resizable(False, False)
window.configure(bg= "seashell3")


#unang window

Welcome = tk.Label(text="Welcome!", fg="black", bg="seashell3", font=("arial", 20, "bold"))
Welcome.pack()




    #STORAGE
pass3 = tk.IntVar()

def new():
    def seepass1():
        if pass3.get() == 1:
            pass1.config(show="")
        else:
            pass1.config(show="*")

    popup1 =tk.Toplevel()
    popup1.title("register section")
    popup1.geometry("400x300")
    popup1.resizable(False,False)
    popup1.configure(bg="green")

    #function na mag babago si cred1 if napindot si register

    def submit():
        cred1.config(text="Your are now registered!")

    cred1 = tk.Label(popup1, text="Fill the following informations!", bg="green", fg="white")
    cred1.place(x=110, y=10)


    intro = tk.Label(popup1, text="Register section", bg="green", fg="black", font=("arial", 15, "bold"))
    intro.place(x=110, y=30)

    user = tk.Label(popup1, text="Username:", bg="green", fg="black", font=("arial", 15, "bold"))
    user.place(x=30, y=100)

    password = tk.Label(popup1, text="Password:", bg="green", fg="black", font=("arial", 15, "bold"))
    password.place(x=30, y=140)

    #entry

    user1 = tk.Entry(popup1)
    user1.place(x=175, y=108)

    pass1 = tk.Entry(popup1, show="*")
    pass1.place(x=175, y=140)

    see1 = tk.Checkbutton(popup1, text="See password", command=seepass1, variable=pass3)
    see1.place(x=175, y=160)
    

    register1 = tk.Button(popup1, text="register", bg="white", fg="black", width=20, height=2, command=submit)
    register1.place(x=100, y=190)


# title
# geometry
# resizable
# configure


#submit sec
register = tk.Button(text="Register", bg="blue", fg="black", font=("arial", 15, "bold"), width=80, height=3, command=new)
register.pack(pady=50)
#done



pass4 = tk.IntVar()

def next():
    def seepass2():
        if pass4.get() == 1:
            pass2.config(show="")
        else:
            pass2.config(show="*")

    popup2 = tk.Toplevel()
    popup2.title("Log in section")
    popup2.geometry("400x300")
    popup2.resizable(False, False)
    popup2.configure(bg="red")

    #function ni cred pag nipindot si submit
    

    cred = tk.Label(popup2, text="Fill up the following!", bg="red", fg="black")
    cred.place(x=150, y=10)

    def submit2():
        cred.config(text="The user is now log in!")

    intro1 = tk.Label(popup2,text="Log in", bg="red", fg="black", font=("arial", 15, "bold"))
    intro1.place(x=175, y=30)

    user1 = tk.Label(popup2, text="Username", bg="red", fg="black", font=("arial", 15, "bold"))
    user1.place(x=30, y=100)

    password1 = tk.Label(popup2, text="Password", bg="red",fg="black", font=("arial", 15, "bold"))
    password1.place(x=30, y=140)

#entry

    user2 = tk.Entry(popup2)
    user2.place(x=175, y=108)

    pass2 = tk.Entry(popup2, show="*")
    pass2.place(x=175, y=140)

    see2 = tk.Checkbutton(popup2, text="See password", command=seepass2, variable=pass4)
    see2.place(x=175, y=160)

    login1 = tk.Button(popup2, text="Log in", bg="green", fg="black", font=("arial", 15, "bold"), width=20, height=2, command=submit2)
    login1.place(x=100, y=190)

login = tk.Button(text="Log in", fg='black', bg="green", font=("arial", 15, "bold"), width=80, height="3", command=next)
login.pack(pady=20)













#end
window.mainloop()