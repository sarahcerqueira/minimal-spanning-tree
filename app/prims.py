from app.graph import *
import math

class Prims:
    
    def minimalSpanningTree(self, graph: Graph) -> Graph:
        minimalTree = Graph()

        smaller = self.__getSmallerEdge(graph)
        v = smaller['v']
        u = smaller['u']
        minimalTree.addVertex(v)
        minimalTree.addVertex(u)
        minimalTree.addEdge(v, u, smaller['dist'])

        edgesPrim = minimalTree.edges()
        vextexSize = len(graph.vertices()) - 1

        while len(edgesPrim) / 2 < vextexSize:
            smaller = self.__getSmallerEdges(minimalTree, graph)
            minimalTree.addVertex(smaller['u'])
            minimalTree.addEdge(smaller['v'], smaller['u'], smaller['dist'])
            edgesPrim = minimalTree.edges()

        return minimalTree


    def __getSmallerEdge(self, graph: Graph)->dict:
        edgesG = graph.edges()
        menorDist = math.inf
        menorAresta = ()

        for edge in edgesG:

            v = edge[0]
            u = edge[1]
            dist = graph.getEdge(v, u)

            if menorDist > dist:
                menorDist = dist
                menorAresta = edge

        return {'v': menorAresta[0], 'u': menorAresta[1], 'dist': menorDist}


    def __getSmallerEdges(self, minimalTree: Graph, graph: Graph)->dict:
        edgesG = graph.edges()
        menorDist = math.inf
        menorAresta = ()

        vextex = minimalTree.vertices()
        edgesPrim = minimalTree.edges()

        for vu in edgesG:

            v = vu[0]
            u = vu[1]
            dist = graph.getEdge(v, u)

            if v in vextex and u not in vextex and menorDist > dist and vu not in edgesPrim:
                menorDist = dist
                menorAresta = vu

        return {'v': menorAresta[0], 'u': menorAresta[1], 'dist': menorDist}