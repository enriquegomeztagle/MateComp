library(matlab)

mersenne <- function(n) {
  return(2^n - 1)
}

prime_numbers <- c(2, 3, 5, 7, 11, 13 ,17)
mersenne_primes <- c()
perfect_numbers <- c()

for (p in prime_numbers) {
  m <- mersenne(p)
  if (isprime(m)) {
    mersenne_primes <- c(mersenne_primes, m)
  }
  else {
    mersenne_primes <- c(mersenne_primes, 0)
  }
}

for (i in seq_along(mersenne_primes)) {
  m <- mersenne_primes[i]
  p <- prime_numbers[i]
  
  r <- (2^(p - 1) * m)
  perfect_numbers <- c(perfect_numbers, r)
}

result_df <- data.frame(PrimeNumber = prime_numbers, MersenneNumber = mersenne_primes, PerfectNumber = perfect_numbers)

print(result_df)

