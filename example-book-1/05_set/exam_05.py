# 두 문자열 s와 skip, 그리고 자연수 index가 주어질 때, 다음 규칙에 따라 문자열을 만들려 합니다. 암호의 규칙은 다음과 같습니다.

# 문자열 s의 각 알파벳을 index만큼 뒤의 알파벳으로 바꿔줍니다.
# index만큼의 뒤의 알파벳이 z를 넘어갈 경우 다시 a로 돌아갑니다.
# skip에 있는 알파벳은 제외하고 건너뜁니다.
# 예를 들어 s = "aukks", skip = "wbqd", index = 5일 때, a에서 5만큼 뒤에 있는 알파벳은 f지만 [b, c, d, e, f]에서 'b'와 'd'는 skip에 포함되므로 세지 않습니다. 따라서 'b', 'd'를 제외하고 'a'에서 5만큼 뒤에 있는 알파벳은 [c, e, f, g, h] 순서에 의해 'h'가 됩니다. 나머지 "ukks" 또한 위 규칙대로 바꾸면 "appy"가 되며 결과는 "happy"가 됩니다.

# 두 문자열 s와 skip, 그리고 자연수 index가 매개변수로 주어질 때 위 규칙대로 s를 변환한 결과를 return하도록 solution 함수를 완성해주세요.


def solution(s, skip, index):
    answer = ''
    apb = 'abcdefghijklmnopqrstuvwxyz'
    arr = list(set(apb)-set(skip))
    arr = "".join(sorted(arr))
    for x in s:
        i = arr.find(x)
        answer += arr[(i+index)%len(arr)]
    return answer

# 아래 코드가 안되는 이유:
# 만약 skip 요소가 너무 많아서 s요소가 몇개 없어서 i-len(arr) 을 두 번 이상 해야할 경우를 고려하지 못함
# def solution(s, skip, index):
#     answer = ''
#     apb = 'abcdefghijklmnopqrstuvwxyz'
#     arr = list(set(apb)-set(skip))
#     arr = "".join(sorted(arr))
#     for x in s:
#         i = arr.find(x)+index
#         if i >= len(arr):
#             i = i-len(arr)
#         answer+=arr[i]
        
#     return answer


# 풀이과정
# 알파벳을 리스트로 생성하면 되긴 하는데 귀찮아서 그냥 문자열로 생성한 뒤 list로 만들엇음
# 그리고 set의 차집합을 사용해서(array.remove는 비효율적이라서) sip 요소를 제거
# 그 후 정렬해서 다시 문자열로 변환
# 그 후 s의 각 요소를 arr에서 찾아서 index만큼 뒤의 요소를 answer에 추가