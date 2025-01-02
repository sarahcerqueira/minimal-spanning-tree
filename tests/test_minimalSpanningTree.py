import unittest
from app.graph import *
from app.prims import Prims
from app.kruskals import KrusKal

class TestMinimalSpanningTree(unittest.TestCase):

    def test_prims(self):
        prims = Prims()
        edgesMinimalSpanngTree = prims.minimalSpanningTree(self.getTree()).edges()
        expectedEdgesMinimalSpanngTree = [('a', 'd'), ('a', 'b'), ('d', 'a'), ('d', 'f'), ('f', 'd'), ('b', 'a'), ('b', 'e'), ('e', 'b'), ('e', 'c'),
         ('e', 'g'), ('c', 'e'), ('g', 'e')]
        self.assertListEqual(edgesMinimalSpanngTree, expectedEdgesMinimalSpanngTree)

    def test_kruskal(self):
        krusKal = KrusKal()
        edgesMinimalSpanngTree = krusKal.minimalSpanningTree(self.getTree()).edges()
        expectedEdgesMinimalSpanngTree = [('d', 'a'), ('d', 'f'), ('a', 'd'), ('a', 'b'), ('e', 'c'), ('e', 'b'), ('e', 'g'), ('c', 'e'), ('f', 'd'), ('b', 'a'), ('b', 'e'), ('g', 'e')]
        self.assertListEqual(edgesMinimalSpanngTree, expectedEdgesMinimalSpanngTree)

    def getTree(self)->Graph:
        g = Graph()
        g.addVertex("a")
        g.addVertex("b")
        g.addVertex("c")
        g.addVertex("d")
        g.addVertex("e")
        g.addVertex("f")
        g.addVertex("g")
        g.addEdge("a", "b", 7)
        g.addEdge("a", "d", 5)
        g.addEdge("b", "c", 8)
        g.addEdge("b", "d", 9)
        g.addEdge("b", "e", 7)
        g.addEdge("c", "e", 5)
        g.addEdge("d", "e", 15)
        g.addEdge("d", "f", 6)
        g.addEdge("e", "g", 9)
        g.addEdge("e", "f", 8)
        g.addEdge("f", "g", 11)

        return g
