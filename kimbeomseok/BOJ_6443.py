from typing import List


def track(length: int, string: str, alphabet: dict, answer: set) -> None:
    for k in alphabet.keys():
        if length <= 0:
            answer.add(string)
            break
        else:
            if 0 < alphabet[k]:
                alphabet[k] -= 1
                track(length - 1, string[:] + k, alphabet, answer)
                alphabet[k] += 1


def anagram(string: str) -> List[str]:
    alphabet: dict
    answer: set
    alphabet = dict()
    answer = set()

    for c in string:
        alphabet[c] = alphabet.get(c, 0) + 1

    track(len(string), '', alphabet, answer)

    return sorted(list(answer))


N = int(input())

for _ in range(N):
    result = anagram(input())

    for elem in result:
        print(elem)
