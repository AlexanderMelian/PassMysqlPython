from tkinter import Button, Label, Grid, Entry, Pack, DISABLED, Listbox, Tk, Frame, StringVar, Scrollbar, IntVar, Toplevel
import hashlib
import pymysql
import re

raiz = Tk()
user = StringVar()
password = StringVar()
log = StringVar()



def register():
    c_user = user.get()
    usercheck = u_checker(c_user,1)
    if usercheck:
        if len(password.get())==0:
            print("Contraseña sin caracteres no es valido")
        else:
            c_pass = hashlib.sha256(password.get().encode('utf-8')).hexdigest()
            pymysql.register(c_user, c_pass)

def logging():
    c_user = user.get()
    usercheck = u_checker(c_user,0)
    if usercheck:
        if len(password.get())==0:
            print("Contraseña sin caracteres no es valido")
        else:
            c_pass = hashlib.sha256(password.get().encode('utf-8')).hexdigest()
            loggeado = pymysql.logging(c_user, c_pass)
    if loggeado:
        print("Loggeado correctamente")
    else:
        print("Contraseña incorrecta")

def u_checker(c_user, dupli):
    if len(c_user) == 0:
        print("User sin caracteres no es valido")
    elif len(c_user) < 3: 
        print("User minimo de 3 caracteres") 
        return False
    elif len(c_user) > 10: 
        print("User maximo de 10 caracteres") 
        return False
    elif not re.match("^[a-zA-Z]*$", c_user):
        print("User solo caracteres")
        return False
    if dupli:
        if not pymysql.check_user(c_user):
            print("User dupicado no se puede")
            return False
    return True



raiz.title("Passowords")
raiz.geometry("600x400")
MiFrame=Frame()
#MiFrame.pack(fill="both")
MiFrame.pack()
#Mi label
Label(MiFrame,text="user:").grid(row=0,column=0)
Label(MiFrame,text="password:").grid(row=1,column=0)
#Text Entry
Entry(MiFrame,textvariable=user).grid(row=0,column=1)
Entry(MiFrame,textvariable=password, show="*").grid(row=1,column=1)
#
Button(MiFrame,text="Registrar",command=lambda: register()).grid(row=2,column=0)
Button(MiFrame,text="Loggear",command=lambda: logging()).grid(row=2,column=1)
#
raiz.mainloop()