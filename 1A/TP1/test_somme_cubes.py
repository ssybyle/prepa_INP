from somme_cubes import somme_cubes_sequence, somme_cubes_entier

def test_somme_cubes_entier():
    assert somme_cubes_entier(5) == 125
    assert somme_cubes_entier(0) == 0
    assert somme_cubes_entier(10) == 1
    assert somme_cubes_entier(121) == 10


def test_somme_cubes_sequence():
    assert somme_cubes_sequence([5]) == 125
    assert somme_cubes_sequence([0, 5, 0, 1]) == 126
    assert somme_cubes_sequence([]) == 0
    assert somme_cubes_sequence([1, 0]) == 1
    assert somme_cubes_sequence([1, 2, 1, 10]) == 1010
