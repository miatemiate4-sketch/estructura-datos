CATALOGO = {
    "lapiz": 2.50,
    "cuaderno": 8.00,
    "boligrafo": 3.50,
    "calculadora": 45.00,
    "mochila": 65.00
}


class CarritoLista:
   
    
    def __init__(self):
        self._carrito = []
    
    def _buscar_indice(self, producto_norm):
        for i, (prod, _) in enumerate(self._carrito):
            if prod == producto_norm:
                return i
        return -1
    
    def agregar(self, producto, cantidad):
        if cantidad <= 0:
            return False
        prod_norm = producto.lower()
        if prod_norm not in CATALOGO:
            return False
        
        idx = self._buscar_indice(prod_norm)
        if idx != -1:
            self._carrito[idx][1] += cantidad
        else:
            self._carrito.append([prod_norm, cantidad])
        return True
    
    def sacar(self, producto, cantidad):
        if cantidad <= 0:
            return False
        prod_norm = producto.lower()
        
        idx = self._buscar_indice(prod_norm)
        if idx == -1 or self._carrito[idx][1] < cantidad:
            return False
        
        self._carrito[idx][1] -= cantidad
        if self._carrito[idx][1] == 0:
            self._carrito.pop(idx)
        return True
    
    def cantidad(self, producto):
        prod_norm = producto.lower()
        idx = self._buscar_indice(prod_norm)
        return self._carrito[idx][1] if idx != -1 else 0
    
    def existe(self, producto):
        prod_norm = producto.lower()
        return self._buscar_indice(prod_norm) != -1
    
    def tamaño(self):
        return sum(cant for _, cant in self._carrito)
    
    def total(self):
        return sum(cant * CATALOGO[prod] for prod, cant in self._carrito)