CATALOGO = {
    "lapiz": 2.50,
    "cuaderno": 8.00,
    "boligrafo": 3.50,
    "calculadora": 45.00,
    "mochila": 65.00
}

class CarritoList(list):
    """Lista personalizada que soporta acceso por clave como diccionario."""
    
    def __getitem__(self, key):
        if isinstance(key, str):
            prod_norm = key.lower()
            for item in self:
                if item[0] == prod_norm:
                    return item[1]
            raise KeyError(f"{key} no está en el carrito")
        return super().__getitem__(key)
    
    def __setitem__(self, key, value):
        if isinstance(key, str):
            prod_norm = key.lower()
            for i, item in enumerate(self):
                if item[0] == prod_norm:
                    self[i][1] = value
                    return
            self.append([prod_norm, value])
        else:
            super().__setitem__(key, value)
    
    def __contains__(self, key):
        if isinstance(key, str):
            prod_norm = key.lower()
            return any(item[0] == prod_norm for item in self)
        return super().__contains__(key)
    
    def __len__(self):
        return super().__len__()

def crear_carrito():
    return CarritoList()

def _buscar_indice(carrito, producto_norm):
    for i, (p, _) in enumerate(carrito):
        if p == producto_norm:
            return i
    return -1

def agregar(carrito, producto, cantidad):
    if cantidad <= 0:
        return False
    prod_norm = producto.lower()
    if prod_norm not in CATALOGO:
        return False
    
    idx = _buscar_indice(carrito, prod_norm)
    if idx != -1:
        carrito[idx][1] += cantidad
    else:
        carrito.append([prod_norm, cantidad])
    return True

def sacar(carrito, producto, cantidad):
    if cantidad <= 0:
        return False
    prod_norm = producto.lower()
    
    idx = _buscar_indice(carrito, prod_norm)
    if idx == -1 or carrito[idx][1] < cantidad:
        return False
    
    carrito[idx][1] -= cantidad
    if carrito[idx][1] == 0:
        carrito.pop(idx)
    return True

def ver_cantidades(carrito):
    return [tuple(item) for item in carrito]

def total(carrito):
    return sum(cant * CATALOGO[prod] for prod, cant in carrito)