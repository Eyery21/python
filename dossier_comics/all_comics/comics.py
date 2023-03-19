class Comics:

    """methode"""

    def __init__(self,personnage, adge_of_parution, name, page, price, type_of_comics):

        self.personnage = personnage
        self.adge_of_parution = adge_of_parution
        self.name = name
        self.page = page
        self.price = price

        self.tytype_of_comics =type_of_comics

    """permet de maitriser le rendu des donnés"""

    def __str__(self):
        return f"{self.personnage}, {self.adge_of_parution}, {self.name}, ({self.page}), ({self.price}), ({self.tytype_of_comics})"

    def __repr__(self) -> str:
        return str(self)




class ComicsData:
    PERSONNAGE_INDEX = 0
    PARUTION_INDEX = 1
    NAME_INDEX = 2
    PAGE_INDEX = 3
    PRICE_INDEX = 4
    TYPE_INDEX = 5

    def __init__(self, comics_data):
        self.comics_data = comics_data

    def generate(self):
        personnage = self.generate_perso()
        parution = self.generate_parution()
        name = self.generate_name()
        page = self.generate_page()
        price = self.generate_price()
        type_of_comics = self.generate_type()

        return Comics(personnage, parution, name, page, price, type_of_comics)

    def generate_perso(self):
        return self.comics_data[self.PERSONNAGE_INDEX]

    def generate_parution(self):
        return self.comics_data[self.PARUTION_INDEX]

    def generate_name(self):
        return self.comics_data[self.NAME_INDEX]

    def generate_page(self):
        return self.comics_data[self.PAGE_INDEX]

    def generate_price(self):
        return self.comics_data[self.PRICE_INDEX]

    def generate_type(self):
        return self.comics_data[self.TYPE_INDEX]