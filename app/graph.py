from heapq import heappush, heappop
''' Este código foi fornecido pelo professor da disciplina Análise e Projeto de Algoritmos, do Programa de 
pós-graduação em Ciência da Computação da Universidade de Feira de Santana, no semestre 2022.2.
'''

class Graph:
    def __init__(self):
        self.vertexMap = dict()

    def addVertex(self, v):
        self.vertexMap[v] = dict()

    def removeVertex(self, v):
        if v in self.vertexMap:
            for (i, j) in self.vertexMap[v].copy():
                print(f"e->{(i, j)}")
                self.removeEdge(i, j)
            del self.vertexMap[v]

    def vertices(self):
        return list(self.vertexMap.keys())

    def adjacents(self, v):
        return [j for (i, j) in self.outgoing(v)]

    def addEdge(self, u, v, data):
        if (u in self.vertexMap) and (v in self.vertexMap):
            self.vertexMap[u][(u, v)] = data
            self.vertexMap[v][(v, u)] = data
        else:
            raise ValueError(f"One or both of the V {u} and {v} are not present in the Graph!")

    def removeEdge(self, u, v):
        if ((u, v) in self.vertexMap[u]) and ((v, u) in self.vertexMap[v]):
            del self.vertexMap[u][(u, v)]
            del self.vertexMap[v][(v, u)]

    def edges(self):
        ret = []
        for e in self.vertexMap.values():
            if len(e.keys()):
                ret.extend(list(e.keys()))
        return ret

    def getEdge(self, u, v):
        return self.vertexMap[u][(u, v)]

    # Arestas que sai de V
    def outgoing(self, v):
        return list(self.vertexMap[v].keys())

    # Quantidade de arestas que saem
    def outdegree(self, v):
        return len(self.vertexMap[v])

    # Vertices que chega
    def incoming(self, v):
        return [(j, i) for (i, j) in self.vertexMap[v]]

    # Quantidade
    def indegree(self, v):
        return len(self.vertexMap[v])

    def path(self, v):
        ret = ""
        visited = set()
        visited.add(v)
        stack = []
        stack.append((v, None))
        while stack:
            (v, p) = stack.pop()
            if p:
                ret += f"{p}--{self.getEdge(p, v)}--{v}  "

            for u in self.adjacents(v):
                if u not in visited:
                    visited.add(u)
                    stack.append((u, v))

        return ret.strip()