from typing import List

class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        # Une dois conjuntos
        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX != rootY:
                # Une baseado no rank para otimização
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1

        result = []

        # Processa cada solicitação de amizade
        for u, v in requests:
            rootU, rootV = find(u), find(v)
            canBeFriends = True

            # Verifica se essa solicitação viola alguma restrição
            for x, y in restrictions:
                rootX, rootY = find(x), find(y)
                if (rootU == rootX and rootV == rootY) or (rootU == rootY and rootV == rootX):
                    canBeFriends = False
                    break

            # Se a solicitação for válida, une os conjuntos de u e v
            if canBeFriends:
                union(u, v)
                result.append(True)
            else:
                result.append(False)

        return result