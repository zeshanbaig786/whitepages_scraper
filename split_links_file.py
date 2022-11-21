linksFile = open("links.txt", "r")
i = 0
j = 0
try:
    while i <= 6:
        j = 0
        i += 1
        ithFile = open(f"links{i}.txt", "w")
        print(f'{i}th file')
        while j <= 100000:
            l = linksFile.readline()
            ithFile.write(l)
            j += 1
            ithFile.flush()
except Exception as e:
    print(e)