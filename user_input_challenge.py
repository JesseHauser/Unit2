'''
##############################
User Input Challenge
##############################

Create a program that asks the user to enter their name and their age. Print out a message 
addressed to them that tells them the year that they will turn 100 years old.

Add on to the previous program by asking the user for another number and printing out that 
many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. 
(Hint: the string "\n" is the same as pressing the ENTER button)
'''
from asyncore import loop


age = input ("what is your age")
num =  100 - int(age)
name = input ("what is your name")
print (f"{name} will turn 100 years old in {num} years")
num1 = input ("give me another number")
repeat =  num1 
sent = print (f"{name} will turn 100 years old in {num} years")

