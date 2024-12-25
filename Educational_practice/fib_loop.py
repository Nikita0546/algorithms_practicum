import time

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def measure_execution_time(n):
    start_time = time.time()  
    result = fib(n)
    end_time = time.time()  
    execution_time_ms = (end_time - start_time) * 1000  
    return result, execution_time_ms

test_values = [3, 7, 10, 20, 32]
results = []

for n in test_values:
    fib_value, exec_time = measure_execution_time(n)
    results.append((n, fib_value, exec_time))

for n, fib_value, exec_time in results:
    print(f"fib({n}) = {fib_value}, Время выполнения: {exec_time:.3f} мс")

print("\nПредположение о сложности алгоритма: O(n)")
