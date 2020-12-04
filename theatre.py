import oeuvre

class Theatre(oeuvre.Oeuvre):
    """Gestion des pièces de théâtre"""
    def __init__(self, main):
        oeuvre.Oeuvre.__init__(main)
        self.typeO = "théâtre"