import math

def fib(n):
    phi = (1 + math.sqrt(5)) / 2  
    psi = (1 - math.sqrt(5)) / 2 
    fib_n = (phi**n - psi**n) / math.sqrt(5)
    
    return round(fib_n)

n = 32 
result = fib(n)
print(f"fib({n}) = {result}")
