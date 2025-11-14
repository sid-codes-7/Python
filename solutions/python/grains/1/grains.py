def square(number):

    if number not in range(1,65):
        raise ValueError("square must be between 1 and 64") # raise a value error
    
    return 2**(number-1) # takes the square number, subtracts it by 1, and powers it to the power of 2

def total():
    
    return 2**64-1 # returns total of grains on all squared
