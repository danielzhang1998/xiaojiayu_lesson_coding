for each in range (100,1000):
    sum = 0
    listing = list(str(each))   # separate to three pieces
    for every in listing:
        sum += int(every) ** 3
    if sum == int(each):
        print("found the matching, it is " + str(each))