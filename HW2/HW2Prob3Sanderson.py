def sieve(k):
    from math import isqrt
    primes = [True]*k
    primes[0] = False
    primes[1] = False
    is_primes = []

    for integer in range(2,isqrt(k)):
        if primes[integer]:
            for x in range(integer**2,k,integer):
                primes[x] = False
    for integer in range(k):
        if primes[integer]:
            is_primes.append(integer)
    return is_primes

print(sieve(15000))