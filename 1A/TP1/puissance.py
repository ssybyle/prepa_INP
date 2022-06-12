def puissance_positive_iterative(nombre, exposant):
    '''
    Retourne nombre à la puissance exposant avec comme contrainte exposant
    positif.

    :param nombre: nombre à élever à la puissance (in)
    :type nombre: number (int ou float)
    :param exposant: l'exposant positif
    :type exposant: int
    :pre: exposant >= 0
    '''
    assert exposant >= 0
    if nombre == 0 and exposant == 0:
      return 1
    else:
      resultat = 1
      for i in range(exposant):
        resultat = resultat*nombre
      return resultat


def puissance_iterative(nombre, exposant):
    '''
    Retourne nombre à la puissance exposant.

    :param nombre: nombre à élever à la puissance (in)
    :type nombre: number (int ou float)
    :param exposant: l'exposant positif ou négatif
    :type exposant: int
    :pre: TODO: compléter...
    '''
    assert nombre != 0 or exposant >= 0
    if nombre == 0 and exposant == 0:
      return 1
    elif exposant > 0:
     return puissance_positive_iterative(nombre,exposant)
    else:
      return 1/puissance_positive_iterative(nombre, -exposant)


def puissance_recursive(nombre, exposant):
    """ 
    Même spécification que puissance_iterative
    """
    assert nombre != 0 or exposant >= 0
    if exposant == 0:
      return 1
    elif exposant > 0:
      return nombre * puissance_recursive(nombre, exposant-1)
    else:
      return 1/puissance_recursive(nombre, -exposant)


def puissance_positive_iterative_mieux(nombre, exposant):
    """ 
    Même spécification que puissance_positive_iterative
    """
    assert exposant >= 0
    if exposant == 0:
      return 1
    elif exposant > 0:
      if exposant % 2 == 0:
        p = exposant/2
        return puissance_positive_iterative(nombre**2,p)
      else:
        p = exposant/2 - 0.5
        return puissance_positive_iterative(nombre**2,p)*nombre
    else:
      if exposant % 2 == 0:
        p = exposant/2
        return 1/puissance_positive_iterative(nombre^2,-p)
      else:
        p = exposant/2 - 0.5
        return 1/puissance_positive_iterative(nombre^2,-p)


def puissance_recursive_mieux(nombre, exposant):
    """ 
    Même spécification que puissance_recursive
    """
    pass # TODO: à corriger...


def calculer_puissance_interactive_simple():
    import math
    nombre = float(input("nombre ? "))
    exposant = int(input("exposant ? "))
    fn_puissance = ( puissance_positive_iterative, puissance_iterative,
            puissance_recursive,
            puissance_positive_iterative_mieux, puissance_recursive_mieux,)
    for puissance in fn_puissance:
        print("{}({}, {}) = ".format(puissance.__name__, nombre, exposant), end='')
        if exposant < 0 and 'positive' in puissance.__name__:
            print('impossible.')
        else:
            resultat = puissance(nombre, exposant)
            print(resultat, end='')
            if resultat is None:
                print(' (non calculé ?)')
            else:
                attendu = nombre ** exposant    # oracle
                if math.isclose(resultat, attendu):
                    print(' (ok)')
                else:
                    print(' (ERREUR: attendu = {})'.format(attendu))


if __name__ == '__main__':
    calculer_puissance_interactive_simple()

