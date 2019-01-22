# name : Samir , @samiro0on , mail: mahmoudsamir109@gmail.com
# binary search tree 17/1/2019  , divide and conquer

# fun node , if smaller go left , if greater go right , repeat
def BinaryTree (unsortedList):
    leftChild, rightChild, rootNode = [], [], []
    for nTimes in range(len(unsortedList)):
        if nTimes == 0 :
            rootNode.append(unsortedList[0])
        else:
            if unsortedList[nTimes] <= rootNode[0] :
                leftChild.append(unsortedList[nTimes])
                BinaryTree(leftChild)
            if unsortedList[nTimes] > rootNode[0] :
                rightChild.append(unsortedList[nTimes])
                BinaryTree(rightChild)

    return leftChild + rootNode + rightChild

s = [65,45,22,14,70,47,95,477,18,694,25,98]
print(BinaryTree(s))

#fun node left right repeat
def BalancedTree (unsortedList):
    rootNode ,leftChild, rightChild = [], [], []
    for nTimes in range(len(unsortedList)):
        if nTimes == 0 :
            rootNode.append(unsortedList[0])
        else:
            if len(leftChild) < nTimes and len(leftChild) == len(rightChild):
                leftChild.append(unsortedList[nTimes])
                # BalancedTree(leftChild)
            else:
                rightChild.append(unsortedList[nTimes])
                # BalancedTree(rightChild)

    return leftChild + rootNode + rightChild

print(BalancedTree(s))
