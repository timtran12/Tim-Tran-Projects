import sys, queue

array = []
f = open(sys.argv[1], "r")
lines = f.readlines()
f.close()

for row in lines:
    if(row == "END OF INPUT" or row == "END OF INPUT\n"):
        break
    row = row.strip()
    words = row.split(" ")
    array.append(words)

nodes_expanded = 0
nodes_generated = 0
distance = 0
start = sys.argv[2]
destination = sys.argv[3]
heuristics = []
route = []

class Node:
    def __init__(self, name):
        self.name = name
        self.previous_distance = 0
        self.distance_traveled = 0
 
q = queue.PriorityQueue()

if(len(sys.argv) > 4):
    f = open(sys.argv[4], "r")
    lines = f.readlines()
    f.close()
    for row in lines:
        if(row == "END OF INPUT" or row == "END OF INPUT\n"):
            break
        row = row.strip()
        words = row.split(" ")
        heuristics.append(words)
    
    destination_est = 0
    for i in heuristics:
        if(destination == i[0]):
            destination_est = int(i[1])
            break
        
    current = Node(start)
    path = []
    visited = []
    q.put((destination_est, [current]))
    nodes_generated+=1

    while not(q.empty()):
        current_cost, current = q.get()
        for i in heuristics:
            if(current[-1].name == i[0]):
                destination_est = int(i[1])
                break
        nodes_expanded+=1
        if(current[-1].name in visited):
            continue
        else:
            visited.append(current[-1].name)
        if(current[-1].name == destination):
            distance = current[-1].distance_traveled
            path = current
            print("nodes expanded: %d" % (nodes_expanded))
            print("nodes generated: %d" % (nodes_generated))

            print("distance: %d km" % (distance))
            print("route:")
            for i in range(len(path)-1):
                print("%s to %s, %.1d km" % (path[i].name, path[i+1].name, path[i+1].previous_distance))
            break
    
        for i in array:
            if(current[-1].name == i[0]):
                new = Node(i[1])
                for j in heuristics:
                    if(new.name == j[0]):
                        destination_est = int(j[1])
                        break
                nodes_generated+=1
                new.previous_distance = int(i[2])
                new.distance_traveled = int(i[2])+current[-1].distance_traveled
                q.put((new.distance_traveled+destination_est, current+[new]))
            
            if(current[-1].name == i[1]):
                new = Node(i[0])
                for j in heuristics:
                    if(new.name == j[0]):
                        destination_est = int(j[1])
                        break
                nodes_generated+=1
                new.previous_distance = int(i[2])
                new.distance_traveled = int(i[2])+current[-1].distance_traveled
                q.put((new.distance_traveled+destination_est, current+[new]))
            
    if(q.empty()):
        print("nodes expanded: %d" % (nodes_expanded))
        print("nodes generated: %d" % (nodes_generated))

        print("distance: infinity")
        print("route:")
        print("none")
        
        
else:
    current = Node(start)
    path = []
    visited = []
    q.put((0, [current]))
    nodes_generated+=1

    while not(q.empty()):
        current_cost, current = q.get()
        nodes_expanded+=1
        if(current[-1].name in visited):
            continue
        else:
            visited.append(current[-1].name)
        if(current[-1].name == destination):
            distance = current_cost
            path = current
            print("nodes expanded: %d" % (nodes_expanded))
            print("nodes generated: %d" % (nodes_generated))

            print("distance: %d km" % (distance))
            print("route:")
            for i in range(len(path)-1):
                print("%s to %s, %.1d km" % (path[i].name, path[i+1].name, path[i+1].previous_distance))
            break
    
        for i in array:
            if(current[-1].name == i[0]):
                new = Node(i[1])
                nodes_generated+=1
                new.previous_distance = int(i[2])
                q.put((current_cost+int(i[2]), current+[new]))
            
            if(current[-1].name == i[1]):
                new = Node(i[0])
                nodes_generated+=1
                new.previous_distance = int(i[2])
                q.put((current_cost+int(i[2]), current+[new]))
            
    if(q.empty()):
        print("nodes expanded: %d" % (nodes_expanded))
        print("nodes generated: %d" % (nodes_generated))

        print("distance: infinity")
        print("route:")
        print("none")