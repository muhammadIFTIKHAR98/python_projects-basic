#This is the code for generating the Fibonacci series
#fibonacci series

def fibonacci():
    #generate first number
    a = 1
    yield a

    #generate second number
    b = 1
    yield b

    #now we will create a infinite rule usig while function
    while True:
        #return the sum of tw0 generated numbers
        c = a + b
        yield c
        #function will resume the loop on next call
        a = b 
        b = c

#Iterate through the fibonacci sequence untill a limit is reached
for num in fibonacci():
    if num > 50:
        break
    print(num)
