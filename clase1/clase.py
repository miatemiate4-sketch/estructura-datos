edad = 25
nombre = "juan"
altura = 1.75
activo = True


def verificar_edad(edad, activo):
# and or not
# >< >= <= == !=
 if edad >= 18 and activo:
    print(f" (nombre) es mayor de edad y esta activo")
 else:
    print(f"(nombre) no cumple con los requisitos. ")

def verificar_altura(altura):
    if altura >= 1.8:
        return "eres alto"
    elif altura >= 1.6:
        return "tienes una altura promedia"
    else:
        return "eres bajito"
    

 