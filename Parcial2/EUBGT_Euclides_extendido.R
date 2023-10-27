euclides_extendido <- function(a, b) {
  # Inicialización de las variables con valores absolutos de a y b
  c <- abs(a)
  d <- abs(b)
  
  # Inicialización de los coeficientes (c1, d1) y (c2, d2)
  c1 <- 1
  d1 <- 0
  c2 <- 0
  d2 <- 1
  
  # Bucle que se ejecuta mientras d no sea cero
  while(d != 0) {
    # Calcular cociente y residuo de la división de c entre d
    q <- c %/% d        
    r <- c - q * d      
    
    # Calcular los nuevos coeficientes (r1, r2)
    r1 <- c1 - q * d1
    r2 <- c2 - q * d2
    
    # Actualizar valores de c, d, c1, d1, c2 y d2
    c <- d
    c1 <- d1
    c2 <- d2
    d <- r
    d1 <- r1
    d2 <- r2
  }
  
  # Función para obtener el signo de un número
  sgn <- function(x) {
    if(x > 0) return(1)
    if(x < 0) return(-1)
    return(0)
  }
  
  # Calcular los coeficientes s y t utilizando c1, c2 y el signo de a, b y c
  s <- c1 / (sgn(a) * sgn(c))
  t <- c2 / (sgn(b) * sgn(c))
  
  # Devolver el MCD y los coeficientes s y t
  return(list(mcd = abs(c), s = s, t = t))
}

# Solicitar al usuario que introduzca los valores de a y b
a <- as.integer(readline(prompt = "a: "))
b <- as.integer(readline(prompt = "b: "))

# Ejecutar la función con los valores introducidos
resultado <- euclides_extendido(a, b)
print(resultado)

# Comprobar la validez de s y t mostrando la ecuación paso a paso
comprobacion <- a * resultado$s + b * resultado$t
print(paste("Comprobación: a * s + b * t =", comprobacion))
print(paste(a, "*", resultado$s, "+", b, "*", resultado$t, "=", comprobacion))
print(paste(a * resultado$s, "+", b * resultado$t, "=", comprobacion))
print(paste(a * resultado$s + b * resultado$t, "=", comprobacion))

# Verificar si la ecuación es correcta comparándola con el MCD
if (comprobacion == resultado$mcd) {
  print("COMPROBACIÓN EXITOSA")
} else {
  print("ERROR EN LA COMPROBACIÓN")
}
