
#정수 배열 array와 정수 n이 매개변수로 주어질 때, array에 들어있는 정수 중 n과 가장 가까운 수를 return 하도록 solution 함수를 완성해주세요.




def solution(array, n):
    answer = 0
    # 가장작은수부터 보면서, n보다 커질때를 찾고, 그 이전, 이후두개를 확인해서 차이나는거 찾기
    array.sort()
    idx = -1
    for x in array:
        if x == n:
            return n
        else:
            if x > n:
                idx = array.index(x)
                break
    if idx == 0 : return array[0]
    if idx == -1 : return array[-1]

    pre = abs(array[idx-1]-n)
    nxt = abs(array[idx]-n)
    return array[idx-1] if pre <= nxt else array[idx]


# 개선)
# 정렬의 인자를 설정하는 방법으로 훨씬 간단하게 풀이 가능 

def solution(array, n):
    array.sort(key = lambda x: (abs(x-n),x)) 
    return array[0]