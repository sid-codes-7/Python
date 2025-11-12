def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed") # check if number is less than or equal to 0.
    
    count = 0 #starts the step count to 0
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        count += 1
    return count #returns the amount of steps taken
