
var = ['python', 'java', 'php', 'javascript', 'c++']

print("Technologies items:", var)

#   Agregando items nuevos
var.append('html5')

print("Technologies items:", var)

#    Elminación de elementos en nuestra lista
var.remove('php')

print("Lista actualizada:", var)

var.append('php')

print(var)

var.pop(5)

var.pop(2)

print(var)

#   Invertir elementos de una lista

var.reverse()

print("Lista invertida: ", var)

#    Eliminar elemento repetido "python"

var.append("python")
var.append("python")

cantidad = var.count("python")

print("Cantidad de veces que se repite 'python': ", cantidad)

#    Eliminación de valor usando pop()

var.pop()
var.pop()

#    print("Lista actualizada: ", var)

#    Crear un nuevo elemento dentro de nuestro lista

var.append('angular')

print("Lista actualizada: ", var)

#    Utilizamos sort()

var2 = [6, 1, 35, 15, 2, 50]
var2.sort()

print("Segunda lista ordenada", var2)

var3 = ["windows", "linux", 30, 5.5]
# var3.sort()
# print("Tercera lista ordenada", var3)


#    Ordenando la primera lista

var.sort()
print("Primera lista ordenada: ", var)

