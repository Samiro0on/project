# Created by Samir @06/10/2017
# AIMA dr.M.A.Saleh

# def is_Parent(father,child):
#     for step in new_graph:
#         if step[0] == father and step[1] == child:
#             return True
#         elif step[0] == child and step[1] == father:
#             print("this is a reverse route")
#             # 3ayez 23ml reverse l graph
#     return False

# we_graph = [['A','B',75],['A','C',140],['A','D',118],['B','E',71],['E','C',151] # i should write it C,E,151
#             ,['C','F',99],['C','G',80],['D','H',111],['F','I',211],['G','J',97]
#             ,['G','K',146],['H','L',70],['I','J',101],['I','M',85],['I','N',90]
#             ,['K','J',138],['K','O',120],['L','O',75],['M','P',142]
#             ,['M','Q',98],['P','R',92],['Q','S',86],['R','T',87]]

we_graph = [['Arad', 'Sibiu', 140], ['Arad', 'Timisoara', 118], ['Arad', 'Zerind', 75], ['Sibiu', 'Fagaras', 99],
           ['Sibiu', 'Rimnicu Vilcea', 80], ['Fagaras', 'Bucharest', 211], ['Bucharest', 'Giurgiu', 90],
           ['Bucharest', 'Urziceni', 85], ['Urziceni', 'Hirsova', 98], ['Urziceni', 'Vaslui', 142],
           ['Hirsova', 'Eforie', 86], ['Vaslui', 'Iasi', 92], ['Iasi', 'Neamt', 87], ['Rimnicu Vilcea', 'Craiova', 146],
           ['Rimnicu Vilcea', 'Pitesti', 97], ['Craiova', 'Pitesti', 138], ['Pitesti', 'Bucharest', 101],
           ['Timisoara', 'Lugoj', 111], ['Lugoj', 'Mehadia', 70], ['Mehadia', 'Drobeta', 75],
           ['Drobeta', 'Craiova', 120], ['Zerind', 'Oradea', 71], ['Oradea', 'Sibiu', 151]]

heuristic = {'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242, 'Eforie': 161, 'Fagaras': 176,
             'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234,
             'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193, 'Sibiu': 253, 'Timisoara': 329,
             'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374}


start_node = input("Please enter the starting node ... Make sure first letter is uppercase ... ")
destination = input("Please enter the destination node ... Make sure first letter is uppercase ... ")
type_of_search = int(input("Please select type of searching algo press 1 for BFS, press 2 for DFS, press 3 for UCS, press 4 for A star. "))

if type_of_search == 1 :
    queue =[start_node]
    destination_found = False
    repeated_element = False
    route = []
    while destination_found is False and len(queue)>0 :
        for branch in we_graph:
            if branch[0] == queue[0]:
        # searching in each list at index 0 if equal to the first element in the waiting queue
                for index in range(len(queue)):
                    if branch[1] == queue[index]:
                        repeated_element = True
                        break
                    else:
                        repeated_element = False
                if repeated_element is False:
                    queue.append(branch[1])
                    #print(queue)
                    route.append(branch)

                    if branch[1] == destination :
                        destination_found = True
                        break
                    else:
                        repeated_element = False
        queue.pop(0)

                #i = i +1
    #print(route)
    #print(queue)


             #else:
                #print("Did not find a direct route to your distination !")
                # lw ml2ash feh graph awel element = start node e3ml reverse ele graph

    right_path = [route[-1][0],destination]
    #print(right_path)
    temp_start = [queue[0]]
    while right_path[0] != start_node:
        for list in route:
            if list[1] == temp_start[0]:
                right_path.insert(0,list[0])
                temp_start.pop()
                temp_start.append(list[0])
                break
    print("the BFS route is ",right_path)

    total_cost = 0

    for i in range(len(right_path)-1):
        for list in we_graph:
    # calculate the weight between each two elements in the right route list
            if right_path[i] == list[0] and right_path[i+1] == list[1]:
                total_cost = total_cost + list[2]
                break
    print("the total distance is : ",total_cost)

elif type_of_search == 2 :
    stack = [start_node]
    destination_found = False
    repeated_element = False
    route = [start_node]
    while destination_found is False and len(stack) > 0:        #leeh and
        for branch in we_graph :
            if branch[0] == stack[-1]:
                for index in range(len(stack)):
                    if branch[1] == stack[index]:
                        repeated_element = True
                        break
                    else:
                        repeated_element = False
                if repeated_element is False:
                    stack.insert(0,branch[1])
                    route.append(branch[1])
                    stack.pop(-1)
                    #print(stack)
                if branch[1] == destination :
                    destination_found = True
                    break


#print(stack)
    print("The DFS route is " , route)
    total_cost = 0

    for i in range(len(route) - 1):
        for list in we_graph:
            # calculate the weight between each two elements in the right route list
            if route[i] == list[0] and route[i + 1] == list[1]:
                total_cost = total_cost + list[2]
                break
    print("the total distance is : ", total_cost)

elif type_of_search == 3:
    goal_found = False
    possible_routes = we_graph.copy()

    for branch in we_graph:
        if branch[0] != start_node:
            possible_routes.remove(branch)

    while goal_found is False:
        i = -1
        branchIndex = -1
        minCost = 999

        for minBranch in possible_routes:
            i += 1
            if minBranch[-1] <= minCost:
                minCost = minBranch[-1]
                branchIndex = i
                # print("i= ", i)

        temp = possible_routes.pop(branchIndex)
        new_parent = temp[-2]
        if new_parent == destination:
            goal_found = True
            total_cost = temp.pop()
            print("The UCS path is : ", temp)
            print("Total cost of path = ", total_cost)
            break
        saveTemp = temp.copy()
        for branch in we_graph:
            if new_parent == branch[0]:
                temp_cost = temp.pop()
                temp.append(branch[1])
                temp.append(temp_cost + branch[-1])
                possible_routes.append(temp)
                # print(possible_routes)
                temp = saveTemp.copy()


elif type_of_search == 4:
    goal_found = False
    possible_routes = we_graph.copy()

    for branch in we_graph:
        if branch[0] != start_node:
            possible_routes.remove(branch)
    print(possible_routes)
    for list in possible_routes:
        g_of_n = list.pop()
        list.append(g_of_n + heuristic.get(list[-1]))
    print(possible_routes)

    while goal_found is False:
        i = -1
        branchIndex = -1
        minCost = 999

        for minBranch in possible_routes:
            i += 1
            if minBranch[-1] <= minCost:
                minCost = minBranch[-1]
                branchIndex = i
                # print("i= ", i)

        temp = possible_routes.pop(branchIndex)
        new_parent = temp[-2]
        if new_parent == destination:
            goal_found = True
            total_cost = temp.pop()
            print("The UCS path is : ", temp)
            print("Total cost of path = ", total_cost)
            break
        saveTemp = temp.copy()
        for branch in we_graph:
            if new_parent == branch[0]:
                temp_cost = temp.pop()
                temp.append(branch[1])
                temp.append(temp_cost + branch[-1] + heuristic.get(branch[-2]) - heuristic.get(branch[0]))
                possible_routes.append(temp)
                # print(possible_routes)
                temp = saveTemp.copy()
