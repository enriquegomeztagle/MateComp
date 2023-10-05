mcd <- function(a, b) {
  c <- abs(a)
  d <- abs(b)
  while (d != 0) {
    r <- c %% d
    c <- d
    d <- r
  }
  return(abs(c))
}

division_entera <- function(a, b) {
  if (a == 0) {
    q <- 0
    r <- 0
  } else {
    r <- abs(a)
    q <- 0
    while (r >= b) {
      r <- r - b
      q <- q + 1
    }
    if (a > 0) {
      q <- q
      r <- r
    } else if (r == 0) {
      q <- -q
      r <- r
    } else {
      q <- -q - 1
      r <- b - r
    }
  }
  return(list(q = q, r = r))
}

# Prueba
a <- 56
b <- 42
result <- division_entera(a, b)
cat(sprintf("Al dividir %d entre %d:\n", a, b))
cat(sprintf("Cociente (q) = %d\n", result$q))
cat(sprintf("Residuo (r) = %d\n", result$r))

# Prueba del MCD
cat(sprintf("El MCD de %d y %d es: %d\n", a, b, mcd(a, b)))

