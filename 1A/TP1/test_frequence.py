from frequence import frequence_sequence, frequence_entier

def test_frequence_entier():
    assert frequence_entier(5, 5) == 1
    assert frequence_entier(5, 1) == 0
    assert frequence_entier(5, 0) == 0
    assert frequence_entier(10, 1) == 1
    assert frequence_entier(121, 1) == 2
    assert frequence_entier(0, 5) == 0
    assert frequence_entier(0, 0) == 1


def test_frequence_sequence():
    assert frequence_sequence([5], 1) == 0
    assert frequence_sequence([5], 5) == 1
    assert frequence_sequence([0, 5, 0, 1], 0) == 2
    assert frequence_sequence([0, 5, 0, 1], 1) == 1
    assert frequence_sequence([0, 5, 0, 1], 5) == 1
    assert frequence_sequence([101, 99], 99) == 1
    assert frequence_sequence([101, 99], 100) == 0
    assert frequence_sequence([], 5) == 0
