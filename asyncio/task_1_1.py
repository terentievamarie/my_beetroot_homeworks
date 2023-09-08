import multiprocessing
import time

def calculate_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b


def calculate_factorial(n):
    if n == 0:
        return 0
    else:
        return n * calculate_factorial(n - 1)

def calculate_squares(n):
    return n**2

def calculate_cubic(n):
    return n**3

def main():
    numbers = list(range(1, 11))
    pool = multiprocessing.Pool(processes=4)
    results = []

    for n in numbers:
        results.extend(pool.map(calculate_fibonacci, [n]))
        results.extend(pool.map(calculate_factorial, [n]))
        results.extend(pool.map(calculate_squares, [n]))
        results.extend(pool.map(calculate_cubic, [n]))

    pool.close()
    pool.join()
    return results

if __name__ == "__main__":
    start_time = time.time()
    results_multiprocessing = main()
    end_time = time.time()
    print("Multiprocessing results:", results_multiprocessing)
    print("Multiprocessing execution time:", end_time - start_time, "seconds")