import film

class Video(film.Film):
    """Gestion des vidéos"""
    def __init__(self, main):
        film.Film.__init__(main)
        self.typeO = "vidéo"
        fenetre.title("Thot - Création de {}".format(self.typeO))


if __name__ == "__main__":
    # creer la fenêtre
    window = Tk()

    # personnaliser la fenetre
    window.title("Thot – scénario de vidéo") # changer le titre de la fenêtre
    window.geometry("1080x800") # changer les dimension de la fenêtre
    window.minsize(480, 360) # fixer la taille min de la fenêtre
    window.iconbitmap("thot.ico") # donner l'url du l'icone
    window.config(background='#000000') # Donner la couleur de fond

    # creer la frame
    accueil = Accueil(window, bg='#E2BC74')
    accueil.pack(expand=YES)

    # afficher la fenêtre
    window.mainloop()
