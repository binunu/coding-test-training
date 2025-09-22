# 잘라서 배열로 저장하기
# 문자열 my_str과 n이 매개변수로 주어질 때, 
# my_str을 길이 n씩 잘라서 저장한 배열을 return하도록 solution 함수를 완성해주세요.

def solution2(my_str, n):
    answer = []
    s = 0
    while len(my_str[s:]) >= n:
        answer.append(my_str[s:s+n])
        s += n
    if len(my_str[s:]) : 
        answer.append(my_str[s:])
    return answer

# 풀이과정
# 문자열을 n만큼씩 잘라 answer에 추가   
# 마지막에 남은 문자열이 있다면 answer에 추가




# 리팩토링
def solution(my_str, n):
    return [ my_str[i:i+n] for i in range(0, len(my_str), n)]    

# 파이썬의 슬라이싱은 아주 관대하기 때문에 arr[:n]에서 n이 배열의 길이보다 커도 에러가 나지 않음. 
# 있는 크기만큼만 반환