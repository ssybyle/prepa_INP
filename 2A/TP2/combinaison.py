''' Calcul des combinaisons. '''
def combinaison(p, n):
  '''
  Il faut n>=p
  '''
  if p == 0 or p == n:
    return 1
  return combinaison(p, n-1) + combinaison(p-1,n-1)

def factorielle(n):
  if n == 0:
    return 1
  return n*factorielle(n-1)

def combinaison_factorielle(p,n):
  return factorielle(n)/(factorielle(n-p)*factorielle(p))

print(combinaison(2, 4))
