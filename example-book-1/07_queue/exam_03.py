# 운영체제의 역할 중 하나는 컴퓨터 시스템의 자원을 효율적으로 관리하는 것입니다. 이 문제에서는 운영체제가 다음 규칙에 따라 프로세스를 관리할 경우 특정 프로세스가 몇 번째로 실행되는지 알아내면 됩니다.

# 1. 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.
# 2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
# 3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.
#   3.1 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료됩니다.
# 예를 들어 프로세스 4개 [A, B, C, D]가 순서대로 실행 대기 큐에 들어있고, 우선순위가 [2, 1, 3, 2]라면 [C, D, A, B] 순으로 실행하게 됩니다.

# 현재 실행 대기 큐(Queue)에 있는 프로세스의 중요도가 순서대로 담긴 배열 priorities와, 몇 번째로 실행되는지 알고싶은 프로세스의 위치를 알려주는 location이 매개변수로 주어질 때, 해당 프로세스가 몇 번째로 실행되는지 return 하도록 solution 함수를 작성해주세요.
from collections import deque
def solution(priorities, location):
    answer = 0
    
    dq = deque()
    for i,p in enumerate(priorities):
        dq.append((i,p))
    
    priorities.sort()
    top = priorities.pop()
    while dq:
        i,p = dq.popleft()
        if top <=p :
            answer+=1
            if i==location:
                return answer
            
            top = priorities.pop() # 마지막요소일 때 pop을 하면 에러가 남
        else:
            dq.append((i,p))
    return 0

# 동일한 로직을 any()를 이용해서 더 간단하게 풀 수 있음
# 풀이
# 먼저 인덱스와 우선순위를 함께 저장
# 그리고 우선순위를 정렬하여 맨 마지지막부터 꺼내면서 비교
# 이걸 any()를 이용해서 더 간단하게 구현 가능
# if any(x[1] > p for x in deque) 를 사용하면 더 간단하게 우선순위 비교 가능
# 그리고 만약 가장 마지막 요소가 마지막에 꺼내지는 상황에서는, return을 하기 전에 top을 갱신하면 에러가 발생할 수 있기에 (없는 요소를 pop하려고 하기 때문)
# top 갱신을 return 후에 하도록 함