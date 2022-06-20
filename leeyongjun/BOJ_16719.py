str = list(input())
result = ['' for _ in range(len(str))]

def recursive(arr, index):
    if not arr:
        return

    #문자열에서 제일 작은 알파벳의 인덱스를 찾는다.
    alphabet = min(arr)
    idx = arr.index(alphabet)
    #위치에 해당하는 알파벳을 초기화 해준다(사용된)
    result[index + idx] = alphabet
    print("".join(result))
    # 가장 작은 알파벳 이후의 탐색이 먼저 이루어져야한다.
    recursive(arr[idx+1:], index+idx+1)
    recursive(arr[:idx], index)

recursive(str, 0)