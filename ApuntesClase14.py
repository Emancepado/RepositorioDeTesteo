import pygame
import random


# Clase 14

# Objetivos de la clase:
# - Aplicar Herencias
# - Conocer los polimorfismos
# - Ejecutar herencias multiples

# ----------------------------------------------------------------------------------------------------------------------------------

# Herencia

# La herencia es un proceso mediante el cual se puede crear una CLASE HIJA que hereda de una CLASE PADRE, compartiendo sus metodos y atributos
# Ademas, una clase hija puede sobreescribir los metodos o atributos o incluso definir unos nuevos

# Definamos una clase padre:

class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    # Metodos genericos pero con implementacion particular
    def hablar(self):
        pass

    def moverse(self):
        pass

    def describeme(self):
        print("Soy un animal del tipo", type(self).__name__)


# Creamos una clase hija que hereda de la padre al pasar la clase padre como parametro de la hija
# class Perro(Animal):    #esto fue actualizado por tu yo del pasado, la clase perro la ves mas abajo
#    pass

# Dado que una clase hija hereda los atributos y metodos de la padre, nos puede ser muy util cuando tengamos clases que se parecen e/ si pero tienen ciertas particularidades
# En este caso, podriamos tomar los elementos comunes de la clase "Animal" para que el resto de clases hijas las hereden
# Es importante respetar la filosofia DRY

# -------------------------------------------------------------------------------------------------------------------------------

# Principio de DRY
# Don't repeat yourself
# Cuanto mas codigo duplicado exista, mas dificil sera de modificar y mas facil sera crear inconsistencias
# Las clases y la herencia ayudan a no repetir codigo de manera innecesaria

# -------------------------------------------------------------------------------------------------------------------------------

# Creamos una clase vacia para ver como se heredan, por defecto, los atributos y los metodos

class Perro1(Animal):
    pass

#su_perro = Perro1("mamifero" , 10)
#su_perro.describeme()

class Perro(Animal):
    def hablar(self):
        print("Guau!")

    def moverse(self):
        print("Caminando con 4 patas")


class Vaca(Animal):
    def hablar(self):
        print("Hijo veni a tomar la choco")

    def moverse(self):
        print("Caminando a 4 patas")


class Abeja(Animal):
    def hablar(self):
        print("Bzzzzz!")

    def moverse(self):
        print("Volando")

    # Creamos un nuevo metodo que se añade a los ya heredados
    def picar(self):
        print(f"{self.especie} usa PICADURA!")
        pygame.mixer.init()
        pygame.mixer.music.load("/home/kali/Desktop/Boludeces varias/SonidoBeedrill.wav")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            continue
        

# Con tan solo un par de lineas de codigo, hemos creado una clase nueva que tiene todo el contenido que la clase padre tiene, tambien, creamos varios animales concretos y sobreescribimos algunos de los metodos que habian sido definidos en la clase "Animal", como el "hablar" o el "moverse", ya que cada animal se comporta de una manera distinta

# A partir de esto, ya podemos crear nuestros objetos de las clases ya definidas y hacer uso de sus metodos

#tuVieja = Vaca("mamifero", 40)
#tuVieja.describeme()
#tuVieja.hablar()
#tuVieja.moverse()

barry = Abeja("insecto", 5)
#barry.describeme()
#barry.picar()

# podemos clasificar los metodos creados en 3 tipos:
# - Heredados directamente de la clase padre ("describeme")
# - Heredados de la clase padre, pero modificados ("hablar, moverse")
# - Creados en la clase hija, por ende, no existen en la clase padre ("picar")

# --------------------------------------------------------------------------------

# METODO SUPER

# el metodo super() nos permite añadir un parametro extra en el constructor de la clase hija
# para añadir parametros al constructor tenemos dos formas
# - "Actualizar manualmente el constructor"
# class Perro2(Animal):
#     def __init__(self, especie, edad, dueño):
#         self.especie = especie
#         self.edad = edad
#         self.dueño = dueño

# - Utilizar el metodo super() para llamar al __init__ de la clase padre y asignar la variable nueva

class Perro3(Animal):
    def __init__(self, especie, edad, dueño):
        super().__init__(especie,edad)
        self.dueño = dueño

# ------------------------------------------------------------------------------------------------------------------------------

# Herencia multiple

# La herencia multiple es similar a la herencia simple, pero una clase hereda varias clases padre en vez de una sola

class Pokemon:
    def __init__(self, tipo, especie):
        self.tipo = tipo
        self.especie = especie

    def pokespawn(self):
        rng = random.randint(0,9)
        if rng <= 4 :
            print(f"Ve! {self.especie}!")
        else :
            print(f"{self.especie} yo te elijo!")
            

        pygame.mixer.init()
        pygame.mixer.music.load("/home/kali/Desktop/Boludeces varias/pokeballOpening2sec.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            continue


class Beedrill(Pokemon,Abeja):
    def __init__(self):
        super().__init__("Bicho", "Beedrill")


       

        
Stinger = Beedrill()
Stinger.pokespawn()
Stinger.picar()

























































































