def spam():
    global egg
    eggs = "Spam"

def bacon():
    eggs = "bacon"

def ham():
    print(eggs)

eggs = 42
spam()
print(eggs)