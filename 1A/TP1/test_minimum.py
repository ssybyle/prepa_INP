'''Programme de test de minimum.'''

from minimum import minimum

def test_min():
    '''Tests de minimum sur des entiers.'''
    assert 1 == minimum(1, 2)
    assert -5 == minimum(elt2=-3, elt1=-5)
    assert -2 == minimum(6, -2)
    assert 9 == minimum(9, 9)

def test_min_chaines():
    '''Test de minimum sur des chaînes de caractères.'''
    assert 'chat' == minimum('chat', 'chien')
