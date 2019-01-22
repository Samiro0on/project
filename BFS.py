# CREATED BY SAMIR @29/09/2017
# BFS
# AI CLASS
# ASSIGNMENT WEEK 2

# here i am representing each city with english alph

map_Represention = {'Arad':'A','Zerind':'B','Sibiu':'C','Timisoara':'D'
    ,'Oradea':'E','Fagaras':'F','Rimnicu Vilcea':'G'
    ,'Lugoj':'H','Bucharest':'I','Pitesti':'J','Craiova':'K','Mehadia':'L'
    ,'Urziceni':'M','Giurgiu':'N','Dobreta':'O','Vaslui':'P','Hirsova':'Q'
    ,'Iasi':'R','Etorie':'S','Neamt':'T'}

# here i am going to list each city with it's neighbours

connect_Romania = {'A':['B','C','D'],'B':['A','E'],'C':['A','E','F','G']
               ,'D':['A','H'],'E':['B','C'],'F':['C','I'],'G':['C','J','K']
               ,'H':['D','L'],'I':['F','J','M','N'],'J':['G','K','I']
               ,'K':['J','G','O'],'L':['H','O'],'M':['I','P','Q'],'N':['I']
               ,'O':['L','K'],'P':['M','R'],'Q':['M','S'],'R':['P','T'],'S':['Q']
               ,'T':['R']}

# note popleft() time complexity O(1) but pop(0) O(n)

# mapping edges between cities = weight
we_Graph = (['A','B',75],['A','C',140],['A','D',118],['B','E',71],['C','E',151]
            ,['C','F',99],['C','G',80],['D','H',111],['F','I',211],['G','J',97]
            ,['G','K',146],['H','L',70],['I','J',101],['I','M',85],['I','N',90]
            ,['J','K',138],['K','O',120],['L','O',75],['M','P',142]
            ,['M','Q',98],['P','R',92],['Q','S',86],['R','T',87])

start_Node = 'A'
# city which i want to start from which is arad
destenation = 'I'
# city i want to reach which is bucharest
waiting_Queue = [start_Node]
# to hold on the next node i am going to visit
index = 0
#if (['A']==we_Graph[0].)
while len(waiting_Queue)>0:
    list1 = we_Graph[index]
    while(list1[0] == waiting_Queue[0]):
        list1 = we_Graph[index]
        if(list1[0] == waiting_Queue[0]):

                waiting_Queue.append(list1[1])
                print(waiting_Queue)


        index = index + 1
        #print(index)

    waiting_Queue.pop(0)
    #print(waiting_Queue)

# FEEEN L H W D ???????
print(waiting_Queue)
