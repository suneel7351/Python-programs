def patterntern(line):
    pattern = ""
    for i in range(0, line):
        for j in range(0, line):
            if ((j == 1 and i != 0 and i != line-1) or ((i == 0 or
                i == line-1) and j > 1 and j < line-2) or (i == ((line-1)/2)
                and j > line-5 and j < line-1) or (j == line-2 and
                                                   i != 0 and i != line-1 and i >= ((line-1)/2))):
                pattern = pattern+"*"
            else:
                pattern = pattern+" "
        pattern = pattern+"\n"
    return pattern


line = int(input("enter the number of lines : "))
print(patterntern(line))
