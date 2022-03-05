# Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...

# Hints
# Ideas about the problem

# Have the generator keep a list of the primes it's generated. A candidate number x is prime if (x % p) != 0 for all earlier primes p.

def genPrimes():
    natural = 1
    while True:
        natural +=1
        n = natural-1
        x = 0
        while n>1:
            if natural%n == 0:
                x =1
                break
            n-=1
        if x == 0:
            yield natural