'''
Created on Apr 27, 2014
@author: tanmaymehrotra
'''

class Vertex:
    def __init__(self,vid,isVisited):
        self.isVisited = isVisited
        self.vid = vid
        
    def __eq__(self,other):
        return self.vid == other.vid
    
    def __hash__(self):
        return hash(self.vid)
        

graph = {
          Vertex(1,False) :[ Vertex(2,False), Vertex(3,False) ],
          Vertex(2,False) :[ Vertex(4,False), Vertex(5,False) ],
          Vertex(3,False) :[ Vertex(4,False), Vertex(6,False), Vertex(7,False) ]
         }