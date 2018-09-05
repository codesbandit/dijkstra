graph = {'a':{'e':6,'d':8},
         'b':{'c':4,'d':3},
         'c':{'b':4,'d':4,'e':2},
         'd':{'b':3,'c':4},
         'e':{'c':2,'a':6}}
 
def dijkstra(graph,start,goal):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = 9999999
    path = []
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0
 
    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node
 
        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)
 
    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Jalur tidak ditemukan')
            break
    path.insert(0,start)
    if shortest_distance[goal] != infinity:
        print('Jarak jalur = ' + str(shortest_distance[goal]) + "KM")
        print('Jalur yang dituju ' + str(path))
 
startw = raw_input("Masukan start = ")
finish = raw_input("Masukan Tujuan = ")

dijkstra(graph, startw, finish)
