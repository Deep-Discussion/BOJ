#피보나치 수 7
import sys

n = int(sys.stdin.readline());

data =[]
data.append(0);
data.append(1);

def fibonacci(n):
    for i in range(2, n+1):
        data.append((data[i-1] + data[i - 2]) %1000000007)


fibonacci(n);
print(data[n])

