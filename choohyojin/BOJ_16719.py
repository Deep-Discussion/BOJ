def printWord(arr, visited):
    word = ""
    for i in range(len(arr)):
        if visited[i]:
            word += arr[i]
            
    return ''.join(word)

inputStr = list(input())
visited = [False for i in range(len(inputStr))]

idx = 0
for i in range(len(inputStr)):
    word = "Z" + printWord(inputStr, visited)
    
    for j in range(len(inputStr)):
        if not visited[j]:
            copied = list(visited)
            copied[j] = True
            newWord = printWord(inputStr, copied)
            
            if newWord < word:
                idx = j
                word = str(newWord)
                
    visited[idx] = True
    print(word)


