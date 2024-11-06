def dfs(laberinto, posicion_actual, visitados=None): #dfs vuelve a buscar desde el anterior es recursivo
    if visitados is None:
        visitados = set()
    
    # Marca la posición actual como visitada
    visitados.add(posicion_actual)
    print(f"Visitando la posición: {posicion_actual}")

    # Si es una salida, termina
    if laberinto[posicion_actual] == 'Salida':
        print("¡Encontraste la salida!")
        return True

    # Explora los vecinos
    for vecino in laberinto[posicion_actual]:
        if vecino not in visitados:
            if dfs(laberinto, vecino, visitados):  # Si se encuentra la salida en la rama, detener la búsqueda
                return True
    
    return False

# Representación del laberinto
laberinto = {
    'Entrada': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E'],
    'C': ['Salida'],
    'D': [],
    'E': [],
    'Salida': []
}

# Comenzar a buscar desde la 'Entrada'
dfs(laberinto, 'Entrada')