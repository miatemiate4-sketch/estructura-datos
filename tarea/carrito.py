
CATALOGO = {
    "lapiz": 2.50,
    "cuaderno": 8.00,
    "boligrafo": 3.50,
    "calculadora": 45.00,
    "mochila": 65.00
}

def crear_carrito():
    return {}

def agregar(carrito, producto, cantidad):
    if producto not in CATALOGO or cantidad <= 0:
        return False
    carrito[producto] = carrito.get(producto, 0) + cantidad
    return True

def sacar(carrito, producto, cantidad):
    if producto not in carrito or carrito[producto] < cantidad:
        return False
    carrito[producto] -= cantidad
    if carrito[producto] <= 0:
        del carrito[producto]
    return True

def ver_cantidades(carrito):
    return list(carrito.items())

def total(carrito):
    return sum(qty * CATALOGO[p] for p, qty in carrito.items())