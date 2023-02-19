votes_soiree = {
    "Alice": ["Bob", "Esma", "Dylan"],
    "Bob": ["Carole", "Esma"],
    "Esma": ["Bob", "Alice"],
    "Fabien": ["Dylan"],
    "Carole": [],
    "Dylan":['Bob'],
}

def scores_aimes(votes):
    """
    Renvoie le dictionnaire dont les clés sont les personnes,
    et les valeurs le nombre de personnes qui leur ont attribué des J'aime.
    Prec : les éléments des listes de votes sont forcément des clefs du dictionnaire votes
    """
    aimes = {}
    for i in votes :
        aimes[i] = 0
    for i in votes :
        for i in votes[i]:
            aimes[i] = aimes[i] + 1
    return aimes

print(scores_aimes(votes_soiree))

#assert scores_aimes(votes_soiree)['Dylan'] == 2
#assert scores_aimes(votes_soiree)['Bob'] == 3
#assert scores_aimes(votes_soiree) == {'Alice': 1, 'Bob': 3, 'Esma': 2, 'Fabien': 0, 'Carole': 1, 'Dylan': 2}