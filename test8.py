# 2부터 20까지 짝수의 합
i=0
sum=0
# while i < 20 :
#     i = i +1
#     if i % 2== 0 :
#         sum = sum + i
# print(sum)

for index in range(2, 21):
    if index%2==0:
        sum += index
print(sum)


        