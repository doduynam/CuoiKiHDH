from tkinter import *
from tkinter import messagebox
import os
import time

def show_c_login():
    c_dang_nhap=Toplevel(root)
    
    
    c_dang_nhap.geometry("800x600")
    c_dang_nhap.configure(bg="#d7dae2")
    c_dang_nhap.title("Operating System")
    c_dang_nhap.resizable(False, False)
    
    lblTitle=Label(c_dang_nhap, text="Login System", font=("arial", 40, "bold"), fg="black", bg="#d7dae2")
    lblTitle.pack(pady=30)
    
    borderColor=Frame(c_dang_nhap, bg="black", width=700, height=480)
    borderColor.pack()
    
    mainFrame=Frame(borderColor, bg="#d7dae2", width=600, height=360)
    mainFrame.pack(padx=16, pady=16)
    
    password=StringVar()
    
    entry_password=Entry(mainFrame, textvariable=password, width=12, bd=2, font=("arial", 24))
    entry_password.place(x=280, y=50)
    Label(mainFrame, text="Password:", font=("arial", 24, "bold"), bg="#d7dae2").place(x=90, y=50)
    
    def reset():
        entry_password.delete(0, END)
        
    def login():
        pw=password.get()
    
        if pw=="children":
            pass
        elif pw=="parent":
            c_dang_nhap.destroy()
            show_c_wait()
        elif pw=="":
            messagebox.showerror("Invalid", "Please enter password!")
        else:
            messagebox.showerror("Invalid", "Password is wrong, try again!")
    
    btn_login = Button(mainFrame, text="Login", height="2", width=16, bg="#ed3833", fg="white", bd=0, command=login).place(x=90, y=200)
    Button(mainFrame, text="Reset", height="2", width=16, bg="#1089ff", fg="white", bd=0, command=reset).place(x=250, y=200)
    Button(mainFrame, text="Exit", height="2", width=16, bg="#00bd56", fg="white", bd=0, command=c_dang_nhap.destroy).place(x=410, y=200)

def cfunction():
    show_c_login()

def show_c_wait():
    c_wait=Toplevel(root)
    
    c_wait.geometry("800x600")
    c_wait.configure(bg="#d7dae2")
    c_wait.title("Operating System")
    c_wait.resizable(False, False)
    
    lblTitle=Label(c_wait, text="PLEASE WAITING!", font=("arial", 40, "bold"), fg="black", bg="#d7dae2")
    lblTitle.pack(pady=30)
    
    hrs=StringVar()
    Entry(c_wait, textvariable=hrs, width=2, font="arial 50", fg="black", bg="#d7dae2").place(x=130, y=155)
    hrs.set("00")
    
    mins=StringVar()
    Entry(c_wait, textvariable=mins, width=2, font="arial 50", fg="black", bg="#d7dae2").place(x=280, y=155)
    mins.set("00")
    
    sec=StringVar()
    Entry(c_wait, textvariable=sec, width=2, font="arial 50", fg="black", bg="#d7dae2").place(x=430, y=155)
    sec.set("10")
    
    Label(c_wait, text="hours", font="arial 12", fg="black", bg="#d7dae2").place(x=210, y=200)
    Label(c_wait, text="minutes", font="arial 12", fg="black", bg="#d7dae2").place(x=360, y=200)
    Label(c_wait, text="seconds", font="arial 12", fg="black", bg="#d7dae2").place(x=510, y=200)
    
    def Timer():
        times=int(hrs.get())*3600+int(mins.get())*60+int(sec.get())
        
        while times>-1:
            minute, second=(times//60, times%60)
            
            hour=0
            if minute>60:
                hour, minute=(minute//60, minute%60)
                
            sec.set(second)
            mins.set(minute)
            hrs.set(hour)
            
            root.update()
            time.sleep(1)
            
            if times==0:
                show_c_login()
                c_wait.destroy()
            times-=1
        
    Timer()

def pfunction():
    pass

root=Tk()
root.geometry("200x160")
root.resizable(False, False)
root.title("OS")
Button(root, text="Run C", height="2", width=16, bg="#ed3833", fg="white", bd=0, command=cfunction).pack(padx=20, pady=20)
Button(root, text="Run P", height="2", width=16, bg="#1089ff", fg="white", bd=0, command=pfunction).pack(padx=20, pady=20)
root.mainloop()