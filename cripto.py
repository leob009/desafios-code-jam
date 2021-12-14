num = input('digite um numero de quatro digitos: ')
numCrip = []
for dig in num:
    digCrip = (int(dig) + 7) % 10
    numCrip.append(digCrip)


# troca o primeiro pelo terceiro
aux1 = numCrip[0]
numCrip[0] = numCrip[2]
numCrip[2] = aux1

# troca o segundo pelo quarto
aux2 = numCrip[1]
numCrip[1] = numCrip[3]
numCrip[3] = aux2
print(numCrip)