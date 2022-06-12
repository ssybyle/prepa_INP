from pivot_gauss import *
import pytest

@pytest.fixture
def m1():
    return [[5, 6, 1, 8], [1, -3, 7, 2], [9, 4, 2, 0]]

@pytest.fixture
def m1bis():
    return [[1, 3, 9, 6], [4, 5, 1, 3], [3, 3, 0, 7]]

def test_est_matrice_valide_ok(m1):
    assert est_matrice_valide([[5]]) == (1, 1)
    assert est_matrice_valide(m1) == (3, 4)

def test_est_matrice_valide_ko(m1):
    assert not est_matrice_valide(7)
    assert not est_matrice_valide([5, 1])
    assert not est_matrice_valide([[5, 1], [1]])

def test_matrice_nulle():
    assert matrice_nulle(1, 1) == [[0]]
    assert matrice_nulle(1, 2) == [[0, 0]]
    assert matrice_nulle(3, 1) == [[0], [0], [0]]

def test_dilater(m1):
    dilater(m1, 1, 2.5)
    assert m1[1] == [2.5, -7.5, 17.5, 5.0]

def test_transvecter(m1):
    transvecter(m1, 2, 1, -2.5)
    assert m1[2] == [6.5, 11.5, -15.5, -5.0]

def test_permuter(m1):
    permuter(m1, 1, 2)
    assert m1 == [[5, 6, 1, 8], [9, 4, 2, 0], [1, -3, 7, 2]]

def test_matrice_augmentee():
    m1 = [[5, 3], [3, 7]]
    v2 = [1, 2]
    m3 = matrice_augmentee(m1, v2)
    assert m3 == [[5, 3, 1], [3, 7, 2]]

def test_colonne_1(m1bis):
    v2 = [3, 5, 3]
    assert colonne(m1bis, 1) == v2

def test_colonne_2(m1bis):
    v3 = [9, 1, 0]
    assert colonne(m1bis, 2) == v3

def test_sous_matrice_m_1_3(m1bis):
    assert sous_matrice(m1bis, 1, 3) == [[3, 9], [5, 1], [3, 0]]

def test_sous_matrice_m_2_3(m1bis):
    assert sous_matrice(m1bis, 2, 3) == [[9], [1], [0]]
