num = input('digite um numero: ')
numForm = []
contador = 0
for numero in num:
    camada = numForm.count('(') - numForm.count(')')
    numeroAnterior = num[contador - 1]

    if contador == 0:
        for c in range(0,int(numero)):
            numForm.append('(')

    elif numero > numeroAnterior:
        for c in range(0,int(numero) - camada):
            numForm.append('(')
    
    elif numero < numeroAnterior:
        for c in range(0, camada - int(numero)):
            numForm.append(')')

    numForm.append(numero)
    contador += 1

ultimoNum = numForm[-1:]

for c in range(0, int(ultimoNum[0])):
    numForm.append(')')

for item in numForm:
    print(item, end=' ')


