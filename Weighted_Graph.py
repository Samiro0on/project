# class to draw a graph
# node , edge , weight
# created by SAMIR @29/09/2017
# AI Class 2017
# Prof. A.Saleh
# optimal solution = 366. Best answer will be 418 = UCS. BFS = 450
# map_Represention to map from city to alph
map_Represention = {'Arad':'A','Zerind':'B','Sibiu':'C','Timisoara':'D'
    ,'Oradea':'E','Fagaras':'F','Rimnicu Vilcea':'G'
    ,'Lugoj':'H','Bucharest':'I','Pitesti':'J','Craiova':'K','Mehadia':'L'
    ,'Urziceni':'M','Giurgiu':'N','Dobreta':'O','Vaslui':'P','Hirsova':'Q'
    ,'Iasi':'R','Etorie':'S','Neamt':'T'}

# connect_Romania to link each city with neighbours
connect_Romania = {'A':['B','C','D'],'B':['A','E'],'C':['A','E','F','G']
               ,'D':['A','H'],'E':['B','C'],'F':['C','I'],'G':['C','J','K']
               ,'H':['D','L'],'I':['F','J','M','N'],'J':['G','K','I']
               ,'K':['J','G','O'],'L':['H','O'],'M':['I','P','Q'],'N':['I']
               ,'O':['L','K'],'P':['M','R'],'Q':['M','S'],'R':['P','T'],'S':['Q']
               ,'T':['R']}

# we_Graph is a weighted graph to link 2 nodes and the related weight between them
we_Graph = (['A','B',75],['A','C',140],['A','D',118],['B','E',71],['C','E',151]
            ,['C','F',99],['C','G',80],['D','H',111],['F','I',211],['G','J',97]
            ,['G','K',146],['H','L',70],['I','J',101],['I','M',85],['I','N',90]
            ,['J','K',138],['K','O',120],['L','O',75],['M','P',142]
            ,['M','Q',98],['P','R',92],['Q','S',86],['R','T',87])
# take input from the user for the starting city and destination
start_Node = input("please enter the starting city make sure first letter is uppercase ")
start_Node = map_Represention.get(start_Node,"Wrong input, sorry")
#print(start_Node)
destination = input("Please enter your destination make sure first letter is uppercase ")
destination = map_Represention.get(destination,"Wrong input, sorry")
#print(destenation)


# a list have the visited nodes in order
waiting_Queue = [start_Node]

# a loop you can not go out till you visit all the nodes or find your destination
while len(waiting_Queue)>0:
    for index in range(len(we_Graph)):

# list1 is a list which i can hold each element of the tuple we_Graph
        list1 = we_Graph[index]

# the second condition to make sure their is no duplicated element in the list
        if list1[0] == waiting_Queue[0] and list1[1] not in waiting_Queue:
            waiting_Queue.append(list1[1])
            #print(waiting_Queue)
    # print(waiting_Queue)

# if i visited a certain node all neighbours and i did not find my destination so remove this node
    if waiting_Queue[len(waiting_Queue)-1] != destination:
        waiting_Queue.pop(0)

# if i found my destination hlt or go out from this while condition
    else:
        break

# right_path a list have the right route to my destination
right_path = [waiting_Queue[0],waiting_Queue[len(waiting_Queue) - 1]]
# temp_Start have a temporary start node or the parent of this child
temp_Start = [waiting_Queue[0]]

# a loop search for the right route it goes out when i found my starting node is first element of that list
while right_path[0] != start_Node:

    for list2 in we_Graph:
# search for the father or each child and add it to the right route
        if list2[1] == temp_Start[0]:
            right_path.insert(0,list2[0])
            temp_Start.pop()
            temp_Start.append(list2[0])
            break

#print(right_path)
# route is a list have the right route from stating node to my destination
route = []
for list3 in right_path:

# mapping keys and value in the first dictionary to represent the output in cities not alph
    for key,value in map_Represention.items():
        if list3 == value:
            #print("the right route is : ",key)
            route.append(key)
# print out the right route
print("the right route is : ",route)

# total_cost to sum all the weights through the right route
total_cost = 0

for i in range(len(right_path)-1):
    for list4 in we_Graph:
# calculate the weight between each two elements in the right route list
        if right_path[i] == list4[0] and right_path[i+1] == list4[1]:
            total_cost = total_cost + list4[2]
            break

# print out the total weight
print("the total distance is : ",total_cost)