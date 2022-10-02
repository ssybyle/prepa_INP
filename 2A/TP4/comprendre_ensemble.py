def test_comprendre_ensembles():
    # initialiser une variable nombres avec l'ensemble qui contient 1, 2, 3 et 2.
    nombres = {1,2,3,2}

    # vérifier la taille de l'ensemble (le nombre d'éléments qu'il contient)
    assert len(nombres) == 3

    # vérifier si l'élément 2 est présent dans l'ensemble
    assert 2 in nombres

    # vérifier si l'élément 5 est présent dans l'ensemble
    assert not 5 in nombres

    # ajouter 33 dans l'ensemble.  Quelle est la taille de l'ensemble ?
    nombres.add(33)
    assert len(nombres) == 4 # taille de nombres
    assert 33 in nombres # 33 est dans l'ensemble

    # ajouter 2 dans l'ensemble. Quelle est sa taille ?
    nombres.add(2)
    assert len(nombres) == 4

    # supprimer l'élément 2 de l'ensemble.
    nombres.discard(2)

    # vérifier si 2 est encore dans l'ensemble
    assert not 2 in nombres

    # vérifier la taille de l'ensemble
    assert len(nombres) == 3

    # supprimer l'élément 7 de l'ensemble.
    nombres.discard(7)

    # Soient e1 et e2 les deux ensembles suivants :
    e1 = {1, 2, 3}
    e2 = {2, 3, 4, 5}

    # intersection de e1 et e2
    assert {2, 3} == e1 & e2

    # union de e1 et e2
    assert {1, 2, 3, 4, 5} == e1 | e2

    # les éléments de e1 qui ne sont pas dans e2 ?
    assert {1} == e1 - e2 

    # les éléments qui sont dans e1 ou e2 mais pas dans l'intersection
    assert {1, 4, 5} == e1 ^ e2

    # créer un ensemble vide (appelé e)
    e = set()

    assert isinstance(e, set)     # e doit être du type set (ensemble)
    assert len(e) == 0            # l'ensemble e est vide
    assert e1 == {1, 2, 3}        # e1 non modifié
    assert e2 == {2, 3, 4, 5}     # e1 non modifié

if __name__ == '__main__':
    test_comprendre_ensembles()