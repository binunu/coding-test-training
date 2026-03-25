# 징검다리 level 4
# 출발지점부터 distance만큼 떨어진 곳에 도착지점이 있습니다. 그리고 그사이에는 바위들이 놓여있습니다. 바위 중 몇 개를 제거하려고 합니다.
# 예를 들어, 도착지점이 25만큼 떨어져 있고, 바위가 [2, 14, 11, 21, 17] 지점에 놓여있을 때 바위 2개를 제거하면 출발지점, 도착지점, 바위 간의 거리가 아래와 같습니다.

# 제거한 바위의 위치	각 바위 사이의 거리	거리의 최솟값
# [21, 17]	[2, 9, 3, 11]	2
# [2, 21]	[11, 3, 3, 8]	3
# [2, 11]	[14, 3, 4, 4]	3
# [11, 21]	[2, 12, 3, 8]	2
# [2, 14]	[11, 6, 4, 4]	4
# 위에서 구한 거리의 최솟값 중에 가장 큰 값은 4입니다.

# 출발지점부터 도착지점까지의 거리 distance, 바위들이 있는 위치를 담은 배열 rocks, 제거할 바위의 수 n이 매개변수로 주어질 때, 바위를 n개 제거한 뒤 각 지점 사이의 거리의 최솟값 중에 가장 큰 값을 return 하도록 solution 함수를 작성해주세요.

# 그냥 단순히 각 바위사이의 거리를 돌면서 각 거리가 목표보다 작으면 치운다고만 생각했음
# 근데 사실은 해당 거리를 치우면 그 거리는 다음거리에 합쳐지기 때문에
# 다음 거리가 원래는 목표치보다 작았지만 커질수도 있는것임
# 그래서 누적합으로 계산해서 풀었어야함


def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    dis=[rocks[0]]
    for i in range(1,len(rocks)):
        dis.append(rocks[i]-rocks[i-1])
    dis.append(distance-rocks[-1])
    
    start=1
    end=distance
    
    while start <= end:
        mid = (start+end)//2
        now_d = 0
        cnt = 0
        for i in range(len(dis)):
            now_d += dis[i]
            if now_d < mid: # 바위치우고 거리 합치기
                cnt+=1  
            else: # 바위놓기
                now_d = 0

        # 도착지점에 대해서도 진행
        if cnt > n: # 예상보다더많이 설치함. -> 적게설치하는방향으로
            end = mid-1
        else: 
            start = mid+1
            answer = mid

        # 만약cnt==n이라면 최대값을 구해야하기 때문에 위쪽범위 탐색
    return answer