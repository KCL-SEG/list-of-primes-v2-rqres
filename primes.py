"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def is_prime(n):
    for d in range(2, int( n/2 )):
        if n % d == 0:
            return False

    return True

def primes(number_of_primes):
    list = []
    if number_of_primes > 0:
        list.append(2)
        number_of_primes -= 1
    else:
        raise ValueError

    next = 3 
    while number_of_primes != 0:
        if is_prime(next):
            list.append(next)
            number_of_primes -= 1
        next += 2

    return list

print(primes(10))
