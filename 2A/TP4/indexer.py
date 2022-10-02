'''Définir un indexeur.'''

import sys
numero = 1
mots_fois = {}
for i in sys.argv[2:]:
  mots_fois[i] = set()
for ligne in open(sys.argv[1]):
  for i in sys.argv[2:]:
    if i in ligne.split():
      mots_fois[i].add(numero)
  numero +=1
#for i in sys.argv[2:]:
  #mots_fois[i] = str(mots_fois[i])[1:-1]
print(str(mots_fois)[1:-1])
