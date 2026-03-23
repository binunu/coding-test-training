# 카펫 – Level 2
# Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.

# Leo는 집으로 돌아와서 아까 본 카펫의 노란색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.

# Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.
import math
def solution(brown, yellow):
    tp = []
    num = brown + yellow
    for i in range(3, int(math.sqrt(num))+1):
        if num % i == 0:
            tp.append([i, num//i])

    for x,y in tp:
        if (x*2)+(y*2)-4 == brown:
            return sorted([x,y],reverse=True)

    return 

# 풀이과정
# 규칙찾기
# 
# 규칙찾기
# 노랑, 브라운의 개수로 n*m인지를 찾아내야함
# 노랑, 브라운의 개수로 알 수 있는것
# -> 전체 칸의 개수
# -> x,y 후보군(전체 칸의 개수의 약수인데 가로,세로가 각 3이상이어야함)

# 전체 칸의 개수의 약수를 구해서 각 약수에서 카펫을 만들 수 있는지 확인하면 됨
# 구한 약수 중 큰 수(열) *2 + 작은수 * 2(행) -4(모서리)

# 개선)
# 1. tuple은 불필요하다 -> 약수를 찾을 때 마다 바로 확인하면됨 
# 2. 둘 중 큰건 언제나 n//i이다.
import math
def solution(brown, yellow):
    num = brown + yellow
    for i in range(3, int(math.sqrt(num))+1):
        if num % i == 0:
            if (num//i*2)+(i*2)-4 == brown:
                return [num//i, i]