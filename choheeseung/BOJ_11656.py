s = input()
suffix = []

for i in range(len(s)):
    suffix.append(s[i:])

suffix.sort()

for i in range(len(s)):
    print(suffix[i])
