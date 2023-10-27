mcd <- function(a, b) {
  c <- abs(a)
  d <- abs(b)
  cat(sprintf("Valores iniciales: c = %d, d = %d\n", c, d))
  
  while (d != 0) {
    r <- c %% d
    cat(sprintf("Residuo r = %d %% %d = %d\n", c, d, r))
    
    c <- d
    d <- r
    cat(sprintf("Nuevo valor de c = %d, Nuevo valor de d = %d\n", c, d))
  }
  
  cat(sprintf("El MCD es: %d\n", abs(c)))
  return(abs(c))
}

a = 56
b = 42

cat(sprintf("El MCD de %d y %d es: %d\n", a, b, mcd(a, b)))
