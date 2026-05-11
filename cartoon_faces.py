from tkinter import Label
from PIL import Image, ImageTk
from tkinter import Label
from PIL import Image, ImageTk
class CartoonFaces:
    def __init__(self, parent):
        self.parent = parent     
        self.normal_img = ImageTk.PhotoImage(
            Image.open("normal.png").resize((120, 120)),
            master=parent
        )
        self.sad_img = ImageTk.PhotoImage(
            Image.open("sad.png").resize((120, 120)),
            master=parent
        )
        self.win_img = ImageTk.PhotoImage(
            Image.open("win.png").resize((140, 140)),
            master=parent
        )
        self.label = Label(parent, image=self.normal_img, bg="#1e1e2f")
        self.label.image = self.normal_img
        self.label.pack(side="right", padx=20, pady=20)
    # Showing normal face
    def show_normal(self):
        self.label.config(image=self.normal_img)
        self.label.image = self.normal_img
    # Showing sad face
    def show_sad(self):
        self.label.config(image=self.sad_img)
        self.label.image = self.sad_img
    # Showing win face
    def show_win(self):
        self.label.config(image=self.win_img)
        self.label.image = self.win_img