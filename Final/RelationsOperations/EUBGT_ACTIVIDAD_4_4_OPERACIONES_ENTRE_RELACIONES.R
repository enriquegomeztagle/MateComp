install.packages("igraph")

library(igraph)

A <- c(1, 2, 3, 4, 5)
B <- A
B <- C

# Definimos las relaciones R y S
R <- read.table(textConnection("
1 1
1 4
1 5
2 1
2 2
2 5
3 2
3 4
4 1
4 3
4 4
4 5
5 1
5 4
5 5
"), col.names = c("from", "to"))

S <- read.table(textConnection("
2 1
2 3
2 4
3 1
3 3
3 4
3 5
4 3
4 4
5 1
5 2
5 3
5 5
"), col.names = c("from", "to"))

print("Relación R:")
print(R)
print("Relación S:")
print(S)

# Calculamos la inversa de S (S^-1)
S_inverse <- S
S_inverse$from <- S$to
S_inverse$to <- S$from

print("Inversa de S (S^-1):")
print(S_inverse)

# Calculamos la composición de R y S (R o S)
R_compose_S <- merge(S, R, by.x = "to", by.y = "from")
# Actualizamos los nombres de las columnas para reflejar los nombres correctos después de la fusión
names(R_compose_S) <- c("key", "from", "to")

print("Composición de R y S (R o S):")
print(R_compose_S)

# Calculamos la intersección de S^-1 y R o S (S^-1 ∩ R o S)
S_inverse_inter_R_compose_S <- merge(S_inverse, R_compose_S, by = c("from", "to"))

print("Intersección de S^-1 y R o S (S^-1 ∩ R o S):")
print(S_inverse_inter_R_compose_S)

# Creamos una matriz booleana de 5x5 para representar la intersección
matrix_size <- 5
M <- matrix(0, nrow = matrix_size, ncol = matrix_size)
for (row in 1:nrow(S_inverse_inter_R_compose_S)) {
  M[S_inverse_inter_R_compose_S[row, "from"], S_inverse_inter_R_compose_S[row, "to"]] <- 1
}

print("Matriz booleana de la intersección (S^-1 ∩ R o S):")
print(M)

# Creamos el grafo dirigido de la matriz
g <- graph_from_adjacency_matrix(M, mode="directed", diag=TRUE)

# Mostrar el grafo
plot(g, layout=layout_in_circle, vertex.size=30, vertex.label=c(1:length(A)), 
     edge.arrow.size=0.5, main="Grafo dirigido de la relación R")
