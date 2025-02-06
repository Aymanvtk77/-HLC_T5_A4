def positivo(n):
    if n == 0:
        return 0
    else:
        return n%10 + positivo(n/10)