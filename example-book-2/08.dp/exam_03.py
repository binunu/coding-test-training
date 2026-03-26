# 정수삼각형 level 3
# 위와 같은 삼각형의 꼭대기에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 합니다. 아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다. 예를 들어 3에서는 그 아래칸의 8 또는 1로만 이동이 가능합니다.

# 삼각형의 정보가 담긴 배열 triangle이 매개변수로 주어질 때, 거쳐간 숫자의 최댓값을 return 하도록 solution 함수를 완성하세요.

def solution(triangle):
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            # 위에 숫자 + 오른쪽 위 숫자 
            up = 0
            ul = 0
            if j != 0:
                up=triangle[i-1][j-1]
            if j != len(triangle[i])-1:
                ul=triangle[i-1][j]
            triangle[i][j]+=max(up,ul)
    return max(triangle[-1])

# 2
# 3 3 
# 4 4 4 
# 위 + 왼쪽위로부터 받을 수 잇음
# 만약 j가 0 이라면 왼쪽위로 못받고 위로는 받음
# 만약 j가 len(i)-1번째라면 왼쪽 위로부터만 받을 수 있음 
# 바로위로는 못받음! 