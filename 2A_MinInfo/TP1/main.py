from __future__ import annotations

class Noeud_a_b:
  def __init__(self, info: int, ab_g: Noeud_a_b = None, ab_d: Noeud_a_b = None) -> None:
    self.info = info
    self.f_g = ab_g
    self.f_d = ab_d

def hauteur(r: Noeud_a_b) -> int:
  if r is None:
    return 0
  else:
    return max(hauteur(r.f_g), hauteur(r.f_d)) + 1

def parcours_inf(ra, aff):
  if ra is None:
    pass
  else:
    parcours_inf(ra.f_g, aff)
    aff(ra.info)
    parcours_inf(ra.f_d, aff)

def parcours_pref(ra, aff):
  if ra is None:
    pass
  else:
    aff(ra.info)
    parcours_inf(ra.f_g, aff)
    parcours_inf(ra.f_d, aff)

def parcours_post(ra, aff):
  if ra is None:
    pass
  else:
    parcours_inf(ra.f_g, aff)
    parcours_inf(ra.f_d, aff)
    aff(ra.info)

def aff(x):
  print(x, end = ' ')

def all_n(ra, p):
  if ra is None:
    return True
  elif p(ra):
    return all_n(ra.f_g, p) and all_n(ra.f_d, p)
  else:
    return False

def ex_n(ra, p):
  if ra is None:
    return False
  elif not p(ra):
    return ex_n(ra.f_g, p) or ex_n(ra.f_d, p)
  else:
    return True

def noeud_bin_rech(ra):
  return all_n(ra.f_g, lambda x: x.info < ra.info) and all_n(ra.f_d, lambda x: x.info > ra.info)

def arbre_bin_rech(ra):
  return all_n(ra, noeud_bin_rech)

Ouisticram = Noeud_a_b(3, None, None)
Salameche = Noeud_a_b(5, None, None)
Tiplouf = Noeud_a_b(1, None, None)
Tortank = Noeud_a_b(3, Tiplouf, Salameche)
Tortipousse = Noeud_a_b(7, Ouisticram, None)
Racine = Noeud_a_b(6, Tortank, Tortipousse)

'''parcours_inf(Racine, aff)
parcours_pref(Racine, aff)
parcours_post(Racine, aff)
print(hauteur(Racine))
print(arbre_bin_rech(Racine))'''