import math

_INIT_START = 3
_START = _INIT_START
_PRIMES = []

def primes(n):
    """ Returns  a list of primes <= n """
    global _START, _PRIMES
    
    if n > _INIT_START and _START >= n:
        primes = []
        
        for p in _PRIMES:
            if p <= n:
                primes.append(p)
            else:
                break
                
        return primes
    else:
        _PRIMES = _primes(n + 1, _START, _PRIMES)
        _START = n
    
        return _PRIMES
    
def _primes(n, start, primes):
    if len(primes) > 0:
        sieve = [False] * start
    
        while len(sieve) < n:
            sieve.append(True)
        
        # take care of 1
        sieve[0] = True
        
        for p in primes:
            if p < n:
                sieve[p] = True
    else:
        sieve = [True] * n
        
    limit = int(math.sqrt(n)) + 1
    
    for i in range(_INIT_START, limit, 2):        
        if sieve[i]:
            sieve[i * i :: 2 * i] = [False] * int((n - i * i - 1) / (2 * i) + 1)
    
    return [2] + [i for i in range(_INIT_START, n, 2) if sieve[i]]

def is_prime(n):
    """ Returns true if n is prime; otherwise false """
    for p in primes(n):
        if n == p:
            return True
    
    return False
    
def factor(n):
    """ Returns list of prime factors of a integer """
    factors = []
    
    if not isinstance(n, int):
        return factors
                 
    n = abs(n)
    
    if n == 0 or n == 1:
        factors.append(n)
    else:
        p_n = primes(math.ceil(math.sqrt(n)))
        
        for p in p_n:
            while True:
                if n % p == 0:
                    factors.append(p)
                    
                    n = n // p
                else:
                    break
            
            if p > n:
                break
                
        if len(factors) == 0:
            factors.append(n)
    
    return factors
