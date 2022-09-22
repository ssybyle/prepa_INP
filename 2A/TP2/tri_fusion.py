'''Le tri fusion.'''


def liste_triee(liste):
    '''Retourner une nouvelle liste contenant les éléments
    de liste ordonnés du plus petit au plus grand.

    :param liste: la liste fournie
    :type liste: liste d'éléments comparables
    :return: une nouvelle liste triée
    '''
    if len(liste) <= 1:
      return liste
    moitie = int(len(liste)/2)
    liste1 = liste[:moitie]
    liste1_triee = liste_triee(liste1)
    liste2 = liste[moitie:]
    liste2_triee = liste_triee(liste2)
    return fusion(liste1_triee, liste2_triee)

def fusion(liste1, liste2):
    '''Retourne la liste qui la fusion des deux listes liste1 et liste2,
    deux listes triées dans l'ordre croissant.

    :param liste1: la première liste à fusionner
    :param liste2: la deuxième liste à fusionner
    :return: la fusion de liste1 et liste2
    :pre: liste1 et liste2 triées.
    :post: liste est triée, fusion de liste1 et liste2
    '''
    nouvelle_liste = []
    i1 = 0
    i2 = 0
    while i1 < len(liste1) and i2 < len(liste2):
      if liste1[i1] <= liste2[i2]:
        nouvelle_liste.append(liste1[i1])
        i1 += 1
      else:
        nouvelle_liste.append(liste2[i2])
        i2 += 1
    if i1 == len(liste1):
      nouvelle_liste.extend(liste2[i2:])
    else:
      nouvelle_liste.extend(liste1[i1:])
    return nouvelle_liste

print(liste_triee([5,3,2,9,6,4]))