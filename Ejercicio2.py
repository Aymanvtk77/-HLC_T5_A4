def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
n = 6
resultado = fibonacci(n)
print(f"El {n}-ésimo término de la sucesión de Fibonacci es: {resultado}")
