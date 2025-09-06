print("Hello ! I am a Ai bot, what is your name?")
name = input()
print(f"Hello {name} nice to meet u ")
print("how re u feeling? agood/bad")
mood = input().lower()
if mood == "good":
    print("Im glad to hear that")
elif mood == "bad":
    print("Im sorry to hear that . Hope things get better for u soon")
else:
    print("I see, sometimes feelings are hard to put into words:).")


print(f"It was nice talking to you {name}, GoodBye!")

