"""Définit les films.
Note: l'utilisation de l'héritage ici est surtout à but éducatif.
"""


class Film:
    """Film."""

    def __init__(self, name, date, stream):
        """Initialise le nom et la date.
        L'attribut "where" permet de savoir où est un film.
        """
        self.name = name
        self.date = date
        self.where = None
        self.stream = stream

    def __str__(self):
        return f"{self.name} ({self.date}) ({self.stream})"

    def __repr__(self) -> str:
        return str(self)


class FilmVHF(Film):
    """Film VHF."""

    type = "vhf"

    def __init__(self, name, date, stream):
        """Initialise le type."""
        super().__init__(name, date, stream)
        self.magnetic_tape = True


class FilmDVD(Film):
    """Film DVD."""

    type = "dvd"

    def __init__(self, name, date, stream):
        """Initialise le type."""
        super().__init__(name, date, stream)
        self.mega_octets = 4700
        

    """rajout par rapport aux cours"""


class FilmPhysic(Film):
    
    type = "physique"

    def __init__(self, name, date, stream):
        uper().__init__(name, date, stream)


class FilmDemat(Film):

    type = "dématérialisé"

    def __init__(self, name, date, stream):
        uper().__init__(name, date, stream)

    """ fin rajout par rapport aux cours"""


class FilmCleaner:
    """Génère un film à partir de données brutes."""

    NAME_AND_DATE_INDEX = 0
    TYPE_INDEX = 1

    """rajout par rapport aux cours"""

    STREAMING_INDEX  = 2

    def __init__(self, film_data):
        self.film_data = film_data

    def generate(self):
        """Génère le film."""
        name = self.generate_name()
        date = self.generate_date()
        type = self.generate_type()
        stream = self.generate_stream()

        # ici on itère sur un tuple de classes (et non d'instances) !
        for Film in (FilmVHF, FilmDVD, FilmDemat, FilmPhysic):
            # on vérifie le type du film par rapport au type de chaque classe
            if type == Film.type:
                # et on retourne un instance de la classe choisie.
                return Film(name, date, stream)

    def generate_name(self):
        """Génère le nom."""
        name_date = self.film_data[self.NAME_AND_DATE_INDEX]
        return name_date[: name_date.index("(")].strip()

    def generate_date(self):
        """Génère la date."""
        name_date = self.film_data[self.NAME_AND_DATE_INDEX]
        # date_with_parenthesis = name_date[name_date.index("(") :]
        # date_letters = date_with_parenthesis.replace("(", "").replace(")", "")
        # return int(date_letters)

    def generate_type(self):
        """Génère le type."""
        return self.film_data[self.TYPE_INDEX].lower()

    """rajout par rapport au cours """

    def generate_stream(self):

        return self.film_data[self.STREAMING_INDEX]