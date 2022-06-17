def moon_travel(height, width, area) -> int:
    answer = 101

    def move(weight: int, x: int, y: int, result: int):
        nonlocal answer, height, width, area

        if not (0 <= y < width):
            return
        if height <= x:
            answer = min(answer, result)
            return

        for w in [-1, 0, 1]:
            if w == weight:
                continue
            move(w, x+1, y+w, result + area[x][y])

    for i in range(len(area[0])):
        move(2, 0, i, 0)
    return answer


height, width = map(int, input().split())
arr = []
for _ in range(height):
    arr.append(list(map(int, input().split())))
print(moon_travel(height, width, arr))
