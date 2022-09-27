def somme(nom_fichier: str) -> float:
    '''
    La somme des nombres qui sont dans le fichier dont le nom est en paramètre.
    Il doit y avoir un et un seul nombre par line.

    :param nom_fichier: le nom du fichier qui contient les nombres
    :return: la somme des nombres contenu dans le fichier, un par ligne
    '''
    with open(nom_fichier) as fichier:
        somme = 0
        i = 1
        for ligne in fichier:
          try:
            nombre = float(ligne)
            somme = somme + nombre
          except ValueError:
            print("Ligne ignorée : " + ligne + "Numéro :", i)
          finally:
            i += 1
        return somme

def main():
    # Définir le nom du fichier
  try:
    import sys
    if len(sys.argv) == 2: # via la ligne de commande
      nom = sys.argv[1]   # le nom du fichier
    else:                  # via l'utilisateur du programme
      nom = input('Nom du fichier : ').strip()

    print(somme(nom))
  #except FileNotFoundError:
    #print("Le fichier n'existe pas.")
  except Exception as e:
    print("Il y a une erreur.", e)

if __name__ == '__main__':
    main()
