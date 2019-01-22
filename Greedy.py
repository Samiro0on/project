



map_Represention = {'Arad':'A','Zerind':'B','Sibiu':'C','Timisoara':'D'
    ,'Oradea':'E','Fagaras':'F','Rimnicu Vilcea':'G'
    ,'Lugoj':'H','Bucharest':'I','Pitesti':'J','Craiova':'K','Mehadia':'L'
    ,'Urziceni':'M','Giurgiu':'N','Dobreta':'O','Vaslui':'P','Hirsova':'Q'
    ,'Iasi':'R','Etorie':'S','Neamt':'T'}




#[start,end,weight,heuristic]
we_Graph_h = (['A','B',75],['A','C',140],['A','D',118],['B','E',71],['C','E',151]
            ,['C','F',99],['C','G',80],['D','H',111],['F','I',211],['G','J',97]
            ,['G','K',146],['H','L',70],['I','J',101],['I','M',85],['I','N',90]
            ,['J','K',138],['K','O',120],['L','O',75] ,['M','P',142]
            ,['M','Q',98],['P','R',92],['Q','S',86],['R','T',87])

heuristic = {'A':366,'B':374,'C':253,'D':329,'E':380,'F':179,'G':193,'H':244,'I':0,'J':100,'K':160
            ,'L':241,'M':80,'P':199,'Q':151,'R':226}


start_Node = input("please enter the starting city make sure first letter is uppercase ")  # _*
start_Node = map_Represention.get(start_Node)
destination = input("Please enter your destination make sure first letter is uppercase ")  #Bucharest
#destination = 'I'
destination = map_Represention.get(destination)
#ya5od heuristic A  mleeesh da3wa b 366 babos 3la el b3deha w lazem tkon 22al mn 366

waiting_Queue = [start_Node]
route = [start_Node]
heuristic_value = []

while True:
    for list in we_Graph_h:
        if list[0] == waiting_Queue[0]:
            waiting_Queue.append(list[1])
    waiting_Queue.pop(0)
    for index in waiting_Queue:
        heuristic_value.append(heuristic.get(index))
    right_node = min(heuristic_value)
    for k , v in heuristic.items():
        if v == right_node:
            waiting_Queue.clear()
            waiting_Queue.append(k)
            route.append(k)
            break
    if route[-1] == destination:
        break
total_cost = 0
for i in range(len(route)-1):
    for temp in we_Graph_h:
# calculate the weight between each two elements in the right route list
        if route[i] == temp[0] and route[i+1] == temp[1]:
            total_cost = total_cost + temp[2]
            break

print("total distance or cost in km is " , total_cost)

for key,value in map_Represention.items():
    for i in range(len(route)):
        if route[i] == value:
            route.append(key)
            route.pop(0)

print("the greedy path is " , route)


