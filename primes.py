"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def primes(number_of_primes):
    limitn = number_of_primes+1
    primes = dict()
    # initialise primes dictionary to set everything to True
    for i in range(2, limitn):
        primes[i] = True

    for i in primes:
        # factors is a sequence of numbers from i to number of primes
        # collecting all the factors of a given number
        factors = range(i, limitn, i)
        for factor in factors[1:]:
            primes[factor] = False
    return [i for i in primes if primes[i] == True]
