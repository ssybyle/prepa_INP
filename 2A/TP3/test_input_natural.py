import pytest
from unittest.mock import patch, call # non trouvé : pip install unittest
from natural import natural, SignError, input_natural


@patch('builtins.input', return_value='0')
def test_input_natural_nominal0(mockinput):
    assert 0 == input_natural('Nombre ? ')

@patch('builtins.input', return_value='18')
def test_input_natural_nominal18(mockinput):
    assert 18 == input_natural('Age ? ')

@patch('builtins.print')
@patch('builtins.input', side_effect=['abc', '18'])
def test_input_natural_nominal_erreur(mockinput, mockprint):
    assert 18 == input_natural('Age ? ')
    assert mockprint.mock_calls == [ call("Un entier est attendu.") ]


@patch('builtins.print')
@patch('builtins.input', side_effect=['-5', 'abc', '-9', '7'])
def test_input_natural_nominal_erreur(mockinput, mockprint):
    assert 7 == input_natural('Age ? ')
    assert mockprint.mock_calls == [
                call("Un entier positif est attendu."),
                call("Un entier est attendu."),
                call("Un entier positif est attendu."),
            ]
