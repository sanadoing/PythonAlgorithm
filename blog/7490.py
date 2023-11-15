T = int(input())


def dfs(num, before, summ, string, before_num):
    global result
    if num == n:
        if summ == 0:
            result.append(string)
    else:
        next = num + 1
        dfs(next, '+', summ + next, string + '+' + str(next), next)
        dfs(next, '-', summ - next, string + '-' + str(next), next)
        if before == '':
            dfs(next, before, summ * 10 + next, string + ' ' + str(next), before_num * 10 + next)
        elif before == '+':
            dfs(next, before, summ - before_num + (before_num * 10 + next), string + ' ' + str(next),
                before_num * 10 + next)
        elif before == '-':
            dfs(next, before, summ + before_num - (before_num * 10 + next), string + ' ' + str(next),
                before_num * 10 + next)


for _ in range(T):
    n = int(input())
    result = []
    dfs(1, '', 1, '1', 0)
    result.sort()
    print('\n'.join(map(str, result)))
    print()
