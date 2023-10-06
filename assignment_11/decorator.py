import time

def performance_log(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        wrapper.time_taken = end_time - start_time
        return result
    return wrapper

@performance_log
def find_primes(min, max):
    primes = []
    for num in range(min, max + 1):
        if num > 1:
            is_prime = True
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    return primes

x = find_primes(2, 50000)
print(len(x))
print(find_primes.time_taken)