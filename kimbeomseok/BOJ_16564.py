def solve(n, team, point):
    low, high = min(team), max(team) + point
    answer = low
    team.sort()

    while low <= high:
        pivot = (low + high) // 2
        temp_point = 0
        for member in team:
            if pivot <= member:
                break
            temp_point += pivot - member
        if temp_point <= point:
            answer = pivot
            low = pivot + 1
        else:
            high = pivot - 1
    print(answer)


n, point = map(int, input().split())
team = []
for _ in range(n):
    team.append(int(input()))
solve(n, team, point)
