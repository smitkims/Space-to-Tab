K = int(input())
lst = input().split('\t')
ans = ''

for i in lst:
    text = ''
    while K <= len(i):
        if i[K-1] == ' ':
            j=K-1
            for p in range(len(i[:K-1])):
                if i[j-1] == ' ':
                    j -= 1
                else:
                    break
            text += i[:j]
            text += '\t'
        else:
            text += i[:K]
        i = i[K:]
    text += i
    ans = ans + text + '\t'

ans = ans[0:len(ans) - 1]
print(ans)
print(len(ans))
