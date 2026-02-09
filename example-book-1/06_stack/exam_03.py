# 햄버거 가게에서 일을 하는 상수는 햄버거를 포장하는 일을 합니다. 함께 일을 하는 다른 직원들이 햄버거에 들어갈 재료를 조리해 주면 조리된 순서대로 상수의 앞에 아래서부터 위로 쌓이게 되고, 상수는 순서에 맞게 쌓여서 완성된 햄버거를 따로 옮겨 포장을 하게 됩니다. 상수가 일하는 가게는 정해진 순서(아래서부터, 빵 – 야채 – 고기 - 빵)로 쌓인 햄버거만 포장을 합니다. 상수는 손이 굉장히 빠르기 때문에 상수가 포장하는 동안 속 재료가 추가적으로 들어오는 일은 없으며, 재료의 높이는 무시하여 재료가 높이 쌓여서 일이 힘들어지는 경우는 없습니다.

# 예를 들어, 상수의 앞에 쌓이는 재료의 순서가 [야채, 빵, 빵, 야채, 고기, 빵, 야채, 고기, 빵]일 때, 상수는 여섯 번째 재료가 쌓였을 때, 세 번째 재료부터 여섯 번째 재료를 이용하여 햄버거를 포장하고, 아홉 번째 재료가 쌓였을 때, 두 번째 재료와 일곱 번째 재료부터 아홉 번째 재료를 이용하여 햄버거를 포장합니다. 즉, 2개의 햄버거를 포장하게 됩니다.

# 상수에게 전해지는 재료의 정보를 나타내는 정수 배열 ingredient가 주어졌을 때, 상수가 포장하는 햄버거의 개수를 return 하도록 solution 함수를 완성하시오.

from collections import deque
def solution(ingredient):
    answer = 0
    pattern = [1,2,3,1]
#     process=[]
#     i=0
#     while i < len(ingredient):
#         if len(process) >= 4 and process[-4:] == [1,2,3,1]:
#                 answer+=1
#                 process=process[:-4]
#         else:
#             process.append(ingredient[i])
#             i+=1
    
#     if len(process) >= 4 and process[-4:] == [1,2,3,1]:
#             answer+=1
    dq = deque()
    i = 0
    while i < len(ingredient) :
        if len(dq) < 4 or [dq[-4],dq[-3],dq[-2],dq[-1]] != [1,2,3,1]  : 
            dq.append(ingredient[i])
            i+=1
        else:
            answer+=1
            for _ in range(4):
                dq.pop()
    
    if len(dq) >= 4 and [dq[-4],dq[-3],dq[-2],dq[-1]] == [1,2,3,1]  : 
            answer+=1
    return answer

# 풀이과정
# 재료를 하나씩 쌓고, 길이가 4 이상이 되면 검사를 한다.
# 마지막 4개가 [1,2,3,1] 이면 제거하고 개수를 하나 늘린다. 
# 이 과정을 재료가 다 쌓일 때까지 반복하는데
# 마지막 재료를 넣은 후에도 한번 더 검사를 해준다. -> 개선의 여지가 있어보임
# 처음엔 일반 리스트로 구현했으나 시간초과 에러가 나서 deque를 사용하였다.

# 근데 pop을 쓰기 위해 deque를 썼는데 사실 리스트에도 pop을 쓸 수 있엇음!!!
# 또한, 파이썬의 슬라이싱은 관대해서, arr = [1,2] 일 때 원소 개수보다 더 큰 범위를 호출해도 에러가 안남. arr[-4:] 를 하면 arr = [1,2] 가 나옴.
# 그리고 마지막 재료 넣은 후 검사할 필요 없이, 재료를 넣고 -> 검사하는 순서로 실행하면 됨
# 더 간단히 한 최종 버전
def solution(ingredient):
answer = 0;
    arr = []
    for i in ingredient: 
        arr.append(i)
        if arr[-4:] == [1,2,3,1]:
            answer+=1
            for _ in range(4):
                arr.pop()
        
    return answer

