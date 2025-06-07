class Reverser:
    def reverse(self,text):
        return' '.join(text.split()[::-1])
r = Reverser()
print(r.reverse("hello world this is python"))