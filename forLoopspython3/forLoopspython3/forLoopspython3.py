#the idea for the while loop is to iterate through something, most of the times the while loop is used for finite tasks that have predetermined lenght, while and for loops are interchangable.

exampleList = [1,5,6,6,2,1,5,2,1,4]

for numbers in exampleList:
    print(numbers)
#this code will print out each item in that list. Usually ,people will choose to actually do something with the items in the list more than just printing it out.

for x in range(1,20):
    print(x);
#this code is a generator function and is very efficient.
for i in range(0,15,3):
    print(i);
#in this case the foor loop is set up so that the number from 0 to 15 prints out, but based on a step of 3, so every number printed is the third number