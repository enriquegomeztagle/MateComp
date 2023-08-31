import sympy as sp

# Define Mersenne function
def mersenne(n):
    return 2 ** n - 1

# Initialize list to store Mersenne primes
mersenne_primes = []

# Find first 20 prime numbers
initial_primes = [p for p in sp.primerange(0, 200)][:20]
print(f"First 20 prime numbers: {initial_primes}")

# Use sympy's isprime to find Mersenne primes from the first 20 prime numbers
for p in initial_primes:
    m = mersenne(p)
    if sp.isprime(m):
        mersenne_primes.append(m)
        print(f"Found {len(mersenne_primes)} Mersenne primes so far: Latest is {m}")

# Initialize generator to produce more primes
prime_gen = sp.primerange(max(initial_primes) + 1, 10**6)

# Continue finding Mersenne primes until we get 20
while len(mersenne_primes) < 20:
    p = next(prime_gen)
    m = mersenne(p)
    if sp.isprime(m):
        mersenne_primes.append(m)
        print(f"Found {len(mersenne_primes)} Mersenne primes so far: Latest is {m}")

print(f"First 20 Mersenne primes: {mersenne_primes}")
