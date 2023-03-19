import random

batarang = 0
batarang_minimum = 10
batsignal = True
mechants = {
    "joker",
    "l'epouvantail",
    "double-face",
    "bane",
    "harley queen",
}

if batsignal:
    print("le bat signal est allumé !")
    print("batman part à la rescousse")
    if batarang:
        0
    print("batman rest dans la batcave")
    while batarang < batarang_minimum:
        batarang += 1
    print("batman a asser de batarang")

    print("batman se demande quel énemi il va affronter")
    ennemis_aleatoires = random.sample(list(mechants), 1)
    for ennemi in ennemis_aleatoires:
        print("le bat-ordinateur indique que le mechant est " + ennemi)

else:
    print("le batsignal est éteint")


a = "j'ai une classe de 30 éleves"
print(a)

b = str(10) + " + " + str("5") + " est égale à " + str(15)
print(b)

c = 10 + 5
print(c)

d = "L'addition de 10 + 5 est égale à " + str(10 + 5)
print(d)

"Bonjour le jour".find("jour")


# mdp = input("Entrez un mot de passe ( min 8 caractères) : ")
# mdp_trop_court = "votre mot de passe est trop court."

# if len(mdp) < 0:
#     print(mdp_trop_court.upper())
# elif len(mdp) < 8:
#     print(mdp_trop_court.capitalize())
# elif mdp.isdigit():
#     print("Votre mot de passe ne contient que des nombres.")
# else:
#     print( "c'est ok")


# for i in range(10):
#     print("bonjour")


# i = 0
# while i < 100:
#     print("bonjour")
#     i += 1


# continuer = "o"
# while continuer == "o":
#     print("on continue...")
#     continuer = input("voulez vous continuer ? o/n ")


# démarre avec une liste vide


class ToolBox:
    """Boite à outils."""

    def __init__(self):
        """Initialise les outils."""
        self.tools = []

    def add_tool(self, tool):
        """Ajoute un outil."""
        self.tools.append(tool)

    def remove_tool(self, tool):
        """Enleve un outil."""
        index = self.tools.index(tool)
        del self.tools[index]


class Screwdriver:
    """Tournevis."""

    def __init__(self, size=3):
        """Initialise la taille."""
        self.size = size

    def tighten(self, screw):
        """Serrer une vis."""
        screw.tighten()

    def loosen(self, screw):
        """Desserre une vis."""
        screw.loosen()

    def __repr__(self):
        """Représentation de l'objet."""
        return f"Tournevis de taille {self.size}"


class Hammer:
    """Marteau."""

    def __init__(self, color="red"):
        """Initialise la couleur."""
        self.color = color

    def paint(self, color):
        """Paint le marteau."""
        self.color = color

    def hammer_in(self, nail):
        """Enfonce un clou."""
        nail.nail_in()

    def remove(self, nail):
        """Enleve un clou."""
        nail.remove()

    def __repr__(self):
        """Représentation de l'objet."""
        return f"Marteau de couleur {self.color}"


class Screw:
    """Vis."""

    MAX_TIGHTNESS = 5

    def __init__(self):
        """Initialise son degré de serrage."""
        self.tightness = 0

    def loosen(self):
        """Déserre le vis."""
        if self.tightness > 0:
            self.tightness -= 1

    def tighten(self):
        """Serre le vis."""
        if self.tightness < self.MAX_TIGHTNESS:
            self.tightness += 1

    def __str__(self):
        """Retourne une forme lisible de l'objet."""
        return "Vis avec un serrage de {}".format(self.tightness)


class Nail:
    """Clou."""

    def __init__(self):
        """Initialise son statut "dans le mur"."""
        self.in_wall = False

    def nail_in(self):
        """Enfonce le clou dans un mur."""
        if not self.in_wall:
            self.in_wall = True

    def remove(self):
        """Enlève le clou du mur."""
        if self.in_wall:
            self.in_wall = False

    def __str__(self):
        """Retourne une forme lisible de l'objet."""
        wall_state = "dans le mur" if self.in_wall else "hors du mur"
        return f"Clou {wall_state}."


hammer = Hammer()
screwdriver = Screwdriver()
toobox = ToolBox()

toobox.add_tool(hammer)
toobox.add_tool(screwdriver)


screw = Screw()
print(screw)
screwdriver.tighten(screw)
print(screw)
screwdriver.tighten(screw)
print(screw)


