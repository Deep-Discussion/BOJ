n = int(input())
# arr = [0 for _ in range(n+1)] #메모리 낭비 그냥 value 만 계속 최신화 시켜주는 것이 더 효율적 일듯
#
# if n <= 2:
#     print(1)
#
# # arr[0] = 0
# arr[1] = 1
# arr[2] = 1
ne, _ne = 0, 1

for i in range(n):
    ne, _ne = (ne + _ne) % 1000000007, ne % 1000000007

print(ne)