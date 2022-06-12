def fact(n):
    ''' Factorielle d'un entier n positif...'''
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)

if __name__ == "__main__":
    print('1000! =', fact(1000))
