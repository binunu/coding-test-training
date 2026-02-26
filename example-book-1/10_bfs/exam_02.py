# ROR 게임은 두 팀으로 나누어서 진행하며, 상대 팀 진영을 먼저 파괴하면 이기는 게임입니다. 따라서, 각 팀은 상대 팀 진영에 최대한 빨리 도착하는 것이 유리합니다.
# 게임 맵의 상태 maps가 매개변수로 주어질 때, 캐릭터가 상대 팀 진영에 도착하기 위해서 지나가야 하는 칸의 개수의 최솟값을 return 하도록 solution 함수를 완성해주세요. 단, 상대 팀 진영에 도착할 수 없을 때는 -1을 return 해주세요.

from collections import deque
def solution(maps):
 
    n = len(maps)
    m = len(maps[0])
    v = [[1001] * m for _ in range(n)]
    v[0][0] = 1
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q = deque([(0,0)])
    while q:
        x,y = q.pop()
        for ix,iy in zip(dx,dy):
            nx = x+ix
            ny = y+iy
            if 0<= nx <n and 0<= ny< m and maps[nx][ny] == 1:
                if v[x][y]+1 < v[nx][ny]:
                    v[nx][ny] = v[x][y]+1
                    q.append((nx,ny))
            
        
    return v[n-1][m-1] if v[n-1][m-1] < 1001 else -1

# 개선 1)
# 위 코드로 정확성 테스트는 통과했으나 효율성 테스트는 다 틀림
# 가장 치명적인 이유는 pop()을 사용하고 있어서 bfs가 아니라 dfs방식으로 동작했다는 점
# 가장 마지막에 들어온걸로 계속 꺼내기 때문에 해당 노드의 가장 끝까지 갔다가 돌아오는 방식임
# 그래서 pop을 popleft로 바꾸니 효율성 테스트는 통과했다.

# 두 번째로 효율성을 증가시킬 수 있는 방법은 바로 한 번 방문한 곳은 방문처리를 하는 것이다
# 한 지점이 여러 경로로 도착할 수 있다면 그 중 가장 먼저 방문한 경로가 최단거리임을 논리적으로 알 수 있다.
# 그래서 방문처리를 하면 뒤늦게 도착한 경로는 계산하지 않아도 됨
# 기존에 최단거리로 사용했던 v를 활용해서 방문처리까지 하도록 수정해 보았다.

from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    v = [[-1] * m for _ in range(n)]
    v[0][0] = 1
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q = deque([(0,0)])
    while q:
        x,y = q.popleft()
        for ix,iy in zip(dx,dy):
            nx = x+ix
            ny = y+iy
            if 0<= nx <n and 0<= ny< m and maps[nx][ny] == 1:
                if v[nx][ny] == -1:
                    v[nx][ny] = v[x][y]+1
                    q.append((nx,ny))
            
        
    return v[n-1][m-1]

# 개선2)
# 마찬가지의 논리로, (x, y)가 가장 먼저 maps[n-1][m-1]에 도착할 때 루프를 종료한다면
# 이후의 불필요한 계산을 줄일 수 있다.(모든 q를 다 안돌아도 됨)
from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q = deque([(0,0)])
    while q:
        x,y = q.popleft()
        if x == n-1 and y == m-1: return maps[n-1][m-1]
        for ix,iy in zip(dx,dy):
            nx = x+ix
            ny = y+iy
            if 0<= nx <n and 0<= ny< m and maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y]+1
                    q.append((nx,ny))
            
        
    return maps[n-1][m-1] if maps[n-1][m-1] != 1 else -1

# 개선3)
# 여기서, 사실은 v를 사용하지 않고 기존 maps를 갱신하면 더 메모리를 아낄 수 있다.

from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q = deque([(0,0)])
    while q:
        x,y = q.popleft()
        if x == n-1 and y == m-1: return maps[n-1][m-1]
        for ix,iy in zip(dx,dy):
            nx = x+ix
            ny = y+iy
            if 0<= nx <n and 0<= ny< m and maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y]+1
                    q.append((nx,ny))
            
        
    return maps[n-1][m-1] if maps[n-1][m-1] != 1 else -1