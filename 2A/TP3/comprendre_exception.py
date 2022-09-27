'''Comprendre les exceptions.'''

def ecrire(objet):
    '''afficher l'objet sans retour à la ligne'''
    print(objet, end='')

def f2(p: str) -> None:
    ecrire('<')
    if p is None:
        raise ValueError('must not be None')
    if not isinstance(p, str):
        raise TypeError('str expected but type is ' + str(type(p)))
    ecrire(p[0])
    ecrire(p[1])
    ecrire('>')

def f1(p1: str) -> None:
    ecrire('[')
    try:
        ecrire('(')
        f2(p1)
        ecrire(')')
    except ValueError:
        ecrire('V')
    except TypeError:
        ecrire('T')
    finally:
        ecrire('F')
    ecrire(']')
