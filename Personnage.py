# -*-coding:utf8 -*
"""Premier exemple avec Tkinter.

On crée une fenêtre simple qui souhaite la bienvenue à l'utilisateur.

"""

# On importe Tkinter
from tkinter import *


if __name__ == "__main__":
# On crée une fenêtre, racine de notre interface
fenetre = Tk()

# On crée un label (ligne de texte) souhaitant la bienvenue
# Note : le premier paramètre passé au constructeur de Label est notre
# interface racine
ligne1 = Label(fenetre, text="Création de personnage")

# On affiche le label dans la fenêtre
ligne1.pack()

ligne2 = Label(fenetre, text="Prénom et surnom")
ligne2.pack()
var_texte = StringVar()
ligne_texte = Entry(fenetre, textvariable=var_texte, width=30)
ligne_texte.pack()

ligne3 = Label(fenetre, text="Document")
ligne3.pack()

bouton_1_1 = Button(fenetre, text="Brouillon", command=fenetre.quit)
bouton_1_1.pack()

bouton_1_2 = Button(fenetre, text="Compte-rendu, synthèse", command=fenetre.quit)
bouton_1_2.pack()

bouton_1_3 = Button(fenetre, text="Devoirs de maths ou une autre science", command=fenetre.quit)
bouton_1_3.pack()

bouton_1_4 = Button(fenetre, text="Devoirs littéraire ou d'histoire", command=fenetre.quit)
bouton_1_4.pack()

bouton_1_5 = Button(fenetre, text="Lettre", command=fenetre.quit)
bouton_1_5.pack()

bouton_1_6 = Button(fenetre, text="Rapports, thèse", command=fenetre.quit)
bouton_1_6.pack()

ligne4 = Label(fenetre, text="Muse")
ligne4.pack()

bouton_2_1 = Button(fenetre, text="Court-métrage", command=fenetre.quit)
bouton_2_1.pack()

bouton_2_2 = Button(fenetre, text="Film", command=fenetre.quit)
bouton_2_2.pack()

bouton_2_3 = Button(fenetre, text="Jeu", command=fenetre.quit)
bouton_2_3.pack()

bouton_2_4 = Button(fenetre, text="Nouvelle", command=fenetre.quit)
bouton_2_4.pack()

bouton_2_5 = Button(fenetre, text="Pub", command=fenetre.quit)
bouton_2_5.pack()

bouton_2_6 = Button(fenetre, text="Roman", command=fenetre.quit)
bouton_2_6.pack()

# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()