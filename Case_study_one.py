print('''Hello! Welcome to Unibuddy
      
You're online buddy personalised to help you naivigate your university experience.

To help us understand your desired experiences 

Please answer the following questions below: 
''')

name = str(input("Please enter your name: ")).lower()
age = int(input("Please enter you age: "))
colour = str(input("Please enter your favourite colour: ")).lower()

print("Hello " + name + "!")
if age <= 22:
    print('''
We have a range of clubs and activities to help you feel comfortable:
1. Welcome to univerity club
2. Salsa, Bachata, Street Dance 
3. Football, Basketball, Hockey, Reading clubs and many more
''')

elif age >22:
    print('''
We have a range of clubs and activities to help you feel comfortable: 
1. Bar meet ups, Cafe meet ups, Hiking
2. Group activities e.g puzzles, board games, card against humanity
3. Sports and Dance activities e.g Football, Salsa, Flamenco
''')
    
else: 
    print("Please enter your correct age")

if colour == "blue" or colour == 'grey' or colour == "white":
    print('''
We also have many options that involve your favourite colour: 
1. Art Classes
2. Swimming activities
3. Skygazing 
''')
    
elif colour == "red" or colour == "orange" or colour == "yellow" :
    print('''
We have many options that involve your favourite colour:
1. Art Classes
2. Martial Arts
3. Pottery Classes 
''')

else:
    print("I'm not sure you have picked a correct colour")

question = input("Is there any questions you would like to ask me:").lower()

if question == "how are you ":
    print("I am good thank you!")

elif question == "i am confused":
    print("University may seem scary but with these clubs and activities we will make sure to help you get settled")

elif question == "no":
    print("Have an amazing university experience! ")

else: 
    print("I am not sure how to answer that. We have many staff members across campus, you are welcome to ask them any questions")

    

