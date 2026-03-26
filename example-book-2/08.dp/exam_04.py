# 등굣길 level 3
# 계속되는 폭우로 일부 지역이 물에 잠겼습니다. 물에 잠기지 않은 지역을 통해 학교를 가려고 합니다. 집에서 학교까지 가는 길은 m x n 크기의 격자모양으로 나타낼 수 있습니다.

# 아래 그림은 m = 4, n = 3 인 경우입니다.

# image0.png

# 가장 왼쪽 위, 즉 집이 있는 곳의 좌표는 (1, 1)로 나타내고 가장 오른쪽 아래, 즉 학교가 있는 곳의 좌표는 (m, n)으로 나타냅니다.

# 격자의 크기 m, n과 물이 잠긴 지역의 좌표를 담은 2차원 배열 puddles이 매개변수로 주어집니다. 오른쪽과 아래쪽으로만 움직여 집에서 학교까지 갈 수 있는 최단경로의 개수를 1,000,000,007로 나눈 나머지를 return 하도록 solution 함수를 작성해주세요.

def solution(m, n, puddles):
    answer = 0
    # 매 칸에 그 칸까지 가는 경로를 저장
    # 왼쪽, 위쪽으로부터 올 수 있음
    # 좌표 순서가 반대인 것에 유의
    # 문제는 (1,1)부터시작하므로 puddles, res에 각각 -1, 순서 반대로 하여 삽입/리턴
    # 갈 수 있는 곳은 
    mp = [[0] *m for _ in range(n)]
#     for x,y in puddles:
#         mp[y-1][x-1] = -1
        
    for i in range(n):
        for j in range(m):
            if i==0 and j ==0:
                mp[i][j] = 1
                continue
            # 왼쪽으로 오는 경우 + 위에서 오는 경우
            # i==0이면 왼쪽에서만 올 수 있음
            # j==0이면 위쪽에서만 올 수 있음
            up = 0
            left = 0
            if i!=0 and [j+1,i] not in puddles:
                up = mp[i-1][j]
            if j!=0 and [j,i+1] not in puddles:
                left = mp[i][j-1]
            mp[i][j] = up+left
            
    return mp[n-1][m-1]%1000000007