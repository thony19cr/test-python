#   Compresión de Lista #1
test = []

for x in range(250):
    x = x + 1
    test.append(x*2)

#  print(test)


#  Compresión de Lista #2
test2 = [x*2 for x in range(10)]

print("Compresión de lista 2: ", test2)
