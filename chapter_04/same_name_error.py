def spam():
    print(eggs) # ERROR
    # eggs = 'spam local' esto combierte la variable global en local y cae en error

eggs = 'global'
spam()