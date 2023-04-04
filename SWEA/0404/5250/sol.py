import sys
sys.stdin = open('input.txt')


def f(s):
    bit = [0] * (V + 1)  # 최소 거리 설정을 완료했음을 담아줄 배열
    bit[s] = 1  # 시작 정점은 바로 담아줌

    # 모든 정점을 순회하며
    # 시작 정점 s 에서 정점 v로 가는 거리를 배열 D에 넣어줌
    for v in range(V + 1):
        D[v] = adj[s][v]

    # 남은 정점의 비용 결정
    # 정점 s는 이미 거리가 정해졌으므로 나머지 노드 V-1개 만큼 순회하며 결정
    for _ in range(V):
        # D[w]가 최소인 w 결정

        # 최소값을 충분히 큰 값으로 초기화
        minn = inf
        # 선택 정점을 0으로 초기화
        w = 0

        # 비용을 결정할 정점 선택하기 위한 순회
        for i in range(V + 1):
            # 남은 정점 중에서 거리가 아직 정해지지 않았고
            # 최소값을 계속 갱신해줘서 남은 정점 중 거리가 최소인 정점 i 선택
            if bit[i] == 0 and minn > D[i]:
                # 정점을 i로 선택
                w = i
                # 최소값을 거리배열의 값으로 설정
                minn = D[i]

        # 거리가 최소인 정점 w는 최소 거리 설정을 완료했으므로
        # 바로 완료 배열에 표시해줌
        bit[w] = 1

        # 선택 정점 w와 인접한 정점에 대해서 기존 비용 vs w를 거쳐가는 비용 비교
        for v in range(V + 1):
            # w에 인접인 정점의 조건 : 자기 자신 제외, 인접하지 않은 것 제외
            if 0 < adj[w][v] < inf:
                # 기존 비용 vs w를 거쳐가는 비용 비교
                D[v] = min(D[v], D[w] + adj[w][v])


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())

    # 충분히 큰 가중치 값
    I = 100 * 1000

    adj = [[I]* (V+1) for _ in range(V+1)]

    for i in range(V+1):
        adj[i][i] = 0

    for _ in range(E):
        u, v, w = map(int, input().split())
        adj[u][v] = w

    D = [0] * (V+1)

    f(0)

    print(f'#{tc} {D[-1]}')