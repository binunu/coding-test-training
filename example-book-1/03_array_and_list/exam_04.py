# 모의고사
# 수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 
# 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

from collections import deque
def solution(answers):
    rank=[[1,0],[2,0],[3,0]];
    s1 = deque([1, 2, 3, 4, 5])
    s2 = deque([2, 1, 2, 3, 2, 4, 2, 5])
    s3 = deque([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
    
    for a in answers:
        a1, a2, a3 = s1.popleft(), s2.popleft(), s3.popleft()
        
        if a1==a: rank[0][1]+=1
        if a2==a: rank[1][1]+=1
        if a3==a: rank[2][1]+=1
        
        s1.append(a1)
        s2.append(a2)
        s3.append(a3)
        
        maxV = max(rank, key=lambda x: x[1])[1]
        
    return [x[0] for x in rank if x[1] == maxV]

# 풀이과정
# 1, 2, 3번 수포자의 찍는 번호의 한 세트가 길이가 다 다르며
# 정답배열과의 길이도 다르기 때문에
# queue를 사용해서 ANSWER의 길이만큼 앞에서부터 뽑아내어 채점 후 다시 맨 뒤에 추가
# 채점이 끝난 후, 가장 많이 맞춘 사람의 점수를 구한 후
# 그 점수와 같은 사람을 모두 반환한다.

# 리팩토링
# tip: enumerate를 사용해서 for문을 돌릴 때 인덱스와 값을 함께 참조할 수 있다

def solution(answers):
    score = [0,0,0]
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ] 
    # 채점
    for i, v in enumerate(answers):
        for j, p in enumerate(patterns):
            if v == p[i%len(p)]: score[j]+=1
    # 최고점수
    maxV = max(score)
           
    # 최고점수를 받은 사람
    return [ i+1 for i, v in enumerate(score) if maxV==v]

# score배열에 점수만 기록하고 인덱스로 각 학생을 구분
# 채점을 할때와 최고점수를 받은 사람을 기록할 때 enumerate로 인덱스를 활용