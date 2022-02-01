'''
##########################################
Lab 2.03 - Game Show
##########################################
In your Notebook
Follow the flow of execution in the following programs and predict what will happen for each
one
---------------------------------------
Example 1
---------------------------------------
a = input("What... is your quest")
b = "to seek the holy grail"
if a != b:
    print("Go On. Off you go")
else:
    b = input("What...is the air-speed velocity of an unladen swallow?")
    if b == "What do you mean? An African or European swallow?":
        print("I don't know that...AHHH [Bridgekeeper was thrown over bridge]")
    else:
        print("[you were thrown over bridge]")

Prediction: for else to run and your anwser
Actual: the first else did not work but second did which im confused about 

---------------------------------------
Example 2
---------------------------------------
user_input = input("What is your favorite color")
if user_input == 'blue':
    print("Blueskadoo")
elif user_input == "red":
    print("Roses are red!")
elif user_input == "yellow":
    print("Mellow Yellow")
elif user_input == "green":
    print("Green Machine")
elif user_input == "orange":
    print("Orange you glad I didn't say banana.")
elif user_input == "black":
    print("I see a red door and I want it painted black")
elif user_input == "purple":
    print("And we'll never be royalllssss")
elif user_input == "pink":
    print("Pinky- and the Brain")
else:
    print("I don't recognize that color. Is it even...??")

Prediction:what ever color they say it will give a response with that color
Actual:it gave the correct repsonses 

---------------------------------------
In your Notebook
---------------------------------------
Translate this Snap! program into a Python program
***Refer to the image provided on Moodle located below the Lab 2.03 link***
Write program below:

---------------------------------------
Create a game show program
---------------------------------------
Declare 10 prizes (prize1, prize2, prize 3 at the top of your file)
User picks a number
The prize corresponding with that door is printed for the user.
Write code below the multiline comment
'''
x = int (input ("what is x"))
y = int (input ("what is y"))
z = int (input ("what is z"))
if x + y > z and x + z > y and y + z > x:
    print (f"the perimiter of the triangle is {x + y + z}")
    if x ** 2 + y ** 2 == z ** 2:
        print("this is a right triangle.")

    #determine if isoscelese, scalene, or equilateral 
    if x == y and y == z:
        print ("this is an equilaterial triangle.")
    elif x == y or z == y or x == z:
        print("This is an isosceles triangle.")
    else:
        print("this is a scalene triangle.")
else: 
    print("Sorry, these inputs do not make a triangle")
