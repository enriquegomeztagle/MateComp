# install.packages("igraph")
library(igraph)

# Define el conjunto A
A <- c(1, 2, 3, 4, 5)

# Inicializa una matriz para la relación R con ceros
R_matrix <- matrix(0, nrow=length(A), ncol=length(A))

# Llena la matriz según la condición dada de la relación aRb si a > b y b es impar
for (i in 1:length(A)) {
  for (j in 1:length(A)) {
    if (A[i] >= A[j] && A[j] %% 2 == 1) {
      R_matrix[i, j] <- 1
    }
  }
}

# Imprime la matriz R
print("Matriz R:")
print(R_matrix)

# Verifica si la relación es reflexiva
is_reflexive <- all(diag(R_matrix) == 1)

# Verifica si la relación es irreflexiva
is_irreflexive <- all(diag(R_matrix) == 0)

# Imprime si la relación es reflexiva o irreflexiva
if(is_reflexive) {
  print("La relación es reflexiva.")
} else if (is_irreflexive) {
  print("La relación es irreflexiva.")
} else {
  print("La relación no es reflexiva ni irreflexiva.")
}

# Verifica si la relación es simétrica
is_symmetric <- all(R_matrix == t(R_matrix))

# Verifica si la relación es asimétrica
is_asymmetric <- all((R_matrix * t(R_matrix)) == 0)

# Imprime si la relación es simétrica o asimétrica
if(is_symmetric) {
  print("La relación es simétrica.")
} else if(is_asymmetric) {
  print("La relación es asimétrica.")
} else {
  print("La relación no es ni simétrica ni asimétrica.")
}

# Verifica si la relación es antisimétrica
is_antisymmetric <- all((R_matrix * t(R_matrix)) == diag(diag(R_matrix)))

# Imprime si la relación es antisimétrica
if(is_antisymmetric) {
  print("La relación es antisimétrica.")
} else {
  print("La relación no es antisimétrica.")
}

# Calcula la matriz resultante de la multiplicación de R por sí misma
R_squared <- R_matrix %*% R_matrix

# Verifica si la relación es transitiva
is_transitive <- all((R_squared <= 1) | (R_matrix == 1))

# Imprime si la relación es transitiva
if(is_transitive) {
  print("La relación es transitiva.")
} else {
  print("La relación no es transitiva.")
}

# Crea el grafo a partir de la matriz de adyacencia
g <- graph_from_adjacency_matrix(R_matrix, mode="directed", diag=TRUE)

# Grafica el grafo
plot(g, layout=layout_in_circle, vertex.size=30, vertex.label=names(A), 
     edge.arrow.size=0.5, main="Grafo dirigido de la Relación R")

# Si la relación cumple con las 3 propiedades, encuentra las clases de equivalencia y la partición
if (is_reflexive && is_symmetric && is_transitive) {
  # Encuentra las clases de equivalencia y la partición
  equivalence_classes <- list()
  partition <- list()
  
  for (element in A) {
    class_index <- find_equivalence_class(element, equivalence_classes)
    if (is.null(class_index)) {
      equivalence_classes[[length(equivalence_classes) + 1]] <- element
    } else {
      equivalence_classes[[class_index]] <- c(equivalence_classes[[class_index]], element)
    }
  }
  
  for (i in seq_along(equivalence_classes)) {
    partition[[i]] <- equivalence_classes[[i]]
  }
  
  # Imprime las clases de equivalencia y la partición
  cat("Clases de Equivalencia:\n")
  for (i in seq_along(equivalence_classes)) {
    cat("Clase", i, ":", equivalence_classes[[i]], "\n")
  }
  
  cat("\nPartición:\n")
  for (i in seq_along(partition)) {
    cat("Subset", i, ":", partition[[i]], "\n")
  }
} else {
  print("La relación no cumple con las tres propiedades: reflexividad, simetría y transitividad.")
}

# Función para encontrar la clase de equivalencia de un elemento
find_equivalence_class <- function(element, equivalence_classes) {
  for (i in seq_along(equivalence_classes)) {
    if (element %in% equivalence_classes[[i]]) {
      return(i)
    }
  }
  return(NULL)
}