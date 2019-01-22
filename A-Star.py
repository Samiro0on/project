romania = [['Arad', 'Sibiu', 140], ['Arad', 'Timisoara', 118], ['Arad', 'Zerind', 75], ['Sibiu', 'Fagaras', 99],
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

cities = ['Arad', 'Bucharest', 'Craiova', 'Drobeta', 'Eforie', 'Fagaras', 'Giurgiu', 'Hirsova', 'Iasi', 'Lugoj',
          'Mehadia', 'Neamt', 'Oradea', 'Pitesti', 'Rimnicu Vilcea', 'Sibiu', 'Timisoara', 'Urziceni', 'Vaslui',
          'Zerind']

print(cities)
print("please make sure the spelling of city is correct.....\n")
start_city = input("please enter your current city:")
# goal_city = input("please enter the destination city:")
goal_city = 'Bucharest'
print("the goal city:", goal_city, "\n")

possible_solutions = []
for b in romania:
    if b[0] == start_city:
        gn = b[2]
        hn = heuristic.get(b[1])
        temp_b = [b[0], b[1], gn + hn]
        possible_solutions.append(temp_b)

print(possible_solutions)

goal_found = False

while goal_found is False:
    i = -1
    mini_branch_index = -1
    mini_cost = 1000
    for branch in possible_solutions:
        i += 1
        if branch[-1] <= mini_cost:
            mini_cost = branch[-1]
            mini_branch_index = i
    temp = possible_solutions.pop(mini_branch_index)
    temp_parent = temp[-2]
    if temp_parent is goal_city:
        goal_found = True
        total_cost = temp.pop()
        print("\nthe A* path is :", temp)
        print("total cost of path =", total_cost)
        break
    save_temp = temp.copy()
    for c in romania:
        if temp_parent == c[0]:
            temp_cost = temp.pop() - heuristic.get(temp_parent)
            temp.append(c[1])
            temp.append(temp_cost + heuristic.get(c[1]) + c[2])
            possible_solutions.append(temp)
            print(possible_solutions)
            temp = save_temp.copy()
