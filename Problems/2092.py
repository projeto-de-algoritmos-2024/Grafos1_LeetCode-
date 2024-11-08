from collections import defaultdict

class Solution:
    def findAllPeople(self, n, meetings, firstPerson):
        # Inicializar as pessoas que sabem o segredo
        knows_secret = {0, firstPerson}
        
        # Agrupar reuniões por tempo e ordenar
        meetings.sort(key=lambda x: x[2])
        
        i = 0
        while i < len(meetings):
            time = meetings[i][2]
            group = defaultdict(list)
            j = i
            
            # Agrupar todas as reuniões no mesmo tempo
            while j < len(meetings) and meetings[j][2] == time:
                x, y, _ = meetings[j]
                group[x].append(y)
                group[y].append(x)
                j += 1
            
            # Usar Union Find para determinar os grupos que sabem o segredo
            parent = {p: p for p in group}
            
            def find(x):
                if parent[x] != x:
                    parent[x] = find(parent[x])
                return parent[x]
            
            def union(x, y):
                parent[find(x)] = find(y)
            
            # Conectar todos os participantes
            for p1 in group:
                for p2 in group[p1]:
                    union(p1, p2)
            
            # Propagar o segredo
            secret_group = set()
            for p in group:
                if p in knows_secret:
                    secret_group.add(find(p))
            
            for p in group:
                if find(p) in secret_group:
                    knows_secret.add(p)
            
            i = j
        
        return list(knows_secret)