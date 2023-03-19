import random
from .comics import ComicsData
from .data import comics


class Biblio:

    def __init__(self):
        self.comics = []
        for comic_data in comics:
            comic = ComicsData(comic_data).generate()
            comic.where = self
            self.comics.append(comic)

        self.sort_by_all_attributes()

    def sort_by_all_attributes(self):
        self.comics.sort(key=lambda comic: (comic.personnage,
                         comic.adge_of_parution, comic.name))
