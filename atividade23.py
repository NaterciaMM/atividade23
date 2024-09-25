# Crie um programa que receba um número do usuário e exiba a tabuada desse número de 1 a 10.
numusu = int(input("insira um numero: "))
for x in range(11):
    print ("{} x {}= {}".format(numusu,x,numusu*x))