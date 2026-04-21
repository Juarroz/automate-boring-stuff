def spam():
    global eggs
    eggs = 'spam' # 2. A variable in a function with a global statement is always a global variable in that function.

def bacon():
    eggs = 'bacon' # 3. Otherwise, if a function uses a variable in an assignment statement, it is a local variable

def ham():
    print(eggs) # 4. However, if the function uses a variable but never in an assignment statement, it is a global variable

eggs = 'global' # 1. A variable in the global scope (that is, outside all functions) is always aglobal variable.
spam()
print(eggs)

