#from Graph import Graph, Vertex
#import queue as Q
from pythonds.graphs import PriorityQueue, Graph, Vertex

def dijkstra(aGraph,start):
    pq = PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(),v) for v in aGraph])
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() \
                    + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance( newDist )
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert,newDist)
        print(currentVert)
    # for g in aGraph:
    #     print(g)

g = Graph()
g.addEdge('V0','V1',5)
g.addEdge('V0','V5',2)
g.addEdge('V1','V2',4)
g.addEdge('V2','V3',9)
g.addEdge('V3','V4',7)
g.addEdge('V3','V5',3)
g.addEdge('V4','V0',1)
g.addEdge('V5','V2',1)
g.addEdge('V5','V4',8)

dijkstra(g,g.getVertex('V0'))
