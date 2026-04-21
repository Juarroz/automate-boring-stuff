# -----------
# Scope Rules
# -----------
# 1. Code what is in global scope, outside all functions, can't use local variables
# 2. Code that is in one function's local scope can't use variables in any other local scope
# 3. Code in a local scope ca access global variables
# 4. You can use the same name for different variables if they are in different scopes. That is, there can be a local
#    variable named spam and a global variable named spam

print('rule 1: global no accede a local')
def rule_01():
    lapis = '2H'
rule_01()
# print(lapis) Error de definicion la variable lapis no esta definida en el global scope

print('\nrule 2: local no accede a local')
def rule_02():
    techo = 'Esta roto'
    rule_02_resultado()
    print(techo)

def rule_02_resultado():
    pared = 'Agrietado'
    techo = 'Se cayo'
rule_02() # techo no se modifica cuando llamamos la otra funcion dentro de la funcion, esta por fuera del alcance


print("\nrule 3: local SI accede a global * modifica con global statement")
def rule_03():
    print(banana)
banana = 'ummmm'
rule_03() # Imprime el global
print(banana)

print("\nrule 4: Local y global pueden tener el mismo nombre, local_global_same_name 'mala practica'")

def duplicar_puntos(cantidad):
    cantidad = cantidad * 2  # Aquí cambiamos la variable LOCAL
    print(f"\nPuntos dentro de la función: {cantidad}")

puntos_globales = 50
duplicar_puntos(puntos_globales)

print(f"Puntos fuera de la función: {puntos_globales}")
