from logging import root
from tkinter import *
from PIL import Image, ImageTk

#tạo Tk windows
base = Tk()
base.title("Trợ lý ảo")
base.geometry("400x500")
base.iconbitmap('logo.ico')
base.resizable(width=FALSE, height=FALSE)


#box
ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial",)

ChatLog.config(state=DISABLED)

ChatLog.place(x=6,y=6, height=386, width=370)
base.mainloop()