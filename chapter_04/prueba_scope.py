def duplicar_puntos(cantidad):
    cantidad = cantidad * 2  # Aquí cambiamos la variable LOCAL
    print(f"Puntos dentro de la función: {cantidad}")

puntos_globales = 50
duplicar_puntos(puntos_globales)

print(f"Puntos fuera de la función: {puntos_globales}")

def spam():
    print(eggs) # prints 'GLOBALGLOBAL'
eggs = 'GLOBALGLOBAL'
spam()
print(eggs)