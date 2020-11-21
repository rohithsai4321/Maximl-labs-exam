def max(str, a):
    count = [0] * NO_OF_CHARS
    for i in range(a):
        count[ord(str[i])] += 1

    maxdistinct = 0
    for i in range(NO_OF_CHARS):
        if (count[i] != 0):
            maxdistinct += 1
    return maxdistinct

def smallest(str):
    n = len(str)
    max_distinct = max(str, n)
    minl = n
    for i in range(n):
        for j in range(n):
            subs = str[i:j]
            subslenght = len(subs)
            sub_distinct_char = max(subs,subslenght)
            if (subslenght < minl and
                    max_distinct == sub_distinct_char):
                minl = subslenght

    return minl


s = input()
NO_OF_CHARS = 256
l = smallest(s)
print(l)