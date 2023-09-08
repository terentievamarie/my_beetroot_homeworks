import asyncio
import time

async def calculate_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b

async def calculate_factorial(n):
    if n == 0:
        return 0
    else:
        return n * await calculate_factorial(n - 1)

async def calculate_squares(n):
    return n**2

async def calculate_cubic(n):
    return n**3

async def main():
    numbers = list(range(1, 11))
    tasks = []

    for n in numbers:
        tasks.append(calculate_fibonacci(n))
        tasks.append(calculate_factorial(n))
        tasks.append(calculate_squares(n))
        tasks.append(calculate_cubic(n))

    results = await asyncio.gather(*tasks)
    return results

if __name__ == "__main__":
    start_time = time.perf_counter()
    loop = asyncio.get_event_loop()
    results_asyncio = loop.run_until_complete(main())
    end_time = time.perf_counter()
    print("Asyncio results:", results_asyncio)
    print("Asyncio execution time:", end_time - start_time, "seconds")