def BFS(G, v): # 그래프 G와 탐색 시작점 v
    visited = [0] * (n+1)   # visited 생성 : 인큐되었다는 뜻
    queue = []              # 큐 생성
    queue.append(v)         # 시작점 enqueue
    visited[v] = 1          # 시작점 방문기록 : 인큐되었음을 표시
    # -> 인큐와 방문기록은 짝을 이룬다.

    while queue:
        t = queue.pop(0)    # 큐의 첫 번째 원소를 소환한다.
        # 방문기록 필요 X -> 인큐 되었다는것 자체가 방문기록이 없다는 것

        ### 목적지에 도착했는지 확인하는 코드

           for i in G[t]:  # 인접 노드들 큐에 인큐
                if not visited[i]:  # 큐에 들어간적 없으면
                    queue.append(i) # 해당 노드를 인큐하고
                    visited[i] = visited[n] + 1 # 방문기록한다.
