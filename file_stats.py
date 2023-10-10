def file_stats(filename):
    f = open(filename, "r")
    counter = 0
    average = 0
    unique = []
    num = 0
    s = f.read().splitlines()
    for x in s:
        for y in unique:
            if x == y:
                num = 1
        average = average+float(x)
        counter = counter+1
        if num == 0:
            unique.append(x)
        num = 0
    average = average/counter
    f.close()
    return average, unique

yes = file_stats("number.txt")

print(yes)