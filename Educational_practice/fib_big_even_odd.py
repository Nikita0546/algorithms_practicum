def fib_eo(n):
    a, b = 0, 1
    
    for _ in range(n - 1):
        a, b = b, (a + b) % 10

    if b % 2 == 0:
        return "even"
    else:
        return "odd"

if __name__ == "__main__":
    n = 7373
    result = fib_eo(n)
    print(f"fib_eo({n}) = {result}")
