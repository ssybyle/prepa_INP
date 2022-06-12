from math import *
import matplotlib.pyplot as plt
import numpy as np
import pendule_exact
'''
m : masse
l : longueur du fil
θ_ini : angle initial
ω_ini : vitesse initiale
T : période d'oscillation
n : nombre de θ qu'on calcule
'''

#Construction de la liste des θ et des énergies
def calcul_pendule_recg(ω_ini,θ_ini,T,l,m,n):
  g = 9.81
  h = T/n
  θk_1 = θ_ini
  θk = θ_ini+ω_ini*h
  θ = [θk_1,θk]
  ω = [ω_ini,(θk-θk_1)/h]
  for i in range(1,n-1):
    θkp1 = (h**2)*((-g/l)*sin(θk_1))+2*θk-θk_1
    ωkp1 = (θkp1-θk)/h
    θ.append(θkp1)
    ω.append(ωkp1)
    θk_1 = θk
    θk = θkp1
  Ec = []
  Ep = []
  for k in ω:
    Ec.append(0.5*m*(l**2)*(k**2))
  for k in θ:
    Ep.append(m*g*l*(1-cos(k)))
  Em = []
  for k in range(len(Ec)):
    Em.append(Ec[k]+Ep[k])
  return θ, ω, Ec, Ep, Em

#Calcul des erreurs
def calcul_erreurs(ω_ini,θ_ini,T,l,m):
  erreurs_tout_n = []
  tout_n = []
  n = 2
  while n<8001:
    θ_exact, ω_exact, Ec_exact, Ep_exact, Em_exact = pendule_exact.calcul_pendule_exact(ω_ini,θ_ini,T,l,m,n)
    θ, ω, Ec, Ep, Em = calcul_pendule_recg(ω_ini,θ_ini,T,l,m,n)
    erreurs = []
    for i in range(len(θ_exact)):
      erreurs.append(abs(θ_exact[i]-θ[i]))
    erreurs_tout_n.append(max(erreurs))
    tout_n.append(n)
    n+=500
  return tout_n, erreurs_tout_n
  
#Tracé des erreurs
def trace_erreurs(ω_ini,θ_ini,T,l,m):
  tout_n, erreurs_tout_n = calcul_erreurs(ω_ini,θ_ini,T,l,m)
  plt.figure(figsize=(3,3))
  plt.plot(tout_n, erreurs_tout_n, label="Erreurs(n)")
  plt.legend()

#Appel des fonctions
if __name__ == '__main__':
  ω_ini,θ_ini,T,l,m,n = 0,pi/16,5,1,1,2000
  θ, ω, Ec, Ep, Em = calcul_pendule_recg(ω_ini,θ_ini,T,l,m,n)
  pendule_exact.trace_theta(θ,T,n)
  pendule_exact.trace_energies(Ec,Ep,Em,T,n)
  pendule_exact.portrait_phase(θ, ω)
  trace_erreurs(ω_ini,θ_ini,T,l,m)
  plt.show()