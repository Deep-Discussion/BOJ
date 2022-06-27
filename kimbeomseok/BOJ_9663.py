def n_queen(n: int) -> None:
    ans = 0
    row = [0] * n
    visited = [False] * n

    def check_is_valid_direction(x) -> bool:
        for i in range(x):
            if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
                return False
        return True

    def solve(x: int) -> None:
        nonlocal ans, n, visited

        if n == x:
            ans += 1
            return

        for i in range(n):
            # [x, i]에 퀸을 놓는다.
            row[x] = i
            if check_is_valid_direction(x):
                visited[i] = True
                solve(x + 1)
                visited[i] = False

    solve(0)
    print(ans)
