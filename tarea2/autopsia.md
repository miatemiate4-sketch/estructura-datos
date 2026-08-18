Las dos bolsas no comparten el mismo carrito interno. Cada una tiene su propio almacenamiento en memoria completamente separado .

┌────────────────────────────────────────────────────────────────────────────────────────────┐
│                                    MEMORIA RAM                                             │
│                                                                                             │
│   ┌──────────────────────────────────────────┐     ┌─────────────────────────────────────┐ │
│   │         OBJETO 1: BolsaLista             │     │        OBJETO 2: BolsaDict          │ │
│   │         id(c1) = 0x7FFF001               │     │        id(c2) = 0x7FFF002           │ │
│   └──────────────────────────────────────────┘     └─────────────────────────────────────┘ │
│                     │                                               │                       │
│                     ▼                                               ▼                       │
│   ┌──────────────────────────────────────────┐     ┌─────────────────────────────────────┐ │
│   │   self._bolsa (referencia)               │     │   self._bolsa (referencia)          │ │
│   │                        │     │                     │ │
│   └──────────────────────────────────────────┘     └─────────────────────────────────────┘ │
│                     │                                               │                       │
│                     ▼                                               ▼                       │
│   ┌──────────────────────────────────────────┐     ┌─────────────────────────────────────┐ │
│   │   ESTRUCTURA: LISTA []                   │     │   ESTRUCTURA: DICCIONARIO {}        │ │
│   │   ┌─────────────────────────────────┐    │     │   ┌───────────────────────────────┐ │ │
│   │   │  índice 0: ['manzana', 5]       │    │     │   │ 'manzana' → 5                 │ │ │
│   │   │  índice 1: ['pera', 3]          │    │     │   │ 'pera' → 3                    │ │ │
│   │   │  índice 2: ['naranja', 2]       │    │     │   │                               │ │ │
│   │   └─────────────────────────────────┘    │     │   └───────────────────────────────┘ │ │
│   └──────────────────────────────────────────┘     └─────────────────────────────────────┘ │
│                                                                                             │
│   ═══════════════════════════════════════════════════════════════════════════════════════   │
│ 
│   ═══════════════════════════════════════════════════════════════════════════════════════   │
│                                                                                             │
│   OPERACIÓN: c1.agregar('uvas', 4)                                                          │
│                                                                                             │
│   ┌──────────────────────────────────────────┐     ┌─────────────────────────────────────┐ │
│   │   c1 (BolsaLista)                        │     │   c2 (BolsaDict)                    │ │
│   │   self._bolsa = [                        │     │   self._bolsa = {                   │ │
│   │       ['manzana', 5],                    │     │       'manzana': 5,                 │ │
│   │       ['pera', 3],                       │     │       'pera': 3                     │ │
│   │       ['naranja', 2],                    │     │   }                                 │ │
│   │       ['uvas', 4]  nuevo             │     │                                     │ │
│   │   ]                                      │     │   tamaño = 8                        │ │
│   │   tamaño = 14                            │     │                                     │ │
│   └──────────────────────────────────────────┘     └─────────────────────────────────────┘ │
│                                                                                             │
│   ═══════════════════════════════════════════════════════════════════════════════════════   │
│   c2 no ve los cambios de c1 → sigue sin tener 'uvas'                                    │
│   ═══════════════════════════════════════════════════════════════════════════════════════   │
│                                                                                             │
└────────────────────────────────────────────────────────────────────────────────────────────┘

Lo que comparten es el diseño exterior, no los datos interiores. Las dos cajas tienen los mismos métodos con los mismos nombres: agregar, sacar, cuantos, tamaño y contiene. Ambas siguen las mismas reglas


# bolsa_dist
antes (con _total)    
   O(1) acceso  
┌─────────────────────────────────────────────────────────┐
│                  OBJETO BOLSA DICT                      │
│  ─────────────────────────────────────────────────────  │
│  self                                                    │
│   │                                                      │
│   ├── _total ───────────────────→ 3  ← ¡Acceso directo! │
│   │               (variable simple, O(1))               │
│   │                                                     │
│   └── _bolsa (diccionario)                              │
│       │                                                 │
│       ├── "manzana" ──→ 2                               │
│       └── "pera" ─────→ 1                               │
│                                                           │
│  Cuando llamas: b.tamaño()                              │
│  ↓                                                      │
│  return self._total                                     │
│  ↓                                                      │
│  3 ← ¡Listo en 1 paso! (O(1))                          │
└─────────────────────────────────────────────────────────┘
despues (sin _total)    
  O(n) recorrido 
┌─────────────────────────────────────────────────────────┐
│                  OBJETO BOLSA DICT                      │
│  ─────────────────────────────────────────────────────  │
│  self                                                    │
│   │                                                      │
│   └── _bolsa (diccionario)                              │
│       │                                                 │
│       ├── "manzana" ──→ 2  ←─────┐                     │
│       │                         │                     │
│       └── "pera" ─────→ 1  ←────┤                     │
│                                 │                     │
│  Cuando llamas: b.tamaño()      ▼                     │
│  ↓                                         ┌─────────┐
│  return sum(self._bolsa.values())          │ Sumador │
│  ↓                                         │  = 0    │
│  ────────────────────────────────→         └────┬────┘
│                                                 │
│  Iteración 1: leer "manzana" = 2               │
│                   sumar al acumulador → 2       │
│                                                 │
│  Iteración 2: leer "pera" = 1                  │
│                   sumar al acumulador → 3       │
│                                                 │
│  Finalmente devolver 3                          │
│  ↓                                              │
│  Tiempo: depende del n° de claves (O(n)) ✗     │
└─────────────────────────────────────────────────┘
# bolsa_list
 antes
 ┌─────────────────────────────────────────────────────────┐
│                  OBJETO BOLSA LISTA                     │
│  ─────────────────────────────────────────────────────  │
│  self                                                    │
│   │                                                      │
│   └── _elementos = []  ← Lista vacía                   │
│                                                          │
│  Documentación decía: tamaño() -> O(1)                  │
│  Pero la implementación era: pass                       │
│                                                          │
│  No se podía verificar porque estaba vacío              │
└─────────────────────────────────────────────────────────┘    
despues
┌─────────────────────────────────────────────────────────┐
│                  OBJETO BOLSA LISTA                     │
│  ─────────────────────────────────────────────────────  │
│  self                                                   │
│   │                                                     │
│   └── _bolsa (lista de listas [elemento, cuenta])       │
│       │                                                 │
│       ├── [0] → ["manzana", 2]  ←─────┐                 │
│       │                             │                   │
│       └── [1] → ["pera", 1]     ←────┤                  │
│                                       │                 │
│  Cuando llamas: b.tamaño()            ▼                 │
│  ↓                                            ┌─────────┐
│  return sum(cant for _, cant in self._bolsa)  │ Sumador │
│  ↓                                            │  = 0    │
│  ────────────────────────────────→            └────┬────┘
│                                                    │
│  Iteración 1: leer ["manzana", 2]                  │
│              extraer 2, sumar → 2                       │
│                                                         │
│  Iteración 2: leer ["pera", 1]                          │
│              extraer 1, sumar → 3                       │
│                                                         │
│  Finalmente devolver 3                                  │
│  ↓                                                      │
│  Pasos: 2 (número de claves distintas)                  │
│  Complejidad: O(n) ✗ (ROMPE la promesa)                 │
└─────────────────────────────────────────────────────────┘
# por que sirve
Antes no funcionaban porque los métodos estaban vacíos. Todos ellos tenían solo la palabra pass, Ahora funcionan porque se implementó la lógica completa dentro de cada método. Cada función tiene código que realmente accede a la estructura interna de datos, modifica su estado cuando es necesario y devuelve valores concretos en lugar de failed. El atributo interno llamado bolsa se llena con la información de los elementos y sus conteos, y todos los métodos saben cómo consultar y actualizar esa información correctamente
