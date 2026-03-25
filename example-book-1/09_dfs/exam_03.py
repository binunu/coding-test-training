# 네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.

# 컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

def solution(n, computers):
    isnet=[False] * n
    cnt=0
    
    def dfs(num):
        for j in range(len(computers[num])):
            if computers[num][j] == 1 and not isnet[j]:
                isnet[j] = True
                dfs(j)

    for i in range(len(computers)):
        if not isnet[i]:
            cnt+=1
            isnet[i] = True
            dfs(i)
        
    return cnt

# 풀이과정
# 컴퓨터를 처음부터 돌면서 방문되지 않은 컴퓨터 발생 시 카운트를 증가시키고 그와 연결된걸 파악(dfs)
# 연결된 컴퓨터가 있으면 모두 방문처리.
# 만약 두 번째 컴퓨터 차례일 때 이미 방문처리 되어있으면 연결된 것이므로 패스
