'''
Created on Apr 17, 2014
@author: tanmaymehrotra
'''
import FirstPackage.Graph as Graph

def DFS(graph,startingVertex):
    if graph.has_key(startingVertex):
        startingVertex.isVisited = True
        graph.update({startingVertex:graph.get(startingVertex)})
        for vertex in graph[startingVertex]:
            if vertex.isVisited != True:
                print(vertex.vid)
                vertex.isVisited = True
                DFS(graph,vertex)
         

def printGraph(graph):
    for key in graph.keys():
        print(key.vid)
        print(key.isVisited)
        for value in graph[key]:
            print(value.vid)
            print(value.isVisited)
                        
if __name__ == "__main__":
    DFS(Graph.graph, Graph.Vertex(1,False))
    printGraph(Graph.graph)

