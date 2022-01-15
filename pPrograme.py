from tkinter import *
from tkinter import messagebox
import tkinter.filedialog as tkdl
import cv2

def pfunction():
    show_p_login()
def show_p_login():
    p_dang_nhap=Toplevel(root)
    
    p_dang_nhap.geometry("800x600")
    p_dang_nhap.configure(bg="#d7dae2")
    p_dang_nhap.title("Operating System")
    p_dang_nhap.resizable(False, False)
    
    lblTitle=Label(p_dang_nhap, text="Login System", font=("arial", 40, "bold"), fg="black", bg="#d7dae2")
    lblTitle.pack(pady=30)
    
    borderColor=Frame(p_dang_nhap, bg="black", width=700, height=480)
    borderColor.pack()
    
    mainFrame=Frame(borderColor, bg="#d7dae2", width=600, height=360)
    mainFrame.pack(padx=16, pady=16)
    
    password=StringVar()
    
    entry_password=Entry(mainFrame, show="*", textvariable=password, width=12, bd=2, font=("arial", 24))
    entry_password.place(x=280, y=50)
    Label(mainFrame, text="Password:", font=("arial", 24, "bold"), bg="#d7dae2").place(x=90, y=50)
    
    def reset():
        entry_password.delete(0, END)
        
    def login():
        pw=password.get()
    
        if pw=="children":
            pass
        elif pw=="parent":
            p_dang_nhap.destroy()
            show_p_do()
        elif pw=="":
            messagebox.showerror("Invalid", "Please enter password!")
        else:
            messagebox.showerror("Invalid", "Password is wrong, try again!")
    
    btn_login = Button(mainFrame, text="Login", height="2", width=16, bg="#ed3833", fg="white", bd=0, command=login).place(x=90, y=200)
    Button(mainFrame, text="Reset", height="2", width=16, bg="#1089ff", fg="white", bd=0, command=reset).place(x=250, y=200)
    Button(mainFrame, text="Exit", height="2", width=16, bg="#00bd56", fg="white", bd=0, command=p_dang_nhap.destroy).place(x=410, y=200)

def show_p_do():
    p=Toplevel(root)
    p.geometry("400x300")
    p.configure(bg="#d7dae2")
    p.title("Operating System")
    p.resizable(False, False)
    def show_image():
        #path = tkdl.askopenfilename()
        path = "hoc.png"
        if len(path) > 0:
            image = cv2.imread(path)
            cv2.imshow('Display Image', image)
            cv2.waitKey(0)
    img = Button(p, text="Hình ảnh", height="2", width=16, bg="#1089ff", fg="white", bd=0, command=show_image).place(x=150, y=50)
    key = Button(p, text="Bàn phím", height="2", width=16, bg="#7089ff", fg="white", bd=0, command=show_image).place(x=150, y=100)
    xem = Button(p, text="Xem khung thời gian", height="2", width=16, bg="#3339ff", fg="white", bd=0, command=show_image).place(x=150, y=150)
    sua = Button(p, text="Sửa khung thời gian", height="2", width=16, bg="#9659ff", fg="white", bd=0, command=show_image).place(x=150, y=200)

root=Tk()
root.geometry("200x160")
root.resizable(False, False)
root.title("OS")
Button(root, text="Run P", height="2", width=16, bg="#1089ff", fg="white", bd=0, command=pfunction).pack(padx=20, pady=20)
root.mainloop()