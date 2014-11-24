import factorization

def main():
    primes = factorization.primes(10)
    
    for p in factorization.primes(20, 10, primes):
        print(str(p), end=' ')
    print()

if __name__ == '__main__':
    main()