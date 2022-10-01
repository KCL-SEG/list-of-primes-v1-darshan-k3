"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

# generating n number of primes


def primes(number_of_primes):
    count = 0
    i = 0
    primes = []
    while n < number_of_primes:
        i += 1
        count = 1
        for j in range(2, i):
            if i % j == 0:
                count = 0
                break
        if count == 1:
            primes.append(i)
            n += 1
    return primes
