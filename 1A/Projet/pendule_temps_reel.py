from math import *
import matplotlib.pyplot as plt
import numpy as np
import pendule_exact

#Tracé en temps réel
def trace_temps_reel(θ,l):
  for k in θ:
    plt.clf()
    plt.xlim(-0.2, 0.4)
    plt.ylim(-1.2,-0.5)
    plt.plot(l*sin(k),-l*cos(k),'ro')
    plt.plot([0,l*sin(k)],[0,-l*cos(k)],'k')
    plt.pause(0.01)
  plt.show()

#Appel de la fonction
ω_ini,θ_ini,T,l,m,n = 0,pi/16,3,1,1,1000
θ, ω, Ec, Ep, Em = pendule_exact.calcul_pendule_exact(ω_ini,θ_ini,T,l,m,n)
trace_temps_reel(θ,l)