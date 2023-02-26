# 8-puzzle solver using Breadth First Search (BFS) 
This repository contains code to solve a 8-puzzle problem using Breadth First Search (BFS). 

<img src="https://github.com/AbhijitMahalle/8-puzzle-solver/blob/master/gif/8_puzzle_solver.gif" width="300" height="300"/>  

## Requirement:
  - Python 2.0 or above

## Dependencies:
  - NumPy
  - random
  - collections 
  - copy

## Instruction to run the code:
```
python 8_puzzle_solver.py
```
## Output
Three output textfile are generated:  
1. nodePath.txt contains states with elements in the column-wise format from the start state to the goal state.
2. NodesInfo.txt stores information of a node_index and its parent in two columns for backtracking.
3. Nodes.txt stores all the explored states.  

plot_path.py file helps in visualizing the output of BFS. 
Visualization for start state 1 5 2 4 0 3 7 8 6 to reach the goal state 1 2 3 4 5 6 7 8 0 is given below:  
 
<img src = "https://github.com/AbhijitMahalle/8-puzzle-solver/blob/master/results/visualization.png" width="170" height="1000"/>
