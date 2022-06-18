from typing import List


def prefix_array(_string: str) -> List[str]:
    arr = []
    c = ''
    for s in reversed(_string):
        c += s

        arr.append(c[::-1])

    return sorted(arr)

for word in prefix_array(input()):
    print(word)