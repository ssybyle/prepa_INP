from math import *
import matplotlib.pyplot as plt
import numpy as np
import pendule_exact
import pendule_recd
import pendule_recg
import pendule_tra

#Tracé des thêta
def trace_theta(θ_exact,θ_recd,θ_recg,θ_tra,temps):
  plt.figure(figsize=(3,3))
  plt.plot(temps, θ_recd, label="Thêta_recd(t)")
  plt.plot(temps, θ_recg, label="Thêta_recg(t)")
  plt.plot(temps, θ_tra, label="Thêta_tra(t)")
  plt.plot(temps, θ_exact, label="Thêta_exact(t)")
  plt.legend()

#Tracé des énergies cinétiques
def trace_énergie_cinétique(Ec_exact,Ec_recd,Ec_recg,Ec_tra,temps):
  plt.figure(figsize=(3,3))
  plt.plot(temps, Ec_recd, label="Ec_recd(t)")
  plt.plot(temps, Ec_recg, label="Ec_recg(t)")
  plt.plot(temps, Ec_tra, label="Ec_tra(t)")
  plt.plot(temps, Ec_exact, label="Ec_exact(t)")
  plt.legend()

#Tracé des énergies potentielles
def trace_énergie_potentielle(Ep_exact,Ep_recd,Ep_recg,Ep_tra,temps):
  plt.figure(figsize=(3,3))
  plt.plot(temps, Ep_recd, label="Ep_recd(t)")
  plt.plot(temps, Ep_recg, label="Ep_recg(t)")
  plt.plot(temps, Ep_tra, label="Ep_tra(t)")
  plt.plot(temps, Ep_exact, label="Ep_exact(t)")
  plt.legend()

#Tracé des énergies mécaniques
def trace_énergie_mécanique(Em_exact,Em_recd,Em_recg,Em_tra,temps):
  plt.figure(figsize=(3,3))
  plt.plot(temps, Em_recd, label="Em_recd(t)")
  plt.plot(temps, Em_recg, label="Em_recg(t)")
  plt.plot(temps, Em_tra, label="Em_tra(t)")
  plt.plot(temps, Em_exact, label="Em_exact(t)")
  plt.legend()

#Tracé des erreurs
def trace_erreurs(ω_ini,θ_ini,T,l,m,n,h,Ɛ):
  tout_n, erreurs_recd = pendule_recd.calcul_erreurs(pendule_recd.calcul_pendule_recd,ω_ini,θ_ini,T,l,m,Ɛ)
  tout_n, erreurs_recg = pendule_recg.calcul_erreurs(ω_ini,θ_ini,T,l,m)
  tout_n, erreurs_tra = pendule_recd.calcul_erreurs(pendule_tra.calcul_pendule_tra,ω_ini,θ_ini,T,l,m,Ɛ)
  plt.figure(figsize=(3,3))
  plt.plot(tout_n, erreurs_recd, label="Erreurs_recd(n)")
  plt.plot(tout_n, erreurs_recg, label="Erreurs_recg(n)")
  plt.plot(tout_n, erreurs_tra, label="Erreurs_tra(n)")
  plt.legend()

#Affichage de toutes les courbes
def courbes(ω_ini,θ_ini,T,l,m,n,Ɛ):
  h=T/n
  temps = np.linspace(0,T,n)
  θ_exact, ω_exact, Ec_exact, Ep_exact, Em_exact = pendule_exact.calcul_pendule_exact(ω_ini,θ_ini,T,l,m,n)
  θ_recd, ω_recd, Ec_recd, Ep_recd, Em_recd = pendule_recd.calcul_pendule_recd(ω_ini,θ_ini,l,m,n,h,Ɛ)
  θ_recg, ω_recg, Ec_recg, Ep_recg, Em_recg = pendule_recg.calcul_pendule_recg(ω_ini,θ_ini,T,l,m,n)
  θ_tra, ω_tra, Ec_tra, Ep_tra, Em_tra = pendule_tra.calcul_pendule_tra(ω_ini,θ_ini,l,m,n,h,Ɛ)
  trace_theta(θ_exact,θ_recd,θ_recg,θ_tra,temps)
  trace_énergie_cinétique(Ec_exact,Ec_recd,Ec_recg,Ec_tra,temps)
  trace_énergie_potentielle(Ep_exact,Ep_recd,Ep_recg,Ep_tra,temps)
  trace_énergie_mécanique(Em_exact,Em_recd,Em_recg,Em_tra,temps)
  trace_erreurs(ω_ini,θ_ini,T,l,m,n,h,Ɛ)
  plt.show()

#Appel de la fonction
courbes(0,pi/16,10,1,1,2000,10**(-8))
