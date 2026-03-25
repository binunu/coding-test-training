# 프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.

# 또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

# 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

from collections import deque
def solution(progresses, speeds):
    answer = []
    dq = deque()
    for p, s in zip(progresses, speeds):
        dq.append(((100-p)+(s-1))//s)
    
    print(dq)
    s = dq.popleft()
    num=1
    while dq:
        if dq[0] <= s:
            dq.popleft()
            num+=1
        else:
            answer.append(num)
            s = dq.popleft()
            num=1
            
    answer.append(num)
    return answer

# 0. 앞에있는 기능은 완료되는대로 배포가능(뒷프로그램 생각x), 뒷기능 완료시 앞기능 배포일에 배포 -> 배포일 처음부터 돌면서, 숫자가 더 작은 프로그램들은 한번에 배포
# 1. dq에 아무것도안남을때까지(모두배포할때까지)
# 2. 각 기능이 배포되기까지의 날짜 계산