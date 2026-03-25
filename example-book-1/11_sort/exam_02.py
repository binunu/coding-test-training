# 숫자 짝꿍
# 두 정수 X, Y의 임의의 자리에서 공통으로 나타나는 정수 k(0 ≤ k ≤ 9)들을 이용하여 만들 수 있는 가장 큰 정수를 두 수의 짝꿍이라 합니다(단, 공통으로 나타나는 정수 중 서로 짝지을 수 있는 숫자만 사용합니다). X, Y의 짝꿍이 존재하지 않으면, 짝꿍은 -1입니다. X, Y의 짝꿍이 0으로만 구성되어 있다면, 짝꿍은 0입니다.

# 예를 들어, X = 3403이고 Y = 13203이라면, X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 3, 0, 3으로 만들 수 있는 가장 큰 정수인 330입니다. 다른 예시로 X = 5525이고 Y = 1255이면 X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 2, 5, 5로 만들 수 있는 가장 큰 정수인 552입니다(X에는 5가 3개, Y에는 5가 2개 나타나므로 남는 5 한 개는 짝 지을 수 없습니다.)
# 두 정수 X, Y가 주어졌을 때, X, Y의 짝꿍을 return하는 solution 함수를 완성해주세요.


from collections import Counter
def solution(X, Y):
    x = Counter(X)
    y = Counter(Y)
    summ = x & y
    if not summ:
        return "-1"
    
    ss = sorted(summ.keys(), reverse=True)
    if ss[0] == '0': return '0'
    
    answer = [k*summ[k] for k in ss]
    return "".join(answer)

# 
# 주요포인트 0. Counter연산, 1. for를 쓰지 않고 *으로 횟수 설정(효율성)
# 3. 리스트컴프리헨션,
# 4. 0을 빠르게 찾는방법 -> 내림차순 후 첫 글자가 0 이면 모두 0임 (매우 큰 숫자일 경우 int(str)로 변환하는 방식을 썼을 때 시간이 오래걸림)
