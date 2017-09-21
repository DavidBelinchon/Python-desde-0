# -*- coding: utf-8 -*-
############## vars ############

a=26
b=11.3

print (a + b)


############## Listas #################

l = [2,"tres",True,["uno",2]]

print (l[1])

print (l[3][0])

l2 = [1,2,3,4,5,6]

print (l2[0:3])

# extreu els 3  primers cada 2
print (l2[0:3:2])

# extreu cada 2
print (l2[0::2])


############## tuplas (se poden reasignar sensecres pero no cambiar el contingut de la llista individualment)

t = 1,True,"hola"

print (t)

print (t[1])


########### maps ###############

d= {"clave1":1,
    "clave2":2,
     3:"numero 3"
   }

print (d["clave1"])
print (d[3])


############## conditionals #########
 
a = 1
b = 2

if a > b:
	print ("false")
else:	
	print ("true")
print("siempre se  executa")

if a > b:
	print ("false")
elif a < b:	
	print ("true")

 
########## bucles #################

a = 0

while  a < 5:
	print(a)
	a+=1

lista= ["l1","l2","l3","l4"]

for elem in lista:
	print(elem)

for lletra in "Paraula":
	print(lletra)

########### Funciones ###########

a = 1
b = 2

def suma(num1,num2):
	return num1 + num2


result = suma(a,b)

print (result)

def parameters(cad,v=2,*algomas):
	print (cad * v)
	for cadena in algomas:
		print (cadena)

parameters("pytnon",3,"hola","adios")


################## Classes ##############

class Humano:
	def __init__(self,nombre):
		self.nombre = nombre
		print ("humano creado")

	def hablar(self,mensaje):
		print (mensaje)


pedro = Humano("pedro")

pedro.hablar("hola me llamo "+pedro.nombre)

################ Herencia ##################

class Ingeniero(Humano):
	def programar(self,lenguaje):
		print ("voy aprogramar en "+ lenguaje)

class Abogado(Humano):
	def caso(self,casoNumero):
		print ("hoy tengo el caso numero "+ str(casoNumero))


raul = Ingeniero("raul")
raul.hablar("hola me llamo "+raul.nombre)
raul.programar("python")

sergi = Abogado("sergi")
sergi.hablar("hola me llamo "+sergi.nombre)
sergi.caso(423)

################ CADENAS Metodos ################ 

s = "hola mundo"

print (len(s))

print (s.count("o"))

print (s.lower())

print (s.upper())

print (s.replace("o","x"))

print (s.split(" "))

print (s.find("a"))


################ Listas metodos ################ 

lista = [1,"dos",3]

buscar = 1

print (buscar in lista)

print (lista.index(buscar)) 

if buscar in lista:
	print (lista.index(buscar))
else:
	print ("no existe elemento en la lista")


### añadir a la llista un element
lista.append("quatro")
print(lista)

###conta les vegades que apreix el 3
print (lista.count(3))

### inseta ala posicio que vulgos un element
lista.insert(0,"zero")
print(lista)


lista = [1,"dos",3]
lista2 = [1,"dos",3]

lista.extend(lista)
print(lista)

### borrar de la llista si no li pases parametre sera el ultim
lista.pop()
print(lista)

### borra el primer element que li pasis com a parametre
lista.remove("dos")
print(lista)

################ Funcio Map ################ 

def operador(n,m):
	return n+m

l1 = [1,2,3,4]
t1 = (9,8,7,6)

lr = map(operador,l1,t1)
print(lr)







