#Importing necessary libraries
import numpy as np
import random
from collections import deque
import copy

# # One can change the initial state here:
#Defining initial state
initial_state = np.array([[1, 4, 7], [5, 0, 8], [2, 3, 6]])

#Defining goal state
goal_state = [i for i in range(1,9)]
goal_state.append(0)
goal_state = np.array(goal_state)
goal_state = np.reshape(goal_state, (-1, 3))
goal_state = goal_state.T

#Defining a Node
def node_info(Node_State_i, Node_Index_i, Parent_Node_Index_i):
    info = [Node_State_i, Node_Index_i, Parent_Node_Index_i]
    return info

#Function that returns the position of the blank tile
def blank_tile(state):
    result = np.where(state == 0)
    return int(result[0]+1), int(result[1]+1)

#Function to move the blank tile to the left
def ActionMoveLeft(node_array):
    a, b = blank_tile(node_array)
    temp_node = copy.deepcopy(node_array)
    if b!=1:
        temp = temp_node[a-1][b-2]
        temp_node[a-1][b-2] = 0
        temp_node[a-1][b-1] = temp
        return True, temp_node
    else:
        return False, temp_node

#Function to move the blank tile to the right
def ActionMoveRight(node_array):
    a, b = blank_tile(node_array)
    temp_node = copy.deepcopy(node_array)
    if b!=3:
        temp = temp_node[a-1][b]
        temp_node[a-1][b] = 0
        temp_node[a-1][b-1] = temp
        return True, temp_node
    else:
        return False, temp_node

#Function to move the blank tile Up
def ActionMoveUp(node_array):
    a, b = blank_tile(node_array)
    temp_node = copy.deepcopy(node_array)
    if a!=1:
        temp = temp_node[a-2][b-1]
        temp_node[a-2][b-1] = 0
        temp_node[a-1][b-1] = temp
        return True, temp_node
    else:
        return False, temp_node

#Function to move the blank tile Down
def ActionMoveDown(node_array):
    a, b = blank_tile(node_array)
    temp_node = copy.deepcopy(node_array)
    if a!=3:
        temp = temp_node[a][b-1]
        temp_node[a][b-1] = 0
        temp_node[a-1][b-1] = temp
        return True, temp_node
    else:
        return False, temp_node

#Function that checks if a node is in the node_list
def NotInList(node_array, node_list):
    for element in node_list:
        a = copy.deepcopy(element[0])
        if np.array_equal(node_array, a):
            return False
    return True

#Initializing Deque class, list of visited nodes
q = deque()
Node_Index_i = np.array([1]) 
Parent_Node_Index_i = np.array([0])
a = copy.deepcopy(initial_state)
b = copy.deepcopy(Node_Index_i)
c = copy.deepcopy(Parent_Node_Index_i)
initial_node = node_info(a, b, c)
q.append(initial_node)
visited_node = []

#Program that uses Breadth First Search Algorithm to explore all possible states from the initial state and stores it in a tree.
while True:
    temp = q.popleft()
    z = copy.deepcopy(temp)
    visited_node.append(z)
    
    a = ActionMoveLeft(z[0])
    if (a[0] and NotInList(a[1], visited_node)):
        Node_Index_i += 1
        e = copy.deepcopy(temp)
        f = copy.deepcopy(Node_Index_i)
        node = node_info(a[1], f, e[1])
        q.append(node)
        if np.array_equal(a[1], goal_state):
            visited_node.append(q[-1])
            break

    a = ActionMoveRight(z[0])
    if (a[0] and NotInList(a[1], visited_node)):
        Node_Index_i += 1
        g = copy.deepcopy(temp)
        h = copy.deepcopy(Node_Index_i)
        node = node_info(a[1], h, g[1])
        q.append(node)
        if np.array_equal(a[1], goal_state):
            visited_node.append(q[-1])
            break

    a = ActionMoveUp(z[0])
    if (a[0] and NotInList(a[1], visited_node)):
        Node_Index_i += 1
        l = copy.deepcopy(temp)
        m = copy.deepcopy(Node_Index_i)
        node = node_info(a[1], m, l[1])
        q.append(node)
        if np.array_equal(a[1], goal_state):
            visited_node.append(q[-1])
            break

    a = ActionMoveDown(z[0])
    if (a[0] and NotInList(a[1], visited_node)):
        Node_Index_i += 1
        j = copy.deepcopy(temp)
        k = copy.deepcopy(Node_Index_i)
        node = node_info(a[1], k, j[1])
        q.append(node)
        if np.array_equal(a[1], goal_state):
            visited_node.append(q[-1])
            break

#Function that generates the path from the initial state to the goal state and stores it in "nodePath.txt" file. 
#It also creates a "Nodes.txt" file which contains all the visited nodes and "NodeInfo.txt" file which contains Index 
# of a node and its parent's node
def generate_path(node_list):
    A = [element[0] for element in node_list]
    B = [element[1] for element in node_list]
    C = [element[2] for element in node_list]

    i = -1
    path = []
    
    while i!=0:
        path.append(A[i])
        i = B.index(C[i])
        c = C[i]
    
    goal_state = [i for i in range(1,9)]
    goal_state.append(0)
    goal_state = np.array(goal_state)
    goal_state = np.reshape(goal_state, (-1, 3))
    goal_state = goal_state.T
    
    path.append(initial_state)
    path.reverse()
    
    textfile = open("nodePath.txt", "w")
    
    for element in path:
        for i in range(element.shape[1]):
            for sub_element in element[:,i]:
                textfile.write(str(sub_element) + " ")
        textfile.write("\n")
    textfile.close()
    
    textfile1 = open("Nodes.txt", "w")
    for element in A:
        for i in range(element.shape[1]):
            for sub_element in element[:,i]:
                textfile1.write(str(sub_element) + " ")
        textfile1.write("\n")
    textfile1.close()
    
    textfile2 = open("NodesInfo.txt", "w")
    textfile2.write("Node_index" + 5*" " + "Parent_Node_index\n")
    for i in range(len(B)):
        textfile2.write(5*" " + str(B[i][0]) + 17*" " + str(C[i][0]))
        textfile2.write("\n")
    textfile2.close()

generate_path(visited_node)




