import sys

#문제에서의 입력
N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().rstrip().split()))

#필요 변수들
set1  = 0 #집합의 합
count = 0 #집합 수
result = 0
#홀수 짝수 나누기 결정
decide = sum(A) % 2

#판단
#홀수 나누기
if decide == 1:
    for i in A:
        set1 += i
        if(set1 % 2 == 1):
            count += 1
            set1 = 0
    if count % 2 == 1:
        result = 1
    
        
        
    
#짝수 나누기
else:
    for i in A:
        set1 += i
        if(set1 % 2 == 0):
            count += 1
            set1 = 0
    if count % 2 == 0:
        result = 1
    else:
        # 2 2 2처럼 짝수가 홀수개 있는 경우 캐치하기 위해서 
        if set1 == 0 and count != 1:
            result = 1
        
        
    
#결과 출력
print(result)