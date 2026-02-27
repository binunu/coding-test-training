# 실패율
# 슈퍼 게임 개발자 오렐리는 큰 고민에 빠졌다. 그녀가 만든 프랜즈 오천성이 대성공을 거뒀지만, 요즘 신규 사용자의 수가 급감한 것이다. 원인은 신규 사용자와 기존 사용자 사이에 스테이지 차이가 너무 큰 것이 문제였다.

# 이 문제를 어떻게 할까 고민 한 그녀는 동적으로 게임 시간을 늘려서 난이도를 조절하기로 했다. 역시 슈퍼 개발자라 대부분의 로직은 쉽게 구현했지만, 실패율을 구하는 부분에서 위기에 빠지고 말았다. 오렐리를 위해 실패율을 구하는 코드를 완성하라.

# 실패율은 다음과 같이 정의한다.
# 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
# 전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때, 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하라.


def solution(N, stages):
    answer = []
    # 목표 : 실패율이 높은 스테이지부터 내림차순 return
    # 각 스테이지의 실패율을 구해야함
    s = [0] * (N+1) # s:  각 스테이지에 도달한 플레이어 수.  
    # 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수는 stages.count(x) 로 구하면 됨
    fail = {}
    
    for x in stages: # 각 스테이지에 도달한 플레이어 수. 
        if x == N+1:
            for i in range(x-1):
                s[i+1] +=1
        else:
            for i in range(x):
                s[i+1] +=1

    for x in range(1,N+1):
        if stages.count(x)==0:
            fail[x] = 0 
        else:
            fail[x] = stages.count(x)/s[x]
    arr = dict(sorted(fail.items(), key=lambda x: x[1], reverse=True))
    return list(arr.keys())
# 처음에 그냥 직관적으로 풀었던 풀이. 하지만 1문제에서 시간초과로 틀렸음.


# 개선
# 각 스테이지에 도달한 플레이어 수, 
# 실패율을 구하는 방법
# 두 가지 구간에서 개선점이 있었다. 
# 특히 실패율을 구할 때 일일이 arr.count() 를 하는 것보다 Counter 를 사용하여 훨씬 단축시킬 수 있었다

from collections import Counter
def solution(N, stages):
    c = Counter(stages)
    answer = []
    # 개선구간 1
    # 각 스테이지에 도달한 플레이어 수 = 전체 플레이어 - 이전 스테이지에서 탈락한 플레이어 수
    s = [0] * (N+1)
    s[1] = len(stages)
    for i in range(2,N+1):
        s[i] = s[i-1]-stages.count(i-1)
    
    fail=[]
    # 개선구간 2
    for i in range(1,N+1):
        if c[i]==0:
            fail.append((i,0))
        else:
            fail.append((i,c[i]/s[i]))
    fail.sort(key=lambda x:x[1], reverse=True)
    return [ x[0] for x in fail]
