print('\n' + '='*20 + ' EJERCICIO 1: Basico ' + '='*20)
for i in range(101):
    print(i, end=', ' if i < 100 else '\n')


print('\n' + '='*20 + ' EJERCICIO 2: Multiplos de 2 ' + '='*20)
for i in range(2, 501, 2):
    print(i, end=', ' if i < 500 else '\n')


print('\n' + '='*20 + ' EJERCICIO 3: Contando Vanilla Ice ' + '='*20)
for i in range(1, 101):
    res = ""
    if i % 10 == 0: res = "baby"
    elif i % 5 == 0: res = "ice ice"
    else: res = str(i)
    print(res, end=', ' if i < 100 else '\n')


print('\n' + '='*20 + ' EJERCICIO 4: Wow. Numero gigante a la vista ' + '='*20)
suma = sum(range(0, 500001, 2))
print(f"La suma total de números pares es: {suma}")


print('\n' + '='*20 + ' EJERCICIO 5: Regresame al 3 ' + '='*20)
for i in range(2024, 0, -3):
    
    proximo = i - 3
    print(i, end=', ' if proximo > 0 else '\n')


print('\n' + '='*20 + ' EJERCICIO 6: Contador dinamico ' + '='*20)
numInicial, numFinal, multiplo = 3, 10, 2
resultados = []
for i in range(numInicial, numFinal + 1):
    if i % multiplo == 0:
        resultados.append(str(i))
print(", ".join(resultados))