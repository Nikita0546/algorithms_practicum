import time

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def measure_time(n):
    start_time = time.time() 
    result = fib(n)           
    end_time = time.time()    
    execution_time = (end_time - start_time) * 1000 
    return result, execution_time

if __name__ == "__main__":
    test_values = [6, 10, 15, 20, 24]  
    
    for n in test_values:
        result, exec_time = measure_time(n)
        print(f"fib({n}) = {result}, Время выполнения: {exec_time:.3f} ms")
