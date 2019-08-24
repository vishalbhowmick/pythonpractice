def guess():
    m = 50
    # m is the middle number in range of possible guesses
    counter = 1
    # counter is the number of guesses take.
    print("Please guess a number")
    condition = input("Is your guess " + '50' + "? (low means it's too low, yes means it's your guess and high means it's too high)\n ")
    while condition != 'yes':
        counter += 1
        if condition == 'low':
            m = m + 1
        elif condition == 'high':
            m = m - 1
        elif condition == 'yes':
            break
        condition = input("Is your guess " + str(m) + "? (0 means it's too low, 1 means it's your guess and 2 means it's too high)\n ")
    print("It took" , counter , "times to guess your number")
guess()
