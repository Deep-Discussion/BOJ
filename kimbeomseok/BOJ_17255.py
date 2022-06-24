from typing import List


def make_n(_n: int) -> None:
    n = str(_n)
    total_length = len(n)
    answer_set = set()

    def solve(length: int, idx_list: List[int], order: List[str], result: str
              ) -> None:
        nonlocal answer_set, n, total_length

        if total_length <= length:
            _order = tuple(order)
            if _order in answer_set:
                return
            answer_set.add(_order)
            return

        for i in range(total_length):
            if i in idx_list or not min(idx_list) - 1 <= i <= max(idx_list) + 1:
                continue
            temp_str = result
            if i < idx_list[-1]:
                temp_str = n[i] + temp_str
            else:
                temp_str += n[i]
            solve(length + 1, idx_list + [i], order + [temp_str], temp_str)

    for idx in range(total_length):
        solve(1, [idx], [n[idx]], f'{n[idx]}')
    print(len(answer_set))


make_n(int(input()))
