from __future__ import annotations # pour permettre les references
from typing import Callable
                                   # aux types non encore definis.
"""
%<*comment
commentaire
*</comment
"""
# Noeud_a_b #
class Noeud_a_b:
    def __init__(self, info: int, ab_g: Noeud_a_b = None, ab_d: Noeud_a_b = None) -> None:
        self.info = info
        self.f_g = ab_g
        self.f_d = ab_d


f2  = Noeud_a_b(2) # feuille sans fils
f5  = Noeud_a_b(5) # ""
n3  = Noeud_a_b(3,f2,f5) # noeud avec un fils gauche f2 et droit f5
f8  = Noeud_a_b(8)  # feuille 
n7  = Noeud_a_b(7,None,f8) # noeud avec un fils droit
n6  = Noeud_a_b(6,n3,n7)
# end #
# hauteur #
def hauteur(n:Noeud_a_b):
    if n is None:
        return 0
    else:
        return 1 + max(n.f_g,n.f_d)
# end #

# ParcoursInfixe #
def ParcoursInfixe(n:Noeud_a_b):
    if n is None:
        return
    else:
        ParcoursInfixe(n.ab_g)
        print(n.info,end = '')
        ParcoursInfixe(n.ab_d)
# end #

# ParcoursPrefixe #
def ParcoursPrefixe(n):
    if n is None:
        return
    else:
        print(n.info,end = '')
        ParcoursInfixe(n.ab_g)
        ParcoursInfixe(n.ab_d)
# end #

# ParcoursPostfixe #
def ParcoursPostfixe(n):
    if n is None:
        return
    else:
        ParcoursInfixe(n.ab_g)
        ParcoursInfixe(n.ab_d)
        print(n.info,end = '')
# end #

# ParcoursInfixeParametre #
def parcours_infixe_parametre(r: Noeud_a_b, traitement : Callable[[int]]) -> None:
    if r is None:
        return
    else:
        parcours_infixe_parametre(r.f_g, traitement)
        traitement(r.info)
        parcours_infixe_parametre(r.f_d, traitement)

parcours_infixe_parametre(n6,lambda x: print(x, end = ' '))
# end #

# ParcoursPrefixeParametre #
# ParcoursPrefixeParametre a faire
# end #

# ParcoursPostfixeParametre #
# ParcoursPrefixeParametre a faire
# end #

# gen_arbre_latex #

def gen_arbre_latex(n:Noeud_a_b,niveau:int) -> str:
    if n == None:
        return ""
    else:
        if niveau == 0:
            r = "\\node "
        else:
            r = "\t"*niveau + "node" # racine
        r = r = r + "{ " + str(n.info) + " }\n" 
        if n.f_g == None and n.f_d == None:
            return r
        if n.f_g == None:
            r = r + "\t"*niveau + "child[missing]  { node {}}\n"
        else:
            r = r + "\t"*niveau + "child  {"
            r = r + gen_arbre_latex(n.f_g,niveau+1)
            r = r + "\t"*niveau + "}\n"
        if n.f_d == None:
            r = r + "\t"*niveau + "child[missing]  { node {}}\n"
        else:
            r = r + "\t"*niveau + "child  {"
            r = r + gen_arbre_latex(n.f_d,niveau+1)
            r = r + "\t"*niveau + "}\n"
        return r
# end #

# gen_str_latex #
def gen_str_latex(n:Noeud_a_b):
    return "\\begin{tikzpicture}[scale = 0.4, sibling distance=10em,\n\
        every node/.style = {shape=rectangle, rounded corners,\n\
        draw, align=center,\n\
        top color=white, bottom color=blue!20}]]\n" + \
            gen_arbre_latex(n,0) + \
                ";\n " + "\\end{tikzpicture}\n"

f = open("chaine.tex", "w")
f.write(gen_str_latex(n6))
f.close()
# end #

# all_n #
def all_n(a:Noeud_a_b, pred:Callable[[int], bool] ):
    if a is None:
        return True
    else:
        return all_n(a.f_g,pred) and pred(a.info) and all_n(a.f_d,pred)
# end #

# ex_n #

def ex_n(a:Noeud_a_b, pred:Callable[[int], bool] ):
    if a is None:
        return False
    else:
        return ex_n(a.f_g,pred) or pred(a.info) or ex_n(a.f_d,pred)
# end #

# all_sa #
def all_sa(n:Noeud_a_b, pred:Callable[[Noeud_a_b], bool] ):
    if n is None:
        return True
    else:
        return all_sa(n.f_g) and pred(n) and all_sa(n.f_d)
# end #

# ex_sa #
def ex_sa(n:Noeud_a_b, pred:Callable[[Noeud_a_b], bool] ):
    if n is None:
        return False
    else:
        return  ex_sa(n.f_g) or pred(n) or ex_sa(n.f_d)
# end #

# propriete_racine_abr #
def propriete_racine_abr(n:Noeud_a_b) -> bool:
    return all_n(n.f_g, lambda x: x < n.info  ) and  \
           all_n(n.f_d, lambda x: x > n.info ) 
# end #

# propriete_abr #
def propriete_abr(n:Noeud_a_b) -> bool:
    return all_sa(n, propriete_racine_abr)
# end #

print(gen_str_latex(n6))