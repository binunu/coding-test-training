# N으로 표현(level 3)
# 아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.

# 12 = 5 + 5 + (5 / 5) + (5 / 5)
# 12 = 55 / 5 + 5 / 5
# 12 = (55 + 5) / 5

# 5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
# 이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.

def solution(N, number):
    answer = 0
    sarr=[set([0]) for _ in range(9)]
    # 인덱스의미 설정.
    # n으로 i를 만드는데 필요한 최소개수? arr[number] 를 도출해야함
    # 가아니고 i개로 만들 수 잇는 리스트를 저장
    #n으로 사칙연산 + 더하기연산 하는걸 계속 더해감(+ 횟수세기)
    #set으로 중복을 줄여가면서 결과값 저장
    #그래서 각 횟수마다 목표숫자가 나오면 return
    #8번만에 안나오면 -1 return
    for i in range(1, len(sarr)):
        sarr[i].add(int(str(N)*i))
        for j in range(1, i):
            for x in sarr[j]:
                for y in sarr[i-j]:
                    sarr[i].add(x+y)
                    sarr[i].add(x-y)
                    sarr[i].add(x*y)
                    if y != 0:
                        sarr[i].add(x//y)
                
        
        if number in set(sarr[i]):
            return i
    return -1