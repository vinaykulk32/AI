# Normal BFS algorithm using python with queue




#Function for BFS
def bfs(visited, graph, node):
# marking the first node as visited and appending it the queue
visited.append(node)
queue.append(node)

#initializing a list to store the order of exploration of the graph
answer=[]

# while there are nodes in the graph which are to be explored
# we need to run this loop
while queue:
# pop the node from the queue for exploring
# we push it to the answer list
n=queue.pop(0)
answer.append(n)

# exploring the neighbours
for neighbour in graph[n]:

# if the neighbour id not visited
# we visit them and put them in the queue
if neighbour not in visited:
visited.append(neighbour)
queue.append(neighbour)

# ptinting the order of exploration of the graph
for key in answer:
print(key)


# defining the grap as its adjacence matrix
graph={
'1':['2','3','4'],
'2':['1','5','6'],
'3':['1'],
'4':['1','7','8'],
'5':['2','9','10'],
'6':['2'],
'7':['4','11','12'],
'8':['4'],
'9':['5'],
'10':['5'],
'11':['7'],
'12':['7'],
}


#initializing empty Queue and Visited
visited=[]
queue=[]

# doing the BFS on this graph
bfs(visited,graph,'1')
