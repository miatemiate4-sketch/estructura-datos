CATALOGO = {
    "lapiz": 2.50,
    "cuaderno": 8.00,
    "boligrafo": 3.50,
    "calculadora": 45.00,
    "mochila": 65.00
}

class CarritoDist:
    
    def __init__(self):
        self._carrito = {}
    
    def agregar(self, producto, cantidad):
        if cantidad <= 0:
            return False
        prod_norm = producto.lower()
        if prod_norm not in CATALOGO:
            return False
        
        self._carrito[prod_norm] = self._carrito.get(prod_norm, 0) + cantidad
        return True
    
    def sacar(self, producto, cantidad):
        if cantidad <= 0:
            return False
        prod_norm = producto.lower()
        
        if prod_norm not in self._carrito or self._carrito[prod_norm] < cantidad:
            return False
        
        self._carrito[prod_norm] -= cantidad
        if self._carrito[prod_norm] == 0:
            del self._carrito[prod_norm]
        return True
    
    def cantidad(self, producto):
        prod_norm = producto.lower()
        return self._carrito.get(prod_norm, 0)
    
    def existe(self, producto):
        prod_norm = producto.lower()
        return prod_norm in self._carrito
    
    def tamaño(self):
        return sum(self._carrito.values())
    
    def total(self):
        return sum(cant * CATALOGO[prod] for prod, cant in self._carrito.items())

