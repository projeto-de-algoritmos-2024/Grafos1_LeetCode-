import collections

class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        # Cria o grafo como um dicionário de dicionários, onde a chave é o nó e o valor é a menor distância entre os nós
        grafo = collections.defaultdict(lambda: collections.defaultdict(lambda: float('inf')))
        
        # Preenche o grafo com as arestas e pesos mínimos entre os nós
        for u, v, w in edges:
            grafo[u][v] = min(grafo[u][v], w)
            grafo[v][u] = min(grafo[v][u], w)
        
        n = len(passingFees)
        
        # Inicializa a tabela de estados para armazenar o custo mínimo em cada nó com o tempo restante
        estados = [[-1] * (maxTime + 1) for _ in range(n)]
        
        # Função auxiliar recursiva que calcula o custo mínimo de um nó ao destino
        def auxiliar(u, tempo):
            # Verifica se chegou ao destino (nó final)
            if u == n - 1:
                return passingFees[u]
            
            # Retorna o valor armazenado na tabela de estados se já foi calculado
            if estados[u][tempo] != -1:
                return estados[u][tempo]
            
            custo_minimo = float("inf")
            
            # Explora os nós vizinhos
            for v in grafo[u].keys():
                # Verifica se há tempo suficiente para ir ao nó vizinho
                if tempo - grafo[u][v] >= 0:
                    val = auxiliar(v, tempo - grafo[u][v])
                    custo_minimo = min(custo_minimo, val)
            
            # Armazena o custo mínimo mais a taxa de passagem do nó atual
            estados[u][tempo] = custo_minimo + passingFees[u]
            return estados[u][tempo]
        
        # Calcula o custo mínimo para ir do nó inicial ao final com o tempo máximo
        resultado = auxiliar(0, maxTime)
        
        # Retorna -1 se o custo mínimo é maior que um valor muito alto, caso contrário retorna o resultado
        if resultado > 10000000:
            return -1
        return resultado
