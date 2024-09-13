print("Funciones version 2")
print("Daniel Uribe")
# zona de listas tuplas set y diccionario
celulares=["Samsung a52","Iphone 11", "Chafa"]
carros=("toyota", "nissan", "Chevrolet")
paises={"Mexico", "Chile", "Argentina" }
tacos = {
    "tacos": "buche",
    "otro taco": "asada",
    "otrooo taco": "tripa"
}

# Zona de funciones
def verlista(telefonos):
    for uncelular in telefonos:
        print(uncelular)

def vertupla(coches):
    for loscarros in coches:
        print(loscarros)

def verset(Paisees):
    for lospaises in Paisees:
        print(lospaises)

def verdiccionario(deme2debuche):
    for lostacos,mastacos in deme2debuche.items():
        print(lostacos, mastacos)


#Llamadas a funciones
print("imprime celulares de una lista")
verlista(celulares)
print("")
print("imprime carros de una tupla")
vertupla(carros)
print("")

print("imprime paises de un set")
verset(paises)
print("")

print("imprime tacos de un diccionario")
verdiccionario(tacos)






