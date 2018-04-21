
from random import randint

def conversor(f,c):
	elegir=(input("\n1. ºC a ºF\n2. ºF a ºC\n" ))
	if(elegir==1):
		c=(input("Ingrese grados Celsius\n"))
	 	f=c*(9/5)+32
	 	print(c+"ºC = "+f+"ºF")
	else:
	 f=(input("Ingrese grados Fahrenheit\n"))
	 c=(f-32)*(5/9)
	 print(f+"ºF = "+c+"ºC")

def dividir():
	print("Divisibles de 5 y 7 entre 1500 y 2700")
	for x in range(1500, 2700):
		if x%5==0 || x%7==0
		print(x)


def adivinar():
	y =randint(0,9)
	x=20
	while(x!=y):
		x=(input("Adivina el numero"))
		if x > y:
			print("El numero secreto es menor")

		if y < x:
			print("el numero es mayor")
	
	y=(input("correcto"))


def invertir:
	inv = ''
	stri = input("Ingrese frase a invertir ")
	c = len(stri)
	while (c>0):
		inv=inv+stri[c-1]
		c-=1
	print("la palabra invertida es "+inv)


def buscapares(minimo, maximo):
	pares=0
	impares=0
	for i in range(minimo,maximo):
		if(i%2==0):
			pares+=1
		else:
			impares+=1
	print("numero de pares en el rango "+pares)
	print("numero de impares en el rango "+impares)

class tipodato:
	lista = [1452, 11.23, 1 + 2j, True, 'w3resource', (0, -1), [5, 12], {"clase": 'V', 'section': 'A'} ]
	def act(self):
		for x in range(0,len(datalist)):
		print(lista[x])
		print(type(lista[x]))

class impresora6:
	def act():
		for x in range(0,6):
		if x==3 or x==6:
			continue
			print(x)

class facto:
	def act(fac):
		acum =0
		for x in range(1,fac):
			acum = acum*x
		print(acum)


class novocal:
	def act(txt):
	vocales = ['a','A','e','E','i','I','o','O','u','U']
	new = ''
	for token in txt:
		if token not in vocales:
			new += token
	print(new)



def main:

	print("programa1")
	dividir()
	print("Programa2 ")
	conversor();
	print("programa3")
	adivinar()
	print("programa4")
	print("programa5")
	invertir()
	print("programa6")
	buscapares(0,10)
	print("programa7")
	ej7=tipodato()
	ej7.act()
	print("programa8")
	ej8=impresora6()
	ej8.act()
	print("programa9")
	ej9=facto
	ej9.act(32)
	print("programa10")
	ej10=novocal()
	ej10.act("tarea del curso de web")

