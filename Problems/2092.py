class Solution:
    def findAllPeople(self, n, meetings, firstPerson):
        knows_secret = set([0, firstPerson])
        
        meetings.sort(key=lambda x: x[2])
        
        for x, y, time in meetings:
            if x in knows_secret or y in knows_secret:
                knows_secret.add(x)
                knows_secret.add(y)
                
                queue = deque([x, y])
                visited = set([x, y])
                
                while queue:
                    person = queue.popleft()
                    for a, b, t in meetings:
                        if t != time:
                            continue
                        if a == person and b not in visited:
                            visited.add(b)
                            knows_secret.add(b)
                            queue.append(b)
                        elif b == person and a not in visited:
                            visited.add(a)
                            knows_secret.add(a)
                            queue.append(a)
        
        return list(knows_secret)