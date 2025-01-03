from app.minimalSpanningTreeAlgorithmTemplate import *
from app.graph import *
from app.dfs import *
import math

class KrusKal(MinimalSpanningTreeAlgorithmTemplate):

    def minimalSpanningTree(self, graph: Graph) -> Graph:
        minimalTree = Graph()

        edgesKruskal = minimalTree.edges()
        vextexSize = len(graph.vertices()) - 1

        while len(edgesKruskal) / 2 < vextexSize:
            smaller = self.__getSmallerEdgesKruskal(minimalTree, graph)
            self.__addVetex(minimalTree, smaller['u'], smaller['v'])
            minimalTree.addEdge(smaller['v'], smaller['u'], smaller['dist'])
            edgesKruskal = minimalTree.edges()

        return minimalTree


    def __getSmallerEdgesKruskal(self, minimalTree, graph):
        edgesG = graph.edges()
        vextex = minimalTree.vertices()
        edgeskruskal = minimalTree.edges()
        shortestDistance = math.inf
        smallestEdge = ()

        for vu in edgesG:

            v = vu[0]
            u = vu[1]
            dist = graph.getEdge(v, u)

            if shortestDistance > dist and vu not in edgeskruskal:
                if v in vextex and u in vextex:
                    pathList = DepthFirstSearch.dfs(minimalTree, v)

                    if u not in pathList:
                        shortestDistance = dist
                        smallestEdge = vu
                else:
                    shortestDistance = dist
                    smallestEdge = vu

        return {'v': smallestEdge[0], 'u': smallestEdge[1], 'dist': shortestDistance}


    def __addVetex(self, graph, u, v):
        vertex = graph.vertices()

        if u not in vertex:
            graph.addVertex(u)

        if v not in vertex:
            graph.addVertex(v)