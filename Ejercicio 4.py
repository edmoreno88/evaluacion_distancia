def suma_serie_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    

    a, b = 1, 1
    suma = a + b
    for _ in range(3, n + 1):
        a, b = b, a + b
        suma += b

    return suma
    
n = int(input("ingresa el valor de n: "))

resultado = suma_serie_fibonacci(n)
print(f"la suma de los primeros {n} terminos es: {resultado}")