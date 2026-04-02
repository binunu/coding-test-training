# 순위 level 3
# n명의 권투선수가 권투 대회에 참여했고 각각 1번부터 n번까지 번호를 받았습니다. 권투 경기는 1대1 방식으로 진행이 되고, 만약 A 선수가 B 선수보다 실력이 좋다면 A 선수는 B 선수를 항상 이깁니다. 심판은 주어진 경기 결과를 가지고 선수들의 순위를 매기려 합니다. 하지만 몇몇 경기 결과를 분실하여 정확하게 순위를 매길 수 없습니다.

# 선수의 수 n, 경기 결과를 담은 2차원 배열 results가 매개변수로 주어질 때 정확하게 순위를 매길 수 있는 선수의 수를 return 하도록 solution 함수를 작성해주세요.

def solution(n, results):
    answer = 0
    matrix = [[0]*(n+1) for _ in range(n+1)]

    for w, r in results:
        matrix[w][r]=1 # 승리
        matrix[r][w]=-1 # 패배
        
    for k in range(1,n+1):
        for j in range(1,n+1):
            for i in range(1,n+1):
                if matrix[i][k] == 1 and matrix[k][j] ==1:
                    matrix[i][j] = 1
                    matrix[j][i] = -1
                
    # 나를 제외한 승패관계를 모두 알 수 있으면 순위를 알 수 있음
    # 굳이 나와 직접 겨룬 결과가 없어도 간접적으로 a>b, a>c면 a>c임을 이용
    # a부터 이긴 or 진 리스트를 돌며 a가 이긴 리스트의 요소들의 이긴 리스트를 계속 돌면서 기록
    for i in range(1,n+1):
        if matrix[i].count(1)+matrix[i].count(-1)  >= n-1: # 0번째, 나를제외한 개수 
            answer+=1
    return answer