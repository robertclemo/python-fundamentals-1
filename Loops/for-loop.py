
counteri = 0
counterj = 0
counterx = 0
countery = 0


for i in range(1, 11): # this will loop 10 times
    print(' ')
    print(f'\033[1;31;40mi -----------------{i}')    
    counteri+=1
    for j in range(1, 6): # this will loop 5 times
        print(f'\033[1;33;40mj -----------{j}')
        counterj+=1
        for x in range(1, 4): # this will loop 3 times
            print(f'\033[1;34;40mx ------ {x}')
            counterx+=1
            for y in range(1, 3): # this will loop 2 times
                print(f'\033[1;35;40my - {y}')
                countery+=1
                # for a total of 300 loops
    # First iteration
    # i loops first time (1)
        # j loops the first time (1)
            # x loops the first time (1)
                # y loops 2 times
    
    # Second iteration
    # i loops first time (2)
        # j loops the first time (2)
            # x loops the first time (2)
                # y loops 2 times
    
    # Third iteration
    # i loops first time (2)
        # j loops the first time (2)
            # x loops the first time (2)
                # y loops 2 times
    #...

totalCount = counteri + counterj + counterx + countery
print(f'''\033[0;36;40m
   i ................. {counteri}
   j ................. {counterj}
   x ................. {counterj}
   y ................. {countery}
   total count........ {totalCount} 
''') # total 510




