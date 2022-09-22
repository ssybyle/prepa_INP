'''programme de test du tri par sélection'''

from tri_fusion import fusion, liste_triee

def test_nominal():
    assert [1, 2, 3, 4] == fusion([1, 3], [2, 4])
    assert [1, 2, 2, 3, 4] == fusion([1, 2, 3], [2, 4])

def test_une_liste_vide():
    assert [1, 2, 3, 4] == fusion([], [1, 2, 3, 4])
    assert [1, 2, 3, 4] == fusion([1, 2, 3, 4], [])

def test_deux_listes_vides():
    assert [] == fusion([], [])


def trier(liste):
    triee = liste_triee(liste)
    assert isinstance(triee, list)
    liste[:] = triee[:]

def test_enonce():
    v = [8, 2, 9, 5, 1, 7]
    trier(v)
    assert [1, 2, 5, 7, 8, 9] == v

def test_avec_doubles():
    v = [8, 2, 9, 2, 1, 8, 7]
    trier(v)
    assert [1, 2, 2, 7, 8, 8, 9] == v

def test_avec_plus_petit_a_la_fin():
    v = [8, 2, 9, 5, 1, 7, 0]
    trier(v)
    assert [0, 1, 2, 5, 7, 8, 9] == v

def test_vide():
    v = []
    trier(v)
    assert [] == v

def test_deja_trie():
    v = [range(10)]
    trier(v)
    assert [range(10)] == v

def test_string():
    v = ['chien', 'chat', 'canard', 'poule', 'lapin']
    trier(v)
    assert ['canard', 'chat', 'chien', 'lapin', 'poule'] == v


def verifier_trier(trier, liste):
    '''Vérifier l'exécution de la fonction « trier » appliquée sur une liste.

    :param trier: la fonction de tri
    :param liste: la liste à trier
    '''
    copie = list(liste)   # une copie de liste initiale
    trier(copie);
    # vérifier que copie est triée
    assert all(copie[i-1] <= copie[i] for i in range(1, len(copie)))
    # vérifier que copie est une permutation de elements 
    #    tous les éléments de 'elements' sont dans 'copie' avec le même nombre d'éléments
    assert all(liste.count(x) == copie.count(x) for x in set(liste))


def test_tri_statistique():
    from random import randint
    min, max = 0, 50
    for taille in (20, 100, 1000):
        for _ in range(10):
            liste = [randint(min, max) for _ in range(taille)]    # liste aléatoire
            verifier_trier(trier, liste)


def test_liste_inchangee():
    liste = [8, 2, 1, 7]               # la liste à trier
    copie = list(liste)                # garder une copie de liste
    triee = liste_triee(liste)         # la liste triée
    assert triee == [1, 2, 7, 8]       # le tri fonctionne
    assert triee is not liste          # nouvelle liste créée
    assert liste == copie              # liste initiale inchangée
