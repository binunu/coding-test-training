# 섬 연결하기 level 3
# n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때, 최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용을 return 하도록 solution을 완성하세요.

# 다리를 여러 번 건너더라도, 도달할 수만 있으면 통행 가능하다고 봅니다. 예를 들어 A 섬과 B 섬 사이에 다리가 있고, B 섬과 C 섬 사이에 다리가 있으면 A 섬과 C 섬은 서로 통행 가능합니다.
 

def solution(n, costs):
    link=0
    p = [i for i in range(n)]
    answer = 0
    def findp(x):
        if p[x] == x:
            return x
        p[x] = findp(p[x])
        return p[x]
    
    def union(a,b):
        if findp(a) != findp(b):
            p[findp(a)] = findp(b)
            return False
        return True    

    costs.sort(key=lambda x:x[2])
    for i,j,c in costs:
        if not union(i,j):
            answer+=c
            link+=1
            if link == n-1:
                return answer
            

# 모든 섬이 연결되어잇는지를 확인하면 됨 
# 일단 최소비용 기준으로 정렬하고,
# 하나씩 돌면서 연결이 되지 않은 섬이면 연결시킴
