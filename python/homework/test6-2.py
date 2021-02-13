final_answer = 0
times = 1
while True:   
    steps = 7 * times
    if (steps % 2 == 1) and (steps % 3 == 2) and (steps % 5 == 4) and (steps % 6 == 5):
        final_answer = times
        print(str(final_answer))
        break
    times += 1
    if times % 50 == 0:
        print(str(times) + "times of 7: " + str(7 * times))