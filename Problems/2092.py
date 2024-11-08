from collections import defaultdict, deque

class Solution:
    def findAllPeople(self, n, meetings, firstPerson):
        knows_secret = {0, firstPerson}
        
        # Agrupa reuniões por tempo
        meetings_by_time = defaultdict(list)
        for x, y, time in meetings:
            meetings_by_time[time].append((x, y))
        
        # Ordena as chaves de tempo
        for time in sorted(meetings_by_time.keys()):
            connections = defaultdict(list)
            
            # Grafo de conexões para o tempo atual
            for x, y in meetings_by_time[time]:
                connections[x].append(y)
                connections[y].append(x)
            
            # Participantes no tempo atual que sabem o segredo
            queue = deque([p for p in connections if p in knows_secret])
            seen = set(queue)
            
            # BFS para propagar o segredo para todos conectados
            while queue:
                person = queue.popleft()
                for neighbor in connections[person]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append(neighbor)
            
            # Atualiza as pessoas que sabem o segredo
            knows_secret.update(seen)
        
        return list(knows_secret)