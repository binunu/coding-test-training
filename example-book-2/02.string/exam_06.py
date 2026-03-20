# 3진법 뒤집기 (level 1)
# 자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

def solution(n):
    answer = 0
    num = int(n)
    tmpstr = ''
    while num >= 3:
        tmpstr += str(num % 3)
        num = num //3    
    tmpstr+=str(num)
    
    tmpint=0
    for i in range(1,len(tmpstr)+1):
        print(tmpstr[-i], 3**i)
        tmpint+= int(tmpstr[-i]) * (3 ** (i-1))
    
        
    return tmpint