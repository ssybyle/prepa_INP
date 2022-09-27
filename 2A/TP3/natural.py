class SignError(Exception):
  pass

def natural(p: str):
  nombre = int(p)
  if nombre<0:
    raise SignError('must not be negative')
  return nombre

'''
def input_natural(p: str):
  try:
    nombre = int(p)
  except ValueError:
    print("Un entier est attendu")
  except SignError:
    print("Un entier positif est attendu")
  return nombre
'''

def input_natural(consigne):
  while True:
    try:
      return natural(input(consigne))
    except ValueError:
      print("Un entier est attendu.")
    except SignError:
      print("Un entier positif est attendu.")