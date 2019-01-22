# A star search algo AI class 2018


we_Graph_h = (['A','B',75],['A','C',140],['A','D',118],['B','E',71],['C','E',151]
            ,['C','F',99],['C','G',80],['D','H',111],['F','I',211],['G','J',97]
            ,['G','K',146],['H','L',70],['I','J',101],['I','M',85],['I','N',90]
            ,['J','K',138],['K','O',120],['L','O',75] ,['M','P',142]
            ,['M','Q',98],['P','R',92],['Q','S',86],['R','T',87])

heuristic = {'A':366,'B':374,'C':253,'D':329,'E':380,'F':179,'G':193,'H':244,'I':0,'J':100,'K':160
            ,'L':241,'M':80,'P':199,'Q':151,'R':226}

start_Node = input("please enter the starting city make sure first letter is uppercase ")

destination = input("Please enter your destination make sure first letter is uppercase ")

waiting_Queue = [start_Node]
f_of_n = []
route = [start_Node]
#while waiting_Queue != destination:
for list in we_Graph_h:
    if list[0] == waiting_Queue[0]:
        waiting_Queue.append(list[1])
        f_of_n.append(list[-1] + heuristic.get(list[1]))
waiting_Queue.pop(0)
# print(min(f_of_n))
for index in range(len(f_of_n)):
    if f_of_n[index] == min(f_of_n):
        # print(waiting_Queue[index])
        route.append(waiting_Queue[index])
        waiting_Queue.clear()
        waiting_Queue.append(route[-1])
        break

print(waiting_Queue)
print("then")
print(route)
print("then")
print(f_of_n)
print("then")
