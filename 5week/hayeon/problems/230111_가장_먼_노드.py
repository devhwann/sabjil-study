from collections import deque


def solution(n, edge):
    answer = 0
    adj = [[] for _ in range(n + 1)]
    distance = [-1] * (n + 1)

    for a, b in edge:
        adj[a].append(b)
        adj[b].append(a)

    queue = deque([1])
    distance[1] = 0

    while queue:
        now = queue.popleft()

        for i in adj[now]:
            if distance[i] == -1:
                queue.append(i)
                distance[i] = distance[now] + 1

    for d in distance:
        if d == max(distance):
            answer += 1

    return answer
