def frequence_sequence(sequence, element):
    '''
    Retourne la fréquence d'un élément dans une séquence.

    :param sequence: séquence dans laquelle l'élément est cherché
    :param element: l'élément cherché
    :return: la fréquence de element dans sequence
    :type: int
    '''
    frequence = 0
    for i in range(len(sequence)):
      if sequence[i] == element:
        frequence += 1
    return frequence

def frequence_entier(nombre, chiffre):
    '''
    Retourne la fréquence d'un chiffre dans un nombre.

    :param nombre: un entier naturel
    :param element: l'élément cherché
    :return: la fréquence de element dans sequence
    :type: int
    :pre: nombre >= 0   # nombre est un entier naturel
    '''
    liste = [int(k) for k in str(nombre) if k.isdigit()]
    return frequence_sequence(liste, chiffre)