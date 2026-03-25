# 행렬의 곱셈(level 2)
# 2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.
def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))] 
    print(answer)
    for i in range(len(arr1)):
        for k in range(len(arr2[0])):
            for j in range(len(arr1[0])):            
                answer[i][k] += arr1[i][j] * arr2[j][k]
                
    return answer

# 풀이과정.
# arr1의 행과 arr2의 열을 돌면서 
# 같은 차수의 (arr1열, arr2행) 값을 곱해나감