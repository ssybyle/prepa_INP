''''La fonction minimum.'''

def minimum(elt1, elt2):
    '''
    Renvoyer le plus petit des deux éléments en paramètre.

    :param elt1: le premier élément.
    :type elt1: un type quelconque équipé de '<'
    :param elt2: le deuxième élément.
    :type elt2: un type compatible avec celui de elt1 pour '<'
    :returns: le plus petit des deux éléments.
    '''
    if elt1 < elt2:
        return elt1
    else:
        return elt2
