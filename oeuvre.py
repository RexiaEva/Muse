import tkinter

def lab(parent)

class Oeuvre(tkinter.Frame):
    """Gestion des œuvres"""
    def __init__(self, fenetre):
        tkinter.Frame.__init__(self, fenetre, bg='#E1CE9A', cursor='pencil')

        labNom = Entry(self)

        fenetre.switch_frame(self)