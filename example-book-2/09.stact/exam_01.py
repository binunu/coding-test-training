# 주식가격 level 2
# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

def solution(prices):
    answer = [i for i in range(len(prices)-1,-1,-1)] 
    arr=[]
    now=0
    for i,p in enumerate(prices):
        while arr and p < arr[-1][1] :
            t, price = arr.pop()
            answer[t] = now-t
        arr.append([i,p])
        now+=1
        # 하나씩 넣으면서 만약 마지막 가격보다 떨어진게 나오면 기록? 
        # 현재초 - 넣었을 때의 초를 계산
    return answer

# 풀이과정
# 나는 처음에 모든 주식이 안떨어졌을 때의 초를 설정해두고
# 떨어진 시점을 저장
# ==> 남아있는걸 마지막에 한꺼번에 저장할 수도 있음(참고)