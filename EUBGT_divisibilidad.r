division_entera <- function(a, b) {
  if (b <= 0){
    stop('Invalid b value')
  }
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
  
  return(list(cociente = q, residuo = r))
}

# Ejemplo 
result <- division_entera(-11, 3)
print(paste("Cociente:", result$cociente))
print(paste("Residuo:", result$residuo))

result <- division_entera(-11, -3) # No acepta negativos para B por la definición
print(paste("Cociente:", result$cociente))
print(paste("Residuo:", result$residuo))
