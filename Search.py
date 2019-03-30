from pacman_ai.Globals import Directions
from collections import deque


def depth_first_search(layout):
    directionTable = {'South': Directions.SOUTH, 'North': Directions.NORTH,
                      'West': Directions.WEST, 'East': Directions.EAST}
    # create a Stack to keep track of nodes we are going to explore
    my_stack = []

    done = set()  # to keep track or explored nodes

    start_point = layout.agentPositions

    # we will push in tuples (coordinates, pass) in the stack
    my_stack.append((start_point, []))
    while len(my_stack) != 0:
        next_node = my_stack.pop()
        coordinate = next_node[0]
        new_pass = next_node[1] if next_node[1] is not None else []

        if layout.is_goal(coordinate):
            return new_pass
        if coordinate not in done:
            done.add(coordinate)
            for k in layout.get_neighbours(coordinate):

                if k[0] not in done:
                    my_stack.append((k[0], new_pass + [directionTable[k[1]]]))


def breadth_first_search(layout):
    directionTable = {'South': Directions.SOUTH, 'North': Directions.NORTH,
                      'West': Directions.WEST, 'East': Directions.EAST}
    # create a Queue to keep track of nodes we are going to explore
    my_queue = deque([])

    done = set()  # to keep track or explored nodes

    start_point = layout.agentPositions

    # we will push tuples (coordinates, pass) in the stack
    my_queue.append((start_point, []))

    while len(my_queue) != 0:
        next_node = my_queue.popleft()
        coordinate = next_node[0]
        new_pass = next_node[1]

        if layout.is_goal(coordinate):
            return new_pass
        if coordinate not in done:
            done.add(coordinate)
            for k in layout.get_neighbours(coordinate):
                if k[0] not in done:
                    my_queue.append((k[0], new_pass + [directionTable[k[1]]]))


def uniform_cost_search(problem):
    directionTable = {'South': Directions.SOUTH, 'North': Directions.NORTH,
                      'West': Directions.WEST, 'East': Directions.EAST}

    # create a Queue to keep track of nodes we are going to explore
    myQueue = util.PriorityQueue()

    done = set()  # to keep track or explored nodes

    startPoint = problem.startingState()

    # we will push in the queue tuples (coordinates, pass)
    # thus, we do not need additional dictionary for the passes (as we have in DFS)
    myQueue.push((startPoint, []), 0)

    while not myQueue.isEmpty():
        nextNode = myQueue.pop()
        coordinate = nextNode[0]
        newPass = nextNode[1]

        if problem.isGoal(coordinate):
            return newPass
        if coordinate not in done:
            done.add(coordinate)
            for k in problem.successorStates(coordinate):
                if k[0] not in done:
                    # we need to calculate a new priority
                    cost = problem.actionsCost(newPass + [directionTable[k[1]]])
                    myQueue.push((k[0], newPass + [directionTable[k[1]]]), cost)


# Abbreviations
bfs = breadth_first_search
dfs = depth_first_search
ucs = uniform_cost_search
