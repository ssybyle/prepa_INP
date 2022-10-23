import graphviz

# Graphe #
class Graphe:
  def __init__(self, noeuds, arcs):
    self.noeuds = noeuds
    self.adj = { n: tuple([a[1] for a in arcs if a[0] == n]) for n in noeuds }
    self.prec = { n: tuple([a[0] for a in arcs if a[1] == n]) for n in noeuds }
    self.arcs = arcs
    self.noeuds_prec={ n:[a[0] for a in arcs if a[1] == n] for n in noeuds }
    self.noeuds_adj = { n:[a[1] for a in arcs if a[0] == n] for n in noeuds }
    self.au_plus_tot = {}
    self.au_plus_tard = {}

  def debut_au_plus_tot(self, noeud):
    "calcule la date de début de la tâche au plus tôt"
    if noeud in self.au_plus_tot:
      return self.au_plus_tot[noeud]
    if len(self.noeuds_prec[noeud]) == 0:
      self.au_plus_tot[noeud] = 0
      return 0
    au_plus_tot = max([self.debut_au_plus_tot(prec) + self.noeuds[prec] for prec in self.noeuds_prec[noeud]])
    self.au_plus_tot[noeud] = au_plus_tot
    return au_plus_tot

  def debut_au_plus_tard(self, noeud):
    "calcule la date de début de la tâche au plus tard"
    if noeud in self.au_plus_tard:
      return self.au_plus_tard[noeud]
    if len(self.noeuds_adj[noeud]) == 0:
      debut_au_plus_tard = self.debut_au_plus_tot(noeud)
      self.au_plus_tard[noeud] = debut_au_plus_tard
      return debut_au_plus_tard
    fin_au_plus_tard = min([self.debut_au_plus_tard(adj) for adj in 
self.noeuds_adj[noeud]])
    debut_au_plus_tard = fin_au_plus_tard - self.noeuds[noeud]
    self.au_plus_tard[noeud] = debut_au_plus_tard 
    return debut_au_plus_tard

  def est_critique(self, noeud):
    "vérifie si une tâche est critique"
    return self.debut_au_plus_tot(noeud) == self.debut_au_plus_tard(noeud)

  def taches_critiques(self):
    "crée la liste des tâches critiques"
    return [n for n in self.noeuds if self.est_critique(n)]
    
  def chemin_critique(self):
    "crée le chemin entre les tâches critiques"
    return [a for a in self.arcs if self.est_critique(a[0]) and 
            self.est_critique(a[1])]
#xxx

# Faisabilite #
  def existence_chemin(self, debut:str, fin:str):
    "vérifie s'il existe un chemin d'un noeud début à un noeud fin"
    chemin = [debut]
    visite = []  #garde en mémoire tous les noeuds visités
    while chemin != []:
      noeud_actuel = chemin.pop(0)
      visite.append(noeud_actuel)
      for i in self.noeuds:  #Pour chaque noeud on regarde:
        if i in self.adj[noeud_actuel] and i not in visite: #s'il s'agit de la suite du chemin, càd si le noeud_actuel amène à i
          chemin.append(i)
          visite.append(i)
        elif i in self.adj[noeud_actuel] and i == fin: #si le chemin existe, càd si le noeud_actuel amène au noeud fin
          return True
    return False

  def cycle(self):
    "vérifie s'il y a un cycle, c'est-à-dire regarde s'il existe un chemin d'un noeud à lui-même, pour chaque noeud du graphe"
    for i in self.noeuds:
      if self.existence_chemin(i,i) == True:
        return 'Le graphe contient un cycle!'
    return None

  def faisabilite(self):
    "vérifie l’ordonnancement des tâches"
    erreurs = []
    for i in self.noeuds.keys():
      if i == 'D': #vérifie que le départ est la première étape et en amène à une autre 
        existe1 = False
        existe2 = True 
        for k in self.arcs:
          if k[0] == i:
            existe1 = True
          if k[1] == i:
            existe2 = False
        if existe1 == False:
          erreurs.append("Le départ n'amène vers aucune autre étape")
        if existe2 == False:
          erreurs.append("Le départ donné n'est pas la première tâche")
      elif i == 'F': #vérifie que la fin est la dernière étape et est atteinte par une autre 
        existe1 = False
        existe2 = True
        for k in self.arcs:
          if k[1] == i:
            existe1 = True
          if k[0] == i:
            existe2 = False
        if existe1 == False:
          erreurs.append("Le fin n'est atteinte par aucune autre étape")
        if existe2 == False:
          erreurs.append("La fin donnée n'est pas la dernière tâche")
      else: #vérifie que chaque étape intermédiaire est atteinte par une autre et amène à une autre
        existe1 = False
        existe2 = False
        for k in self.arcs:
          if k[0] == i:
            existe1 = True
          if k[1] == i :
            existe2 = True
        if existe1 == False:
          erreurs.append(f"L'étape {i} n'amène vers aucune autre étape")
        if existe2 == False:
          erreurs.append(f"L'étape {i} n'est atteinte par aucune autre étape")
    if self.cycle() != None:
      
      erreurs.append(self.cycle())
    return len(erreurs) == 0, erreurs
#xxx

# Generateur #
  def graphe_generator(self):
    "crée un graphe"
    dot = graphviz.Digraph(comment='PERT')

    taches_critiques = set(self.taches_critiques())

    for noeud in self.noeuds:
      if noeud not in taches_critiques:
        dot.node(noeud, f"{noeud}\ndurée:{self.noeuds[noeud]}\ndébut:\ntôt:T+{self.au_plus_tot[noeud]}\ntard:T+{self.au_plus_tard[noeud]}")

    dot.attr('node', color='red')    #On modifie la couleur des noeuds contenants les tâches critiques
    for noeud in taches_critiques:
      dot.node(noeud, f"{noeud}\ndurée:{self.noeuds[noeud]}\ndébut:\ntôt:T+{self.au_plus_tot[noeud]}\ntard:T+{self.au_plus_tard[noeud]}")

    chemin_critique = set(self.chemin_critique())
  
    for arc in self.arcs:
      if arc not in chemin_critique:
        dot.edge(arc[0], arc[1])
      
    dot.attr('edge', color='red')    #On modifie la couleur des flèches reliant les tâches critiques
    for arc in chemin_critique:
      dot.edge(arc[0], arc[1])
  
    dot.view()




if __name__ == "__main__":
  with open ("fichier.txt") as fichier:
    donnees = {ligne.split()[0] : int(ligne.split()[1]) for ligne in fichier}
  
  with open ("precedence.txt") as fichier:
    precedence = {(ligne.split()[0], ligne.split()[2]) for ligne in fichier}

  PERT = Graphe(donnees, precedence)
  
  (faisable,erreurs) = PERT.faisabilite()
  if not(faisable):
    print(erreurs)
    exit(1)

  PERT.graphe_generator()
#xxx