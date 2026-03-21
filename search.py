from collections import deque
import heapq
import funcs
# hi
def search(strategy, grid, start, goal, teleports):
    expanded = []
    search_path = {start: None}
    counter = 0     # for tie breaking

    # initialising the fringe
    if strategy in ('D', 'B'):
        fringe = deque([start])
    else:
        fringe = []
        heapq.heappush(fringe, (0, start[0], start[1], 0, 0, start))    # minheap data structure
#                               ^pri ^xstart ^ystart  ^cnt ^g ^pos
    while fringe:

        if strategy == 'B':
            current = fringe.popleft()              # remove oldest node added to fringe (BFS)
        elif strategy == 'D':
            current = fringe.pop()                  # remove newest added node to fringe (DFS)

        else:
            _, _, _, _, current_g, current = heapq.heappop(fringe)    # remove the lowest priority value from fringe


        if current in expanded:
            continue
        expanded.append(current)    # add the current node to expanded list, if not already in there

        if current == goal:
            path = funcs.rebuild_path(search_path, goal)
            return expanded, path   # return the expanded list and path if goal found
        
        for neighbour in funcs.get_neighbours(current, grid, teleports):
            if neighbour not in expanded:
                search_path[neighbour] = current    # 'the parent of neighbour is current'
                                                    # adding the new neighbour into search dictionary
                if strategy == 'B' or strategy == 'D':
                    fringe.append(neighbour)

                else:



    


