# Cargar las bibliotecas necesarias
library(matlab)
library(numbers)

# Función para calcular el número de Fermat
fermat <- function(n) {
  2^(2^n) + 1
}

# Función para calcular el número de Mersenne
mersenne <- function(p) {
  2^p - 1
}

# Función para obtener el siguiente número primo
next_prime <- function(n) {
  candidate <- n + 1
  while (!isprime(candidate)) {
    candidate <- candidate + 1
  }
  candidate
}

# Función para obtener los primeros úmeros primos de Mersenne
get_mersenne_primes <- function() {
  primes <- c()
  p <- 2
  while (length(primes) < 7) {
    m <- mersenne(p)
    if (isprime(m)) {
      primes <- c(primes, m)
    }
    p <- next_prime(p)
  }
  primes
}

# Función para obtener los primeros números primos de Fermat
get_fermat_primes <- function() {
  primes <- c()
  n <- 0
  while (length(primes) < 7 && n < 5) { # Continuamos hasta tener 7 primos de Fermat 
    # La restricción de n < 5 se debe a que solo hay 5 números primos de Fermat conocidos.
    f <- fermat(n)
    if (isprime(f)) {
      primes <- c(primes, f)
    }
    n <- n + 1
  }
  primes
}

# Obtener los primeros números primos de Mersenne y Fermat
mersenne_primes_list <- get_mersenne_primes()
fermat_primes_list <- get_fermat_primes()

# Mostrar los resultados
cat(paste("Los primeros", length(mersenne_primes_list), " números primos de Mersenne:\n"))
print(mersenne_primes_list)
cat(paste("Los primeros", length(fermat_primes_list), " números primos de Fermat:\n"))
print(fermat_primes_list)
