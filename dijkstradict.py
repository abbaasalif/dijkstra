#dijikstra with dict
import sys


            
    
def dijikstra(graph, source):
    distances = {}#to store the distances of nodes from source
    visited=[] # to store visited nodes
    parents = [-1] * len(graph[0])# to store parents of the nodes
    for i in range(len(graph[0])): # initializing distances dictonary -> for source node distance 0 rest nodes infinity simulated using sys
        if i==source:
            distances[i]=0
        else:
            distances[i]=sys.maxsize
    #create a priority queue enumerate returns the index too.
    pq = []
    nodes = list(distances.keys()) #we take out the keys and create a nodes array from distances dictionary
    weights = list(distances.values()) # we take out the values and create a weights array from distances dictionary
    for i in range(len(weights)): # insert generic bubble sort here. What we do is while sorting the weights we sort the respective nodes too which will create the Priority queue
        for j in range(0,len(weights)-i-1):
            if weights[j]>weights[j+1]:
                temp = weights[j]
                temp1 = nodes[j]
                weights[j] = weights[j+1]
                nodes[j] = nodes[j+1]
                weights[j+1]=temp
                nodes[j+1] = temp1
    pq = nodes # I just wasted a variable but the code is much readabe now . Phew! nevermind.
    while pq: # till the priority queue is not empty
        node = pq.pop(0) # pop the first node -> the one with the least priority
        visited.append(node) # add that node to the visited list as we will not consider this node from the next interation of priority queue
        for i in range(len(graph[node])): # for the graph in the index of the node
            if graph[node][i] != 0: # when it is zero it means its not connected
                if distances[i] > distances[node]+graph[node][i]: #we check whether travelling to another node is chepaer than what the weights have been intialized or changed from.
                    distances[i] = distances[node]+graph[node][i] # if yes we replace the distances dictionary and also update the parent for that node.
                    parents[i] = node
        pq=[] # recreating PQ after the changes made in distances dictionary
        nodes = list(distances.keys())
        weights = list(distances.values())
        for i in range(len(weights)):
            for j in range(0,len(weights)-i-1):
                if weights[j]>weights[j+1]:
                    temp = weights[j]
                    temp1 = nodes[j]
                    weights[j] = weights[j+1]
                    nodes[j] = nodes[j+1]
                    weights[j+1]=temp
                    nodes[j+1] = temp1
        pq = nodes
        for i in visited: # here we remove the nodes from the priority queue that are already been visited.
            pq.remove(i)
    return distances, parents #then we return the distances from source node and the parents of that node -> Note parents means the previous node.

                



        

            



if __name__ == '__main__':
    graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]
    distances, parents = dijikstra(graph, 0)
    print(distances)
    print(parents)
               

