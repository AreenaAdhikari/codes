class flashcard:
    def __init__(self,word,meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word+'('+self.meaning+')'
flash =[]
print("welcome to flash card application")
while(True):
    word = input("Enter the  word: ")
    meaning = input("Enter the meaning of ur word : ")
    flash.append(flashcard(word,meaning))
    option = int(input("Enter 0 if u want to add more flash cards else enter 1 : "))
    if (option):
      break
print("Your flashcards:")
for i in flash :
    print(i)

