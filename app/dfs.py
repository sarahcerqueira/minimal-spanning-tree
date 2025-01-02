from app.graph import *

class DepthFirstSearch :
    @staticmethod
    def dfs(graph: Graph, wantedVertex)->list:
        vertexVisited = set()
        path = []
        DepthFirstSearch.__dfsRec(graph, wantedVertex, vertexVisited, path)
        return path

    @staticmethod
    def __dfsRec(graph, wantedVertex, vertexVisited, path):
        vertexVisited.add(wantedVertex)
        adjacents = graph.adjacents(wantedVertex)

        for u in adjacents:
            if u not in vertexVisited:
                path.append(u)
                DepthFirstSearch.__dfsRec(graph, u, vertexVisited, path)