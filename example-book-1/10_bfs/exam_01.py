# n개의 음이 아닌 정수들이 있습니다. 이 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# 사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.



# 풀이과정
# 처음 사고 : n번이 될 때까지 각 회차마다 +, -의 가능성을 계산
# 마지막  n번에서 목표숫자가 되면 카운트
# 그럼 2, 4, 8, 16 씩 경우의 수가 늘어날 것임. 2의 n제곱만큼.
# 근데 사고는 bfs인데 풀이방식은 다시보니 dfs 백트래킹임... 아래에서 bfs풀이를 다시 구현해봄


# 처음 풀이 dfs 방식으로 풀었음. 
def solution(numbers, target):
    answer = [0]
    n=len(numbers)
    def loof(i,res):
        if i == n :
            if res == target:
                answer[0] +=1 
            return
            
        loof(i+1,res+numbers[i])

        loof(i+1,res-numbers[i])

    loof(0, 0)
    return answer[0]

# 개선 1) nonlocal을 사용해서 anwser를 굳이 배열로 안해도 됨!!

def solution(numbers, target):
    answer = 0
    n=len(numbers)
    def loof(i,res):
        nonlocal answer
        if i == n :
            if res == target:
                answer +=1 
            return
            
        loof(i+1,res+numbers[i])

        loof(i+1,res-numbers[i])

    loof(0, 0)
    return answer

# 개선 2) answer 에다가 저장하지 않고, 그냥 개수를 각각 return하는 방식

def solution(numbers, target):
    n=len(numbers)
    def loof(i,res):

        if i == n :
            if res == target:
                return 1
            return 0
            
        return loof(i+1,res+numbers[i]) + loof(i+1,res-numbers[i])

    return loof(0, 0)


# bfs 풀이
# 풀이핵심은 현재까지 만들 수 있는 모든 합의 목록을 트리의 단계별로 쌓아나가는 것임

def solution(numbers, target):
    answer = [0]
    for num in numbers:
        temp = []
        for a in answer:
            temp.append(a+num)
            temp.append(a-num)
        answer = temp
    
    return answer.count(target)

# dp 풀이 (심화)
# bfs 풀이에서는 사실 모든 경우를 다 계산. (2의 n제곱 가지)
# 근데 db를 이용해 좀 더 효율적으로 고칠 수 있음.
# 중복되는 계산을 Counter 를 사용해서 하나로 합침

# dp는 해당 키 값을 만들 수 있는 경우의 수를 저장한다. 
# dp[n] = dp[a] + dp[b] + dp[c] ... 
# n을 만들 수 있는 모든 경로를 더함. 
# key를 만드는 모든 경우로 key+num 을 만들 수 있음
# 하지만 key+num을 만드는 경우의 수는 key를 만드는 경우의 수 외에도 다른 경로가 존재하므로 
# =를 하지 않고 += 을 해주는 것임.

from collections import Counter
def solution(numbers, target):
    dp = Counter()
    dp[0] = 1 # 0을 만들 수 있는 경우는 아무것도 더하거나 빼지 않았을 때 1가지 밖에 없음 - 문제조건에 숫자의 범위는 1 이상

    for num in numbers:
        temp = Counter()
        for key in dp:
            temp[key+num] += dp[key] 
            temp[key-num] += dp[key] 
            dp = temp
    return dp[target]