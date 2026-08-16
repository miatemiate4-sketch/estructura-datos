# ================================================
# 🛒 CARRITO DE UCC
# ================================================

# Catálogo de productos (PRECIO POR UNIDAD)
precios = {
    "lapiz": 2.50,
    "cuaderno": 8.00,
    "boligrafo": 3.50,
    "calculadora": 45.00,
    "mochila": 65.00
}

# Carrito vacío (PRODUCTO -> CANTIDAD)
carrito = {}


def agregar(producto, cantidad):
    """Agrega X unidades de un producto"""
    if producto not in precios:
        print(f" '{producto}' no existe")
        return
    if cantidad <= 0:
        print(" La cantidad debe ser mayor a 0")
        return
    if producto in carrito:
        carrito[producto] += cantidad
    else:
        carrito[producto] = cantidad
    print(f" Agregado: {cantidad}x {producto}")


def sacar(producto, cantidad):
    """Quita X unidades de un producto"""
    if producto not in carrito:
        print(f" '{producto}' no está en el carrito")
        return
    if carrito[producto] < cantidad:
        print(f" Solo hay {carrito[producto]} disponibles")
        return
    carrito[producto] -= cantidad
    if carrito[producto] <= 0:
        del carrito[producto]
        print(f" Eliminado: {producto}")
    else:
        print(f" Sacado: {cantidad}x {producto}")


def ver_cantidades():
    """Muestra cuántas unidades de cada producto"""
    if not carrito:
        print(" Carrito vacío")
        return
    print("\n CANTIDADES:")
    for producto, cantidad in carrito.items():
        print(f"  • {producto}: {cantidad} unidad(es)")


def total():
    """Calcula el monto total a pagar"""
    if not carrito:
        print(" TOTAL: $0.00")
        return
    suma = 0
    for producto, cantidad in carrito.items():
        suma += precios[producto] * cantidad
    print(f" TOTAL: ${suma:.2f}")


def mostrar_catalogo():
    """Muestra todos los productos disponibles"""
    print("\n CATÁLOGO:")
    for producto, precio in precios.items():
        print(f"  • {producto}: ${precio:.2f}")


# ================================================
#  PROGRAMA PRINCIPAL
# ================================================
if __name__ == "__main__":
    print(" TIENDA UCC")
    print("=" * 35)

    while True:
        mostrar_catalogo()

        print("\n" + "=" * 35)
        print("1-Agregar  2-Sacar  3-Ver  4-Total  5-Salir")
        print("=" * 35)

        opcion = input("Opción: ")

        if opcion == "1":
            producto = input("Producto: ").lower().strip()
            try:
                cantidad = int(input("Cantidad: "))
                agregar(producto, cantidad)
            except ValueError:
                print(" Debes ingresar un número")

        elif opcion == "2":
            producto = input("Producto: ").lower().strip()
            try:
                cantidad = int(input("Cantidad: "))
                sacar(producto, cantidad)
            except ValueError:
                print(" Debes ingresar un número")

        elif opcion == "3":
            ver_cantidades()

        elif opcion == "4":
            total()

        elif opcion == "5":
            print("\n ¡Gracias por tu compra!")
            break

        else:
            print(" Opción no válida)