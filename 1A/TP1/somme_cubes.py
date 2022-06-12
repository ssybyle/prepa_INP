def somme_cubes_sequence(sequence):
    '''
    Retourne la somme des cubes des éléments d'une séquence.

    :param sequence: une séquence de nombre
    :return: la somme des cubes des éléments d'une séquence
    :type: nombre
    '''
    somme = 0
    for i in range(len(sequence)):
      somme += (sequence[i])**3
    return somme

def somme_cubes_entier(nombre):
    '''
    Retourne la somme des cubes des chiffres d'un nombre.

    :param nombre: un entier naturel
    :return: la somme des cubes des chiffres de nombre
    :type: nombre
    :pre: nombre >= 0   # nombre est un entier naturel
    '''
    assert nombre >= 0
    liste = [int(k) for k in str(nombre) if k.isdigit()]
    somme = somme_cubes_sequence(liste)
    return somme
