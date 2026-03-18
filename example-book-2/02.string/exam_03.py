# 튜플(level 2)
# 셀수있는 수량의 순서있는 열거 또는 어떤 순서를 따르는 요소들의 모음을 튜플(tuple)이라고 합니다. n개의 요소를 가진 튜플을 n-튜플(n-tuple)이라고 하며, 다음과 같이 표현할 수 있습니다.
# ...
#특정 튜플을 표현하는 집합이 담긴 문자열 s가 매개변수로 주어질 때, s가 표현하는 튜플을 배열에 담아 return 하도록 solution 함수를 완성해주세요.

def solution(s):
    answer = []
    arr= []
    step1 = s[2:-2].split("},{")
    for s in step1:
        arr.append(list(map(int,s.split(","))))  
    arr.sort(key=lambda x: len(x))
    for a in arr:
        for b in a:
            if b not in answer:
                answer.append(b)
    return answer

# 풀이설명
# 먼저 문자열을 잘 가공해서 숫자만 든 배열로 변환시켜준다. 
# 그리고 길이순으로 배열을 오름차순 한 후 
# 돌면서 요소를 하나씩 꺼내온다. 
# 문제에 제시된 조건으로 보아 
# arr을 돌면서 첫 요소부터 요소의 개수가 +1씩 증가하면서 이전에 없던 요소를
# 나온 순서대로 담으면 끝