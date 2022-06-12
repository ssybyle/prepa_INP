'''Les tours de Hanoï.'''
def hanoi(n,depart,milieu,arrivee):
  if n == 1:
    print(depart, '->', arrivee)
  else:
    hanoi(n-1,depart,arrivee,milieu)
    hanoi(1,depart,milieu,arrivee)
    hanoi(n-1,milieu,depart,arrivee)
    

hanoi(4,'A','B','C');