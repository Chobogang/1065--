n = int(input())

hansu = 0
for i in range(1, n+1):
    # 정수를 받을 때, 문자열로 바꿔서 받기
    num = list(map(int, str(i)))
    if i < 100:
        hansu += 1  
    elif num[0]-num[1] == num[1]-num[2]:
        hansu += 1  
print(hansu)