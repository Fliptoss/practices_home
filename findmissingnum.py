def missing(n):
    num = set(n)

    output = []

    for i in range(1, n[-1] + 1):
        if i not in num:
            output.append(i)

    return output

listofnums = [1,2,3,5,6,8,10,11]

missing_nums = missing(listofnums)

print(" ".join(map(str, missing_nums)))