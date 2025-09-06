print("Hello , I am an Ai chat bot, what is ur name?")
name = input()
print(f"That is a nice name {name}, nice to meet you ")
print("How are you feeling ? (good/bad):")
mood = input().lower()
if mood == "good":
    print("Nice to hear that")
elif mood == "bad":
    print("Im sorry to hear that , i hope things will get better for u . It definetly will:) .")
else:
    print(" understand , sometimes its hard to put feelings into words :) .")

print("Tell me , What are youre hobbies:") 
input()
print("That is such a nice hobby")
print("My favourite hobbie is chess, Do u like chess (no/yes) :")
like = input().lower()
if like == "yes":
    print("tHATS GREAT WE CAN PLAY TOGHETHER SOMETIMES!!")
elif like == "no":
    print("That okay everyone has diffrent intrests")
else:
    print("ok.")
print("Last question, which instrument do u prefer(guitar/ukelele)?.")
instrument = input().lower()
if instrument == "guitar":
    print("OH thats, nice it my favourite instrument too.")
else:
    print("Same here glad we both like the same instrument")

print(f"It was nice talking to you {name}, Have a nice day.Goodbye")