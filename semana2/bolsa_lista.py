# Código base — Semana 02
# Fuente: 01-Momento-1-Contrato-y-secuencia/02-Semana-02-ADT-y-Spec-Driven-Development/02-guia-de-laboratorio.html
# bolsa_lista.py

class ElementoNoEncontradoError(Exception):
    """Excepción lanzada cuando se intenta sacar un elemento inexistente."""
    pass

class BolsaLista:
    #Las búsquedas son O(n) porque recorre línea por línea
    def __init__(self):
        self._bolsa = []
    
    def _buscar_indice(self, elemento):
        for i, (elem, _) in enumerate(self._bolsa):
            if elem == elemento:
                return i # Encontrado → devuelve posición
        return -1 #no encontro
    
    def agregar(self, elemento): # Busca si ya existe (O(n))
        idx = self._buscar_indice(elemento)#idx=Índice (posición numérica en la lista
        if idx != -1:
            self._bolsa[idx][1] += 1
        else:
            self._bolsa.append([elemento, 1])
    
    def cuantos(self, elemento):
        idx = self._buscar_indice(elemento)
        return self._bolsa[idx][1] if idx != -1 else 0  # ← CON RETURN
    
    def contiene(self, elemento):
        return self._buscar_indice(elemento) != -1  # ← CON RETURN
    
    def sacar(self, elemento):
        #Complejidad: O(n) por búsqueda + O(n) por pop en medio de lista
        idx = self._buscar_indice(elemento)
        if idx == -1 or self._bolsa[idx][1] == 0:
            raise ElementoNoEncontradoError(f"El elemento '{elemento}' no está en la bolsa")
        
        self._bolsa[idx][1] -= 1
        if self._bolsa[idx][1] == 0:
            self._bolsa.pop(idx)#  Elimina el par completo
    
    def tamaño(self):#Devuelve el total de elementos 
        return sum(cant for _, cant in self._bolsa)  # ← CON RETURN