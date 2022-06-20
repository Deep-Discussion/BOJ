import collections

n, m = map(int, input().split(' '))
cakes = list(map(int, input().split(' ')))


div10 = []
rest = []
ans = 0

#10의 배수인 것 먼저 찾아서 커팅
while cakes:
    cake = cakes.pop()
    if cake % 10:
        rest.append(cake)
    else:
        div10.append(cake)

div10.sort(reverse=True)


def cutting(l):
    global ans, m

    if l == 10:
        ans += 1
        return
    elif l < 10:
        return
    elif m <= 0:
        return

    else:
        l -= 10
        ans += 1
        m -= 1
        if l > 10:
            cutting(l)
        elif l == 10:
            ans += 1
        return

while m:
    if div10:
        val = div10.pop()
        cutting(val)
        continue

    if rest:
        val = rest.pop()
        cutting(val)

    if not div10 and not rest:
        break

print(ans)