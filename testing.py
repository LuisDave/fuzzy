def timer (limit, tag):
    if limit > 0:
        limit = limit - 1
        #print (limit, " ", tag)
        return limit
    elif limit < 0:
        print("")
pass        

counter1 = 15
counter2 = 10
while counter1 > 0:
    timer_1 = timer(counter1 , 2)
    timer_2 = timer(counter2, 1)
    if timer_2 > 0:
        print(timer_1, " ", timer_2)
    elif timer_1 > 0:
        print(timer_1)
    counter1 -= 1
    counter1 -= 1
pass