if __name__ == '__main__':
    dic = {}
    s = list()
    for _ in range(int(input())):

        name = input()
        score = float(input())
        if score in dic:
            dic[score].append(name)
        else:
            dic[score] = [name]
        if score not in s:
            s.append(score)
    n = min(s)
    s.remove(n)
    n1 = min(s)
    dic[n1].sort()
    for i in dic[n1]:
        print(i)