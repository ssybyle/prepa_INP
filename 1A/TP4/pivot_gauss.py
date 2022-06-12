'''
Implantation du pivot de Gauss.  Une matrice est une liste de colonnes, une
colonne étant une liste de nombres.
'''

def exemple_m1():
  return [[5,6,1,8],[1,-3,7,2],[9,4,2,0]]

def est_matrice_valide(m):
  if isinstance(m, list) == False:
    return False
  for i in range(len(m)):
    if isinstance(m[i], list) == False:
      return False
    for k in m[i]:
      if isinstance(k, int) == False:
        return False
    if len(m[i]) != len(m[0]):
      return False
  else:
    return len(m), len(m[0])

def matrice_nulle(n, p):
  matrice = []
  for i in range(n):
    bébé_matrice = []
    for k in range(p):
      bébé_matrice.append(0)
    matrice.append(bébé_matrice)
  return matrice

def afficher(m):
  pass

def dilater(m, i, alpha):
  for k in range(len(m[i])):
    m[i][k]=alpha*m[i][k]
  return None

def transvecter(m, i1, i2, alpha):
  dilater(m, i2, alpha)
  for k in range(len(m[i1])):
    m[i1][k]=m[i1][k] + m[i2][k]
  return None

def permuter(m, i1, i2):
  (m[i1],m[i2])=(m[i2],m[i1])
  return None

def matrice_augmentee(m, c):
  for k in range(len(c)):  
    m[k].append(c[k])
  return m

def colonne(m, c):
  matrice = []
  for i in range(len(m)):  
    matrice.append(m[i][c])
  return matrice

def sous_matrice(m, c_debut, c_fin):
  sous_matrice = []
  for i in range(len(m)):
    bébé_matrice = []
    for k in range(c_debut, c_fin):
      bébé_matrice.append(m[i][k])
    sous_matrice.append(bébé_matrice)
  return sous_matrice

def resoudre_gauss(A, b, optimise=False, trace=False):
  S = []
  for i in range(len(A)):
    c = colonne(A, i)
    S.append(c) #chaque ss liste = colonne de A
  longueur = len(S)
  for i in range(len(A)):
    for k in (len(S)-longueur, len(S)):
      transvecter(S, S[k], S[k+1], (-A[i][k+1])/A[i][k])
  longueur -= len(S) 
  
   #transvecte le 1er terme sur tout puis le 2 ème sur tout sauf la 1ère ect ect

      
  #ligne = 0
  #x = 0
  #for i in range(len(A)):
    #for k in range(len(A[i])):
      #ligne += A[i][k]
    #x = b/ligne
  #return x

if __name__ == '__main__':
  m1=exemple_m1()
  m1[1]=m1[0]
  m1[0][0]=0
  print(m1)
  print(est_matrice_valide([[3,4],[2],[7]]))
  