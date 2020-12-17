
def output(s):
    moves = len(s)
    s=s+['end']
    # print(s)
    i = 0
    series=""
    while (i < len(s) - 1):
        # Counting occurrences of s[i]
        count = 1
        while s[i][0] == s[i + 1][0]:
            i += 1
            count += 1
            if i + 1 == len(s):
                break
        series=series+(str(count)+str(s[i][0]))
        i += 1
    print(moves,'moves',series) #prints number of moves and series of moves