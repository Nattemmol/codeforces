from collections import Counter


def broken_keyboard():
    t = int(input())

    for _ in range(t):
        ans=[]
        s = input()

        count = Counter(s)
        
        for k in count.keys():
            if count[k] %2 == 1:
                ans.append(k)
        freq = 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                freq += 1
            else:
                if freq % 2 == 1:
                    ans.append(s[i])
                freq = 1
        ans_set = set(ans)
        list_ans = list(ans_set)

        list_ans.sort()
        print("".join(list_ans))
    return
broken_keyboard()
