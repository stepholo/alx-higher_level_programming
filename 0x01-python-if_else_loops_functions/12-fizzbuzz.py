#/usr/bin/python3
def fizzbuzz():
    ''' Iterates trough a range of 100

    Return:
         If multiple of 3 print "Fizz" instead
         If multiple of 5 print "Buzz" instead
         if multiple of both 3 and 5 print "FizzBuzz"
    '''
    for i in range(1, 101):
        if i % 15 == 0:
            i = "FizzBuzz"
        elif i % 3 == 0:
            i = "Fizz"
        elif i % 5 == 0:
            i = "Buzz"
        print("{} ".format(i), end="")
