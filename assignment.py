def add_one(value):
    return value + 1

for number in [1, 2, 3]:
    if number > 1:
        print(add_one(number))

# 1. What is printed, in order? Explain how the loop and the if condition
# decide which numbers are passed to add_one.
# Your answer: The output is: "3"\"4"  in that order and on sepreate lines. 
# the loop runs for all the numbers in the list but only prints if the inconditon is met.  The loop checks the numbers 1, 2, and 3, but the if condition only allows numbers greater than 1 to be used by add_one(). Therefore, the function adds 1 to 2 and 3, printing 3 and 4 in that order.

# 2. What does add_one(2) return? Explain the difference between return
# inside the function and print in the loop.
# Your answer: add_one(2) returns 3, because the function adds 1 to the given value.
#add_one(2) returns 3 because the function adds 1 to the value 2. The return statement sends the result back to the program (the computer sees it), while print() prints the result of the function (so I the user can see it ).
