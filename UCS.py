# UCS algorithm using python with priorotyqueue



# Path Cost
def pat_cost(path):
	total_cost=0
	for (node,cost) in path:
		total_cost =cost
	return total_cost, path[-1][0]




#Function for BFS
def ucs(graph, start, goal):
	#initializing empty priorityQueue and Visited 
	visited=[]
	queue=[[(start,0)]]
	
	# while there are nodes in the graph which are to be explored 
	# we need to run this loop
	while queue:
		# sort the queue and pop
		queue.sort(
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


# doing the BFS on this graph
bfs(visited,graph,'1')
