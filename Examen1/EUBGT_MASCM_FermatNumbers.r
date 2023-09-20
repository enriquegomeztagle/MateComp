# Cargar las bibliotecas necesarias
# install.packages("dplyr")
# install.packages("numbers")
# install.packages("matlab")

library(matlab)
library(numbers)
library(dplyr)

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
    # La restricción de n < 5 se debe a que solo hay 5 números primos de Fermat conocidos
    # solo soporta 5 porque el sexto ya sería muy grande para la computadora.
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

# Similitudes:
# 1) Basados en formulas con potencias de 2.
# 2) Los primeros números son 3 en ambos.

# Diferencias:
# 1) Los de fermat crecen más rapido
# 2) La formula de fermat es más compleja

# Solo se conocen 5 números de fermat y por eso solo tenemos 5, ya que el siguiente es demasiado grande y no lo soporta el poder computacional
# al menos de los 2 lenguajes que probamos.

# La formula está basado en binario
# No tienen más relaciones


# Crear un dataframe para guardar las diferencias
df <- data.frame(
  Position = 1:max(length(mersenne_primes_list), length(fermat_primes_list)),
  Mersenne = NA,
  Fermat = NA,
  Difference = NA
)

# Rellenar las columnas de Mersenne y Fermat
df$Mersenne[1:length(mersenne_primes_list)] <- mersenne_primes_list
df$Fermat[1:length(fermat_primes_list)] <- fermat_primes_list

# Calcular la diferencia
df <- df %>%
  mutate(Difference = case_when(
    is.na(Mersenne) ~ "-",
    is.na(Fermat) ~ "-",
    TRUE ~ as.character(Fermat - Mersenne)
  ))

# Mostrar el dataframe
print(df)

# OUTPUT
# Position Mersenne Fermat Difference
# 1        1        3      3          0
# 2        2        7      5         -2
# 3        3       31     17        -14
# 4        4      127    257        130
# 5        5     8191  65537      57346
# 6        6   131071     NA          -
# 7        7   524287     NA          -
