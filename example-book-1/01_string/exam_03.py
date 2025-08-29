# OX퀴즈
# 덧셈, 뺄셈 수식들이 'X [연산자] Y = Z' 형태로 들어있는 문자열 배열 quiz가 매개변수로 주어집니다. 
# 수식이 옳다면 "O"를 틀리다면 "X"를 순서대로 담은 배열을 return하도록 solution 함수를 완성해주세요.

def solution1(quiz):
    answer = []
    for test in quiz:
        test = test.rsplit("=",1)
        if eval(test[0])==int(test[1]):
            answer.append("O")
        else:
            answer.append("X")
    return answer

# 풀이과정
# 식의 왼쪽과 오른쪽을 '=' 기준으로 나눔
# 이전 문제에서 나왔던 eval() 함수를 사용한 적이 있어 이를 활용(안된다면 직접계산)
# if문을 사용해 O, X를 판단해 배열에 추가
# 최종 배열을 반환

def solution(quiz):
        return ["O" if eval(q.split("=")[0])==int(q.split("=")[1]) else"X" for q in quiz] 
# 리스트 컴프리헨션으로 한 줄로 만들 수 있다.
# 각 for문을 돌며 O, X를 판단해 최종 배열로 반환