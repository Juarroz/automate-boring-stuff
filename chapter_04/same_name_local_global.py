def spam():
    global eggs
    eggs = 'spam' # this is a global variable, rule 2

def bacon():
    eggs = 'bacon' # this is a local variable, rule 3

def ham():
    print(eggs) # this is a global variable, rule 4

eggs = 'global' # this is a global variable, rule 1
spam()
print(eggs)

