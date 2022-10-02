def test_comprendre_dictionnaire():
    # Les noms de pays en fonction de leur code ISO 3166-1 alpha-2
    pays = { 'FR': 'France', 'DE' : 'Allemagne',
            'ES' : 'Espagne', 'GB' : 'Angleterre' }

    # Obtenir le pays 'Allemagne'
    assert 'Allemagne' == pays['DE']

    # Vérifier que le code 'IT' n'est pas défini dans pays.
    assert 'IT' not in pays

    # Que se passe-t-il si on veut récupérer le pays associé à 'IT' ?
    '''Il ne se passe rien car IT n'est pas dans pays'''

    # Obtenir le pays qui correspond à un code donné ('IT' ou 'FR' par exemple).
    # S'il n'y a pas de pays associé au code on obtiendra 'INCONNU'.
    for code, nom_attendu in (('FR', 'France'), ('IT', 'INCONNU')):
        assert nom_attendu == 'France' or 'INCONNU'   #retrouver le nom associé à code

    # Ajouter le nom 'Italie' associé au code 'IT'.
    pays['IT'] = 'Italie'
    assert 'IT' in pays # le code 'IT' est défini
    assert pays['IT'] == 'Italie'  # le pays associé est 'Italie'

    # Changer le pays associé à 'GB' pour mettre 'Royaume-Uni'
    pays.update({'GB' : 'Royaume-Uni'})
    assert 'Royaume-Uni' == pays['GB'] # le pays associé à 'GB' est "Royaume-Uni'

    # Obtenir tous les codes connus dans pays
    codes = pays.keys()
    print('Les codes :', codes)

    # Obtenir tous les noms de pays connus dans pays
    les_pays = pays.values()
    print('Les pays :', les_pays)

    # Obtenir tous les couples (code, nom) de pays
    couples = pays.items()
    print('Les couples :', couples)

    # Afficher le contenu de pays sous la forme : code -> pays
    for i in pays:
      print(i, '->', pays[i])

if __name__ == '__main__':
    test_comprendre_dictionnaire()
