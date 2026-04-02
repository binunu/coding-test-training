# 가장 먼 노드 level 3

# n개의 노드가 있는 그래프가 있습니다. 각 노드는 1부터 n까지 번호가 적혀있습니다. 1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 합니다. 가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미합니다.

# 노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때, 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성해주세요.

from collections import deque
def solution(n, edge):
    answer = 0
    d=[0]*(n+1) #1번으로부터의 최단경로를 각각 저장
    v=[False] *(n+1)
    v[1]=True
    gh=[[] for _ in range(n+1)] # 각 노드 정리 -> gh[n] : n출발로 도착할 수 있는 간선 배열 저장
    dq=deque()
    # 노드 정리
    for s,e in edge:
        gh[s].append(e)
        gh[e].append(s)
    print(gh)
    
    # 1부터 최단거리 계산
    for nxt in gh[1]:
        dq.append(nxt)
    
    print(dq)
    while dq:
        x = dq.popleft()
        d[x]+=1
        v[x] = True
        for n in gh[x]:
            if not v[n]:
                dq.append(n)
    print(d)
    # 결과값 도출    
    return d.count(max(d))