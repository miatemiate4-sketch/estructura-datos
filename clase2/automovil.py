# Define (crea) la clase llamada automovil.
class automovil:
    #Declara un atributo llamado marca y especifica que debería ser de tipo texto (str, string).
    marca: str
    color: str
    modelo: str
    #Declara un atributo llamado anio (año), esperando que sea un número entero (int, integer).
    anio: int

#Define el Constructor de la clase, conocido como __init__. Este método se ejecuta automáticamente solo una vez, justo cuando creas un objeto nuevo (ej: mi_coche = automovil("Toyota")).
    def __init__(self, marca: str):
        #Asigna el valor recibido en el parámetro marca al atributo self.marca del objeto creado
        self.marca = marca

    def set_color(self, color: str):
        self.color = color

    def set_modelo(self, modelo: str):
        self.modelo = modelo

    def set_anio(self, anio: int):
        self.anio = anio
#Define un método llamado revisar_estado.
    def revisar_estado(self)-> bool:
        #codigo..
        #Finaliza la ejecución del método y devuelve el valor True como resultado.
        return True            
#Crea un nuevo objeto de tipo automovil y lo almacena en una variable llamada auto1.
auto1 = automovil('Mazda')
auto2 = automovil('Toyota')
auto3 = automovil('Mazda')
"""if auto1 == auto3:
     print("son iguales")
else:
     print("no son iguales")
"""
print("objeto 1: ", auto1)
print("objeto 2: ", auto2)
print("objeto 3: ", auto3)

