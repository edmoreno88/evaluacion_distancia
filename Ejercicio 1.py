# creamos una clase base llamada "Animal"
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad    

# creamos un metodo "comer"
    def comer(self):
	    print(f"{self.nombre} está comiendo.")
	 
# Creamos una clase derivada llamada "Perro" que hereda de "Animal"
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza
    def ladrar(self):
	    print(f"{self.nombre} está ladrando.")
	 
	# Creamos una clase derivada llamada "Gato" que también hereda de "Animal"
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color
    
    def maullar(self):
     print(f"{self.nombre} está maullando.")
	 
# Creamos instancias de las clases
mi_perro = Perro("Rocko", 3, "Doberman")
mi_gato = Gato("Garfiel", 2, "Negro")
	 
	# Llamamos a métodos de las instancias
mi_perro.comer()
mi_perro.ladrar()
	 
mi_gato.comer()
mi_gato.maullar()
	 
	# Accedemos a los atributos de las instancias
print(f"{mi_perro.nombre} tiene {mi_perro.edad} años y es de raza {mi_perro.raza}.")
print(f"{mi_gato.nombre} tiene {mi_gato.edad} años y es de color {mi_gato.color}.")
