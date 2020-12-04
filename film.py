import theatre

class Film(theatre.Theatre):
    """Gestion des films"""
    def __init__(self, main):
        theatre.Theatre.__init__(main)
        self.typeO = "film"