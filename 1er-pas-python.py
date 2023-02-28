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
