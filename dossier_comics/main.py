from pprint import pprint

from all_comics.comics import Comics
from all_comics.library import Biblio

def main():

    biblio = Biblio()

    comics = biblio.comics

    print("mes comics préféré: ")
    pprint(comics)


if __name__ == "__main__":
    main()