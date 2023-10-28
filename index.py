# Não é permitido usar os canos

import heapq
fases = {
    'fase1': {'fase2': 2},
    'fase2': {'fase3': 3, 'fase6': 10},
    'fase3': {'fase2': 3, 'fase4': 2},
    'fase4': {'fase3': 2, 'fase5': 3},
    'fase5': {'fase4': 3, 'fase6': 4, 'fase7': 2},
    'fase6': {'fase5': 4, 'fase8': 3},
    'fase7': {'fase5': 2, 'fase8': 4},
    'fase8': {'fase6': 3, 'fase7': 4},
}

# Função para calcular o menor caminho usando o algoritmo de Dijkstra
def dijkstra(graph, start, end):
    heap = [(0, start)]
    visited = set()

    while heap:
        (cost, current) = heapq.heappop(heap)

        if current in visited:
            continue

        if current == end:
            return cost

        visited.add(current)

        for neighbor, weight in graph[current].items():
            if neighbor not in visited:
                heapq.heappush(heap, (cost + weight, neighbor))

    return float('inf')  # Se não há caminho, retornar infinito

# Altere os dados das fases que você quiser, aqui
inicio = 'fase1'
destino = 'fase7'

caminho_mais_curto = dijkstra(fases, inicio, destino)

print(f'O menor caminho de {inicio} para {destino} tem um custo total de {caminho_mais_curto}.')
