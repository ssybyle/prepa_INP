'''Programme de test de puissance_iterative'''

'''Ce programme est engendré automatiquement.'''

from puissance import puissance_iterative as puissance
import pytest

if puissance(1, 1) is None:

    def test_puissance_iterative():
        assert False, "puissance_iterative n'est pas définie !"

else:
    # Tests avec des expostants positifs

    def test_nominal_sujet():
        assert 64 == puissance(4, 3)

    def test_nominal_entier_negatif():
        assert 9 == puissance(-3, 2)
        assert -8 == puissance(-2, 3)
        assert 1 == puissance(-1, 50);
        assert -1 == puissance(-1, 51);

    def test_nominal_reel():
        assert 1.44 == puissance(1.2, 2)
        assert .125 == puissance(.5, 3)

    def test_exposant_nul():
        assert 1 == puissance(-5, 0)
        assert 1 == puissance(7.3, 0)
        assert 1 == puissance(0, 0)

    def test_bon_type_int():
        p = puissance(4, 3)
        assert isinstance(p, int)

    def test_bon_type_float():
        p = puissance(4.0, 3)
        assert isinstance(p, float)

    def test_sur_complexe():
        assert -1j == puissance(1j, 3)


    # Tests avec de grands exposants

    def test_grand_exposant():
        assert 1 == puissance(-1, 900);
        assert -1 == puissance(-1, 901);

    def test_plus_grand_exposant():
        assert 1 == puissance(-1, 1000);
        assert -1 == puissance(-1, 1001);

    def test_tres_grand_exposant():
        assert 1 == puissance(-1, 100000);
        assert -1 == puissance(-1, 100001);



    # Tests des exposants négatifs

    def test_exposant_negatif():
        assert .25 == puissance(2, -2)
        assert 16.0 == puissance(-.5, -4)
        assert -32.0 == puissance(-.5, -5)

