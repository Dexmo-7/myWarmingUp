"""
def fizzbuzz(value):
    counter = 1
    while value > 0:
        if counter % 15 == 0:
            print("FizzBuzz")
        elif counter % 5 == 0:
            print("Buzz")
        elif counter % 3 == 0:
            print("Fizz")
        else:
            print(counter)
        counter += 1
        value -= 1

value = int(input("How many numbers may be showed?: "))

fizzbuzz(value)

"""
#LIST COMPREHENSION SOLUTION
def fizzbuzz(value):
    total = ["FizzBuzz" if counter%15==0 else "Buzz" if counter%5==0 \
        else "Fizz" if counter%3==0 else counter for counter in range(1,value+1)]
    print(total)
    
value = int(input("How many numbers may be showed?: "))
fizzbuzz(value)
