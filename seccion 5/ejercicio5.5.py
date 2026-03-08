def factorial(n):
    if n < 0:
        raise ValueError("El número debe ser un entero positivo.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
try:
    print(factorial(5))  
    print(factorial(0))  
    print(factorial(-3))
    
except ValueError as e:
    print(e)