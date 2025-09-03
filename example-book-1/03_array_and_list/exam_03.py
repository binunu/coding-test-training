# 가장 큰 수 찾기
# 정수 배열 array가 매개변수로 주어질 때, 
# 가장 큰 수와 그 인덱스를 담은 배열을 return 하도록 solution 함수를 완성해보세요.

def solution(array):
    return [max(array), array.index(max(array))]

# 중복된 숫자가 없다는 것을 힌트로, index()사용 -> 가장 첫 인덱스만 찾음