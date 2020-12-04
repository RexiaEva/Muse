# -*-coding:utf8 -*
from tkinter import *
from tkinter import ttk

import cm
import film
import jeu
import livre
import nouvelle
import pub
import roman
import theatre
import video

class Thot(Tk):
    """L'appication qui gère tout les documents"""
    
    def __init__(self, fenetre, **kwargs):
        Tk.__init__(self)
        self.title("Thot") # changer le titre de la fenêtre
        self.geometry("1080x900") # changer les dimension de la fenêtre
        self.minsize(480, 360) # fixer la taille min de la fenêtre
        self.iconbitmap("thot.ico") # donner l'url du l'icone
        self.config(background='#000000') # Donner la couleur de fond

        self.main = Frame(fenetre, padding="4 4 4 4", background='#E2BC74') # On déclare la frame principale
        self.main.pack(fill=BOTH)
        fenetre.columnconfigure(0, weight=1)
        fenetre.rowconfigure(0, weight=1)
        



        self.Titre = Label(self.main, text="Bienvenue dans Thot", font=("Times New Roman", 32), bg='#FEFEFE', fg='#850606')
        self.Titre.pack(side=TOP)

        self.fenIntro = Label(self.main, text="Un logiciel de traitement de text indépendant et surtout libre.", font=("Times New Roman", 16), bg='#FEFEFE', fg='#000000')
        self.fenIntro.pack(side=TOP)




        self.cadreDoc = Frame(self.main, bg='#E0CDA9')
        self.cadreDoc.pack(expand=YES)

        self.cadreDocTitre = Label(self.cadreDoc, text="Document", font=("Times New Roman", 16), bg='#FEFEFE', fg='#000000')
        self.cadreDocTitre.pack(side=TOP)

        self.docs = ["Brouillon", "Compte-rendu, résumé, synthèse", "Devoirs de maths ou une autre science", "Devoirs littéraire ou d'histoire", "Lettre", "Rapports, thèse"]
        self.docsB = list()
        for i, doc in enumerate(self.docs):
            self.docsB.append(Button(self.cadreDoc, text=doc, font=('Times New Roman', 16), bg="#000000", fg='#FEFEFE'))
            self.docsB[i].pack()




        self.cadreMuse = Frame(self.main, bg='#E1CE9A')
        self.cadreMuse.pack(expand=YES)

        self.cadreMuseTitre = Label(self.cadreMuse, text="Muse", font=("Times New Roman", 16), bg='#FEFEFE', fg='#000000')
        self.cadreMuseTitre.pack(side=TOP)

        self.muses = ["Film", "Court-métrage", "Vidéo", "Pub", "Livre", "Roman", "Nouvelle", "Pièce de théâtre", "Jeu"]
        self.musesF = [lambda: film.Film(self), lambda: cm.CM(self), lambda: video.Video(self), lambda: pub.Pub(self), lambda: livre.Livre(self), lambda: roman.Roman(self), lambda: nouvelle.Nouvelle(self), lambda: theatre.Theatre(self), lambda: jeu.Jeu(self)]
        self.musesB = list()
        for i, muse in enumerate(self.muses):
            self.musesB.append(Button(self.cadreMuse, text=muse, command=self.musesF[i], font=('Times New Roman', 16), bg="#000000", fg='#FEFEFE'))
            self.musesB[i].pack()

        self.cadreMuseTitre2 = Label(self.cadreMuse, text="Élément histoire", font=("Times New Roman", 16), bg='#FEFEFE', fg='#000000')
        self.cadreMuseTitre2.pack()

        self.muses2 = ["Personnage"]
        self.muses2B = list()
        for i, muse in enumerate(self.muses2):
            self.muses2B.append(Button(self.cadreMuse, text=muse, font=('Times New Roman', 16), bg="#000000", fg='#FEFEFE'))
            self.muses2B[i].pack()

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

if __name__ == "__main__":
    # creer la fenêtre
    window = Tk()
    Thot(window)
    # afficher la fenêtre
    window.mainloop()
