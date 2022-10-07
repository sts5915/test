# 정수 제곱근 판별
# n이 양의 정수 x의 제곱이라면 (x+1)의 제곱을 리턴
# n이 양의 정수 x의 제곱이 아니라면 -1을 리턴


def solution(n):
    answer = 0
    x = n ** 0.5
    if x == int(x):
        answer = (x+1)**2
    else :
        answer = -1
    return answer
print(solution(122))