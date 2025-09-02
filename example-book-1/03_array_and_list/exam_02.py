# 7의 개수
# 머쓱이는 행운의 숫자 7을 가장 좋아합니다. 
# 정수 배열 array가 매개변수로 주어질 때, 7이 총 몇 개 있는지 return 하도록 solution 함수를 완성해보세요.


def solution1(array):
    answer = "".join(str(array))
    return answer.count('7')

# 풀이과정
# array의 모든 원소를 문자열로 변환 후 합친 후 '7'의 개수를 count 메서드로 세어 반환


# 리팩토링
def solution(array):
    answer = "".join(map(str,array))
    return answer.count('7')
# 첫 풀이에서 사용했던 str(array)는 array 전체를 문자열로 변환하기 때문에 '[' 와 ',' 같은 문자도 포함된다.
# 따라서 map(str, array)를 사용하여 array의 각 원소를 문자열로 변환한 후 합치는 것이 더 정확하다.