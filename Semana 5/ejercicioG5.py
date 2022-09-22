graph = {
    'a': ['b', 'c', 'e'],
    'b': ['d', 'f'],
    'c': ['g'],
    'e': ['f'],
    'f': ['e'],
}


def IDS(raiz, objetivo):
    profundidad = 0
    while True:
        result = DLS(raiz, objetivo, profundidad)
        if result == objetivo:
            return result
        profundidad = profundidad + 1


def DLS(nodo, objetivo, profundidad):

    if profundidad == 0 and nodo == objetivo:
        return nodo
    elif profundidad > 0:
        for hijo in graph.get(nodo, []):
            if objetivo == DLS(hijo, objetivo, profundidad-1):
                return objetivo


print(IDS('a', 'c'))