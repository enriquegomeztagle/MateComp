# Instalar y cargar la librería 'numbers'
# install.packages("matlab")
library(matlab)

# Definir la función de Mersenne
smersenne <- function(n) {
  return(2^n - 1)
}

# Inicializar una lista para almacenar los números primos de Mersenne
mersenne_primes <- c()

# Encontrar los primeros 20 números primos
initial_primes <- head(primes(200), 20)
cat("Primeros 20 números primos:", initial_primes, "\n")

# Encontrar los números primos de Mersenne utilizando la función smersenne y isprime
for (p in initial_primes) {
  m <- smersenne(p)
  if (isprime(m)) {
    mersenne_primes <- c(mersenne_primes, m)
    cat("Mersenne encontrado: ", m, "\n")
  }
}

