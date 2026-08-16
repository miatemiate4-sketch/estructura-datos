class BolsaDict:
    """Bolsa implementada como diccionario de conteos."""
    
    def __init__(self):
        self._conteos = {}
        self._total = 0
    
    def agregar(self, elemento):
        self._conteos[elemento] = self._conteos.get(elemento, 0) + 1
        self._total += 1
    
    def sacar(self, elemento):
        if elemento in self._conteos:
            self._conteos[elemento] -= 1
            self._total -= 1
            if self._conteos[elemento] == 0:
                del self._conteos[elemento]
    
    def cuantos(self, elemento):
        return self._conteos.get(elemento, 0)
    
    def tamaño(self):
        return self._total
    
    def contiene(self, elemento):
        return elemento in self._conteos


# Precios de la tienda universitaria
PRECIO_PRODUCTOS = {
    "cuaderno": 3.50,
    "lapiz": 0.50,
    "goma": 0.75,
    "pluma": 1.20,
    "estuche": 12.00,
    "calculadora": 25.00,
    "mochila": 45.00,
    "boligrafo": 1.00,
    "regla": 1.50,
    "libreta": 2.80
}


class CarritoTienda:
    def __init__(self):
        self.bolsa = BolsaDict()
        self.precios = PRECIO_PRODUCTOS
    
    def agregar(self, producto, cantidad=1):
        """Agrega productos al carrito."""
        for _ in range(cantidad):
            self.bolsa.agregar(producto)
    
    def quitar(self, producto, cantidad=1):
        """Quita productos del carrito."""
        for _ in range(cantidad):
            self.bolsa.sacar(producto)
    
    def total(self):
        """Calcula el total a pagar."""
        return sum(
            self.bolsa.cuantos(p) * self.precios.get(p, 0) 
            for p in self.bolsa._conteos
        )
    
    def mostrar(self):
        """Muestra el estado del carrito."""
        if self.bolsa.tamaño() == 0:
            print("\n🛒 Carrito vacío")
            return
        
        print("\n🎓 CARRITO TIENDA UNIVERSITARIA")
        print("=" * 45)
        
        for producto in self.bolsa._conteos:
            cantidad = self.bolsa.cuantos(producto)
            precio = self.precios.get(producto, 0)
            subtotal = cantidad * precio
            print(f"{producto:<20} x{cantidad:>2}  ${precio:>6.2f}  ${subtotal:>6.2f}")
        
        print("=" * 45)
        print(f"TOTAL UNIDADES: {self.bolsa.tamaño():>28}")
        print(f"TOTAL A PAGAR:  ${self.total():>27.2f}")


def menu():
    """Menú interactivo para gestionar el carrito."""
    carrito = CarritoTienda()
    
    while True:
        print("\n" + "=" * 45)
        print("  🛒 MENÚ TIENDA UNIVERSITARIA")
        print("=" * 45)
        print("1. Ver carrito")
        print("2. Agregar producto")
        print("3. Quitar producto")
        print("4. Ver lista de productos")
        print("5. Pagar y finalizar")
        print("6. Salir")
        print("-" * 45)
        
        opcion = input("Selecciona opción (1-6): ").strip()
        
        if opcion == "1":
            carrito.mostrar()
        
        elif opcion == "2":
            producto = input("Producto: ").strip().lower()
            if producto in PRECIO_PRODUCTOS:
                cantidad = int(input("Cantidad: "))
                carrito.agregar(producto, cantidad)
                print(f"✅ Agregado {cantidad} x {producto}")
            else:
                print("❌ Producto no disponible")
        
        elif opcion == "3":
            producto = input("Producto a quitar: ").strip().lower()
            if carrito.bolsa.contiene(producto):
                cantidad = int(input("Cantidad a quitar: "))
                carrito.quitar(producto, cantidad)
                print(f"✅ Quitado {cantidad} x {producto}")
            else:
                print("❌ Producto no está en el carrito")
        
        elif opcion == "4":
            print("\n📋 PRODUCTOS DISPONIBLES:")
            print("-" * 40)
            for prod, precio in PRECIO_PRODUCTOS.items():
                print(f"  {prod:<20}  ${precio:.2f}")
        
        elif opcion == "5":
            if carrito.bolsa.tamaño() == 0:
                print("❌ Carrito vacío, nada que pagar")
            else:
                carrito.mostrar()
                confirmacion = input("Confirmar pago? (s/n): ")
                if confirmacion.lower() == "s":
                    print(f"\n💳 ¡Pago realizado! Total: ${carrito.total():.2f}")
                    break
        
        elif opcion == "6":
            print("👋 ¡Gracias por visitar la tienda!")
            break
        
        else:
            print("❌ Opción inválida")


# Ejecutar el programa
if __name__ == "__main__":
    menu()