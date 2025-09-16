def prime(n):
    if n < 1:
        raise ValueError('there is no zeroth prime')
    
    primes = [2, 3, 5, 7, 11, 13, 17]

    if n <= len(primes):
        return primes[n-1]
    
    at = 17

    while n > len(primes):
        at += 2
        if all(at%prime for prime in primes):
            primes.append(at)

    return primes[-1]
