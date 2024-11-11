from collections import deque, defaultdict

class Solution:
    def friendRequests(self, n, restrictions, requests):
        # representa amizades
        friends = defaultdict(list)
        result = []
        
        # verifica se duas pessoas estão indiretamente conectadas
        def violates_restriction(u, v):
            queue = deque([u])
            visited = set([u])
            
            # Faz BFS para ver conexões
            while queue:
                current = queue.popleft()
                
                if current == v:
                    return True
                
                for friend in friends[current]:
                    if friend not in visited:
                        visited.add(friend)
                        queue.append(friend)
            return False

        for u, v in requests:
            can_be_friends = True
            for x, y in restrictions:
                # restrições
                if (violates_restriction(u, x) and violates_restriction(v, y)) or \
                   (violates_restriction(u, y) and violates_restriction(v, x)):
                    can_be_friends = False
                    break

            # Adiciona a amizade se não há violação de restrição
            if can_be_friends:
                friends[u].append(v)
                friends[v].append(u)
                result.append(True)
            else:
                result.append(False)
                
        return result
