def contar(n):
    if n < 10:
        return 1
    return 1 + contar(n/10)

contar(123456)