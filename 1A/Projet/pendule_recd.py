from math import *
import matplotlib.pyplot as plt
import numpy as np
import pendule_exact
'''
x: θk+1
Ɛ: précision qu'on veut atteindre dans la méthode de Newton
u: approximation de θk+1 par la methode de Newton
'''

#Fonction f(θ)
def f(x,l):
  g=9.81
  return (-g/l)*sin(x)

#Fonction g0(θ1)
def g0(x,l,ω_ini,θ_ini,h):
  return (h**2)*f(x,l)-x+θ_ini+h*ω_ini
  
#Fonction gk(θk+1)
def gk(x,l,θk,θk_1,h):
  return (h**2)*f(x,l)-x+2*θk-θk_1

#Dérivée de la fonction gk(θk+1)
def gk_prime(x,l,h):
  g=9.81
  return -g/l*(h**2)*cos(x)-1

#Méthode de Newton pour θkp1 
def Newton_θkp1(fonction,dérivée,θk,θk_1,l,h,Ɛ):
  u=θk
  while abs(fonction(u,l,θk,θk_1,h))>Ɛ:
    u=u-fonction(u,l,θk,θk_1,h)/dérivée(u,l,h)
  return u

#Construction de la liste des θ et des énergies
def calcul_pendule_recd(ω_ini,θ_ini,l,m,n,h,Ɛ):
  g=9.81
  θk_1=θ_ini
  θk=Newton_θkp1(g0,gk_prime,ω_ini,θ_ini,l,h,Ɛ)
  θ = [θk_1,θk]
  ω = [ω_ini,(θk-θk_1)/h]
  for i in range (1,n-1):
    θkp1 = Newton_θkp1(gk,gk_prime,θk,θk_1,l,h,Ɛ)
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
def calcul_erreurs(schema,ω_ini,θ_ini,T,l,m,Ɛ):
  erreurs_tout_n = []
  tout_n = []
  n = 2
  while n<8001:
    h = T/n
    θ_exact, ω_exact, Ec_exact, Ep_exact, Em_exact = pendule_exact.calcul_pendule_exact(ω_ini,θ_ini,T,l,m,n)
    θ, ω, Ec, Ep, Em = schema(ω_ini,θ_ini,l,m,n,h,Ɛ)
    erreurs = []
    for i in range(len(θ_exact)):
      erreurs.append(abs(θ_exact[i]-θ[i]))
    erreurs_tout_n.append(max(erreurs))
    tout_n.append(n)
    n+=500
  return tout_n, erreurs_tout_n

#Tracé des erreurs
def trace_erreurs(schema,ω_ini,θ_ini,T,l,m,Ɛ):
  tout_n, erreurs_tout_n = calcul_erreurs(schema,ω_ini,θ_ini,T,l,m,Ɛ)
  plt.figure(figsize=(3,3))
  plt.plot(tout_n, erreurs_tout_n, label="Erreurs(n)")
  plt.legend()

#Appel des fonctions
if __name__ == '__main__':
  ω_ini,θ_ini,T,l,m,n,Ɛ = 0,pi/16,5,1,1,2000,10**(-8)
  h=T/n
  θ, ω, Ec, Ep, Em = calcul_pendule_recd(ω_ini,θ_ini,l,m,n,h,Ɛ)
  pendule_exact.trace_theta(θ,T,n)
  pendule_exact.trace_energies(Ec,Ep,Em,T,n)
  pendule_exact.portrait_phase(θ, ω)
  trace_erreurs(calcul_pendule_recd,ω_ini,θ_ini,T,l,m,Ɛ)
  plt.show()