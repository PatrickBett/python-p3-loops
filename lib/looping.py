#!/usr/bin/env python3

def happy_new_year():
    i=10
    while i >= 0:
        if i == 0:
            print( "Happy New Year!")
        else:
            print(i)
        i-=1
#happy_new_year()

def square_integers(int_list):
    # code goes here!
    for i in int_list:
        print(i**2)
#square_integers([1,2,3,4,5,6,7,8,9,10])

def fizzbuzz():
    # code goes here!
   
    for i in range(101):
        if i % 3 ==0:
            print("Fizz")
        elif i % 5 ==0:
            print("Buzz")
        elif i % 3 and i % 5:
            print("FizzBuzz")
        else:
            print(i)
        
fizzbuzz()