import networkx as nx
import matplotlib.pyplot as plt

# Representación del laberinto
laberinto = {
    'Entrada': ['A', 'B'],
    'A': ['Entrada'],
    'B': ['C', 'D', 'Entrada'],
    'C': ['B', 'E'],
    'D': ['B', 'E'],
    'E': ['C', 'D', 'Salida'],
    'Salida': []
}

# Crear un grafo a partir del laberinto
G = nx.Graph()
for nodo, vecinos in laberinto.items():
    for vecino in vecinos:
        G.add_edge(nodo, vecino)

# Dibujar el grafo del laberinto
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold')
plt.title('Laberinto Representado con Nodos y Aristas')
plt.show()

# Bucle del laberinto
posicion_actual = "Entrada"
while posicion_actual != "Salida":
    print(f"Estás en {posicion_actual}. Puedes moverte a: {', '.join(laberinto[posicion_actual])}")
    proximo_paso = input("¿A dónde quieres ir? ").strip()
    
    # Verificamos si el próximo paso es válido
    if proximo_paso in laberinto[posicion_actual]:
        posicion_actual = proximo_paso
        print(f"Te has movido a {posicion_actual}")
    else:
        print("Movimiento no válido. Intenta de nuevo.")

# Mensaje final al llegar a la salida
print("¡Felicidades! Has encontrado la salida del laberinto.")
