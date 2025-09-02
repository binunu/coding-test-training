# 문자열 밀기
# 문자열 "hello"에서 각 문자를 오른쪽으로 한 칸씩 밀고 마지막 문자는 맨 앞으로 이동시키면 "ohell"이 됩니다. 
# 이것을 문자열을 민다고 정의한다면 문자열 A와 B가 매개변수로 주어질 때, 
# A를 밀어서 B가 될 수 있다면 밀어야 하는 최소 횟수를 return하고 밀어서 B가 될 수 없으면 -1을 return 하도록 solution 함수를 완성해보세요.
def solution(A, B):
    answer = 0
    while A != B:
        if answer >= len(A):
            return -1
        
        text = A[-1]   
        for a in A[:-1]:
            text+=a  
        A = text 
        answer+=1 
    
    return answer

# 풀이과정
# A와 B가 같아질 때까지 반복
# A의 길이만큼 반복했는데도 같아지지 않으면 -1 반환
# A의 마지막 문자를 잘라서 맨 앞으로 붙이고 나머지 문자들을 뒤에 이어붙여 A를 갱신
# 밀어야 하는 횟수를 1 증가
# A와 B가 같아지면 밀어야 하는 횟수를 리턴

# 리팩토링
def solution(A, B):
    for i in range(len(A)):
        if A == B:
            return i
        A = A[-1] + A[:-1]
    return -1 
# tip: A를 오른쪽으로 미는 부분을 A = A[-1] + A[:-1]로 간단히 표현할 수 있다



# 심화
# "hello"를 여러 번 회전하면 만들 수 있는 문자열은 
# 사실 A를 두 번 이어붙인 "hellohello" 안에 부분 문자열로 모두 들어있다.
# 그 부분문자열의 시작점이 A를 B로 만들기 위해 밀어야 하는 횟수이다.
# find() 함수는 찾는 문자열이 없으면 -1을 반환하므로,
# A와 B의 길이가 다르면 -1을 반환하도록 조건을 추가했다.


def solution(A, B):
    return (A+A).find(B) if len(A) == len(B) else -1