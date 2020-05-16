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

#root.mainloop()











#canvas = Canvas(root, width=400, height=200)
#canvas.pack()

#image = ImageTk.PhotoImage(file="storm.jpg")
#canvas.create_image(0, 0, image=image, anchor=NW)

#canvas_id = canvas.create_text(10, 10, anchor="nw")
#canvas.itemconfig(canvas_id, text="this is the textjhsbafjshbdfjhabsdfhbajsdbfjhabsdfjhbasjdfhbjashdbfjashbfdjhasfbjahsbdfjhabsfd ")
#canvas.itemconfig(canvas_id, font=("Helvetica", 16), fg = 'white')
#canvas.insert(canvas_id, 12, "new ")


#pilfile = Image.open("storm.jpg")
#Image = ImageTk.PhotoImage(pilfile)
#ImageLabel = Label(root,image = Image, compound="center")
#ImageLabel.image = Image
#ImageLabel.pack()