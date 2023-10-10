# References
# https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/

# Tim Tran
# 1001638285

# Imports time to use for keeping track of execution time
import time

# Sets the mode to either continuous or iterative
mode = 1


# Initializes the number of cycles to 0
cycles = 0

# Creates the graph class
class Graph:
    
    # The graph class is initialized with the number of vertices and an empty array that will contain the edges of the graph
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
    
    # Adds the paths to the graph    
    def add_path(self, source, destination, length):
        self.graph.append([source, destination, length])
    
    # Prints the solution
    def print_solution(self, distance, source):

        print("\n_______________\nSource:", source)
        print("\nVertex\t\tDistance")

        # Prints the distances of the nodes besides the source node
        for k in range(1, self.V):
            if k == source:
                continue

            print("{0}\t\t{1}".format(k, distance[k]))
            
        print("_______________")
        
    # Calculates the shortest distance
    def calculate(self, src):
        # Initializes the initial value to infinity
        distance = [float("Inf")] * self.V
        # Sets the distance of the node to itself to 0
        distance[src] = 0
        # Iterates through each other node
        for x in range(self.V - 1):
            for source, destination, length in self.graph:
                if distance[source] != float("Inf") and distance[source] + length < distance[destination]:
                    distance[destination] = distance[source] + length
                    
            # Prints out the current source's current distances to other nodes iteratively
            if mode == 2:
                print("Current node distances")
                self.print_solution(distance, src)
                while(1):
                    y = input("To continue, type in Y: ")
                    if y == "Y":
                        break
            global cycles
            cycles+=1
        
        # Prints out all of the nodes final distances to other nodes
        if mode == 1:
            self.print_solution(distance, src)
            
# The user must select the mode        
while 1:
    select = input("Please type in 1 for continuous or 2 for iterative: ")
    if select == "1":
        mode = 1
        break
    elif select == "2":
        mode = 2
        break
    else:
        continue

f = open("input.txt", "r")

nodes = []
num = 0

# Puts the input into an array to be read
for x in f:
    nodes.append([])
    nodes[num].append(int(x[0]))
    nodes[num].append(int(x[2]))
    nodes[num].append(int(x[4]))
    num+=1

# initializes the graph
g = Graph(len(nodes))

# Adds all paths to graph
for x in nodes:
    g.add_path(x[0], x[1], x[2])
    g.add_path(x[1], x[0], x[2])

# Sets the start time
start_time = time.time()

# Calculates the distances for all the nodes
for x in range(g.V-1):
    g.calculate(x+1)
    
# Prints the final time
if mode == 1:
    print("\n--- %s seconds ---" % (time.time() - start_time))
    
print("Cycles: %d" % (cycles))