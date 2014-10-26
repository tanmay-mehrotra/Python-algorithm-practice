'''
Created on Sep 2, 2014
@author: tanmaymehrotra
'''

import Queue

class Node:
    'node of a graph'
    def __init__(self,value,isVisited=False):
        self.value = value
        self.isVisited = isVisited
        
    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return self.value == other.value

n1 = Node(1);n2 = Node(2);n3 = Node(3);
n4 = Node(4);n5 = Node(5);n6 = Node(6);

graph = {
         n1 : [n2, n4],
         n2 : [n3],
         n3 : [n4],
         n4 : [n5, n6],
         n5 : [n2]
    }

def BFS(start):
    q = Queue.Queue();
    q.put(start)
    while not q.empty():
        node = q.get()
        if not node.isVisited:
            print node.value
            node.isVisited = True
            neighbours = graph.get(node)
            if neighbours is None:
                continue
            else:
                for neighbour in graph.get(node):
                    q.put(neighbour)
                    

def DFS(start):
    print start.value
    if not graph.has_key(start) :
        return
    start.isVisited = True
    for neighbour in graph.get(start):
        if neighbour is not None and neighbour.isVisited is False:
            DFS(neighbour)
    
        
if __name__ == '__main__':
    print "BFS"
    #BFS(n1)
    print "DFS"
    DFS(n1)
    