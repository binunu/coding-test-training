# 점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다. 학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다. 예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.

# 전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.


def solution(n, lost, reserve):
    answer = 0 
    arr = [1] * n
    for x in lost:
        arr[x-1] -= 1
    for x in reserve:
        arr[x-1] += 1 
    if arr[:2] == [0,2]: 
        arr[:2] = [1,1]
    for i in range(1, n-1):
        if arr[i] == 0:
            if arr[i-1] == 2:
                arr[i] += 1
                arr[i-1] -= 1
            elif arr[i+1] == 2:
                arr[i] += 1
                arr[i+1] -= 1
    if arr[-2:] == [2,0]:
        arr[-2:] = [1,1]
    return n-arr.count(0)


# 풀이과정
# 앞에서부터 돌 때, 앞사람껄 빌리는게 무조건 이득. 그래야 뒤에서 필요하면 뒷사람이 빌려줄 수 있음. 
# 빌리고 도난당한 후 각 학생이 가진 체육복의 개수를 배열에 저장
# 전체 학생을 돌며 [2,0] 이 있으면 [1,1] 로 만듦(앞사람의 체육복 빌리기)
# 만약 앞사람이 없으면 뒷사람까지 검사[0,2] -> [1,1]

# 그리고 맨 앞고 맨 뒤가 0일 경우는 따로 처리(반복문 돌기 전, 후)

# 내 코드 개선) 
# 학생이 n명이면 애초에 배열의 크기를 n+2(맨앞 1개, 맨뒤 1개 추가)로 만들어서 연산을 한번만 수행할 수 있다.
# 앞에서부터 돌 때, 앞사람껄 빌리는게 무조건 이득. 그래야 뒤에서 필요하면 뒷사람이 빌려줄 수 있음. 
# 각 체육복의 개수를 배열에 저장
def solution(n, lost, reserve):
    answer = 0 
    arr = [0] + [1] * n + [0] # 앞뒤에 하나씩 더 생성
    for x in lost:
        arr[x] -= 1
    for x in reserve:
        arr[x] += 1 
    # if arr[:2] == [0,2]: 
    #     arr[:2] = [1,1]
    for i in range(1, n+1): # 범위 조절
        if arr[i] == 0:
            if arr[i-1] == 2:
                arr[i] += 1
                arr[i-1] -= 1
            elif arr[i+1] == 2:
                arr[i] += 1
                arr[i+1] -= 1
    # if arr[-2:] == [2,0]:
    #     arr[-2:] = [1,1]
    return sum(1 for a in arr if a >= 1)


# 개선 1 (다른접근법)
# 내 풀이는 일단 학생수만큼 반복을 진행해야 하기 때문에 
# 학생수가 매우 많은데 도난당한 학생 수가 적을 때 비효율적일 수 있다. 
# 그래서 애초에 빌려야 하는 학생과 빌려줄 수 있는 학생을 저장해놓는다면 더 효율적일 것이다.
# 개선된 풀이
def solution(n,lost,reserve):
    need = sorted([x for x in lost if x not in reserve]) # 빌려야하는 학생 = reserve에 없고 lost에 있는 학생
    give = [x for x in reserve if x not in lost] # 빌려줄수있는 학생 = lost에 없고 reserve에 있는 학생
    #앞에서부터 순서대로 확인하려면 sort가 된 상태여야함
    cnt = 0
    # 빌려주기
    for x in need:
        if x-1 in give:
            give.remove(x-1)
            cnt+=1
        elif x+1 in give:
            give.remove(x+1)
            cnt+=1
            
    return n - len(need) + cnt
    

# 개선 2)
# 위 코드에서 need와 give를 정의할 때, set을 쓰면
# in연산과 remove연산이 훨씬 효율적이어짐
need = set(lost)- set(remove)
give = set(reserve) - set(lost)
