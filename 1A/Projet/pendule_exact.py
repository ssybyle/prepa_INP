from math import *
import matplotlib.pyplot as plt
import numpy as np
'''
m : masse
l : longueur du fil
θ_ini : angle initial
ω_ini : vitesse initiale
T : période d'oscillation
'''

#Construction de la liste des θ et des énergies
def calcul_pendule_exact(ω_ini, θ_ini, T, l, m, n):
  g = 9.81
  x = sqrt(g/l)
  temps = np.linspace(0,T,n)
  θ = []
  ω = []
  for t in temps:
    θ.append(θ_ini*cos(x*t)+ω_ini*(1/x)*sin(x*t))
    ω.append(-θ_ini*x*sin(x*t)+ω_ini*cos(x*t))
  Ec = []
  Ep = []
  for i in ω:
    Ec.append(0.5*m*(l**2)*(i**2))
  for i in θ:
    Ep.append(m*g*l*(1-cos(i)))
  Em = []
  for i in range(len(Ec)):
    Em.append(Ec[i]+Ep[i])
  return θ, ω, Ec, Ep, Em

#Tracé de θ
def trace_theta(θ, T, n):
  temps = np.linspace(0,T,n)
  plt.figure(figsize=(3,3))
  plt.plot(temps, θ, label="Thêta(t)")
  plt.legend()

#Tracé des énergies
def trace_energies(Ec, Ep, Em, T, n):
  temps = np.linspace(0,T,n)
  plt.figure(figsize=(3,3))
  plt.plot(temps, Ec, 'g', label="Energie cinétique(t)")
  plt.plot(temps, Ep, 'r', label="Energie potentielle(t)")
  plt.plot(temps, Em, 'm', label="Energie mécanique(t)")
  plt.legend()

#Portrait de phase
def portrait_phase(θ, ω):
  plt.figure(figsize=(3,3))
  plt.plot(θ, ω, label="ω(θ)")
  plt.legend()

#Pour que l'appel des fonctions ne s'exécute que dans ce fichier
if __name__ == '__main__':
  ω_ini,θ_ini,T,l,m,n = 7,0,5,1,1,2000
  θ, ω, Ec, Ep, Em = calcul_pendule_exact(ω_ini,θ_ini,T,l,m,n)
  trace_theta(θ, T, n)
  trace_energies(Ec, Ep, Em, T, n)
  portrait_phase(θ, ω)
  plt.show()
