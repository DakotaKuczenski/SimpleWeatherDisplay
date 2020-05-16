from tkinter import * 
import tkinter as tk
import infoAPI as ap
import PIL
from PIL import ImageTk, Image # will implement in future. 
import time 

class app():
    def __init__(self):
        root = tk.Tk()
        root.title('My Weather')
        root.geometry("200x100")
        out = ap.location()
        
        w = Label(root, text= out[0],fg = 'white', font=("Helvetica", 16), background = 'black' ) 
        e = Label(root, text= out[1],fg = 'white', font=("Helvetica", 16), background = 'black' )
        k = Label(root, text= str(out[2]) + ' F',fg = 'white', font=("Helvetica", 16), background = 'black' )

        w.pack()
        k.pack()
        e.pack()

        root.mainloop()

app=app()
