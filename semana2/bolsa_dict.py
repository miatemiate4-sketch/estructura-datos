# Código base — Semana 02
# Fuente: 01-Momento-1-Contrato-y-secuencia/02-Semana-02-ADT-y-Spec-Driven-Development/02-guia-de-laboratorio.html


class ElementoNoEncontradoError(Exception):
    """Excepción lanzada cuando se intenta sacar un elemento inexistente."""
    pass

class BolsaDict:
    """
    TAD Bolsa implementado con diccionario interno.
    """
    
    def __init__(self):
        self._bolsa = {}
    
    def agregar(self, elemento):
        """Agrega un elemento a la bolsa."""
        self._bolsa[elemento] = self._bolsa.get(elemento, 0) + 1
    
    def cuantos(self, elemento):
        """Devuelve la cantidad de veces que aparece un elemento."""
        return self._bolsa.get(elemento, 0)
    
    def contiene(self, elemento):
        """Devuelve True si el elemento está en la bolsa."""
        return elemento in self._bolsa
    
    def sacar(self, elemento):
        """
        Remueve una instancia del elemento.
        Lanza ElementoNoEncontradoError si no existe.
        """
        if elemento not in self._bolsa or self._bolsa[elemento] == 0:
            raise ElementoNoEncontradoError(f"El elemento '{elemento}' no está en la bolsa")
        
        self._bolsa[elemento] -= 1
        if self._bolsa[elemento] == 0:
            del self._bolsa[elemento]
    
    def tamaño(self):
        """Devuelve el total de elementos en la bolsa."""
        return sum(self._bolsa.values())