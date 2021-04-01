def cost(closelist,cities):
    parent = closelist[0]
    finalCost = 0;
    for urutan in range(1,len(closelist)):
        for x in cities:
            if x == parent:
                for y in range(len(cities[x])):
                    if cities[x][y][0] == closelist[urutan]:
                        finalCost+=cities[x][y][1]
                parent = closelist[urutan]
    return finalCost

cities =  {
  "a": [1,1],
  "b": [2,2],
  "c":[3,3],
}
connection = {
    "a": [["b", 1],
          ["c",4]],
    "b":[["c", 1]]
}

def heuristic(cities, start, goal):
    dx = abs(cities[start][0] - cities[goal][0])
    dy = abs(cities[start][1] - cities[goal][1])
    return dx + dy

def fcost(g, h):
    return g + h

childs = []
open_list = []
closed_list = []
open_list.append('a')
Fcost = {'a': fcost(0, heuristic(cities,'a', 'c'))}
diffPath = 0
parent={}
while open_list:
    childs = []
    current = sorted(Fcost.items(), key=lambda x: x[1], reverse=False)[0][0]
    if current in open_list:
        open_list.remove(current)
        closed_list.append(current)

    if current == 'c':
        print(closed_list)
        print(cost(closed_list,connection))
        break
    for neighbour in connection[current]:
        if neighbour in closed_list:
            continue
        for new_path in connection[current]:
            if new_path[0] != neighbour[0]:
                for j in connection:
                    if j != current:
                        for index in range(len(connection[j])):
                            if connection[j][0][0] == neighbour[0]:
                                diffPath =(connection[j][0][-1] + new_path[-1])

        if diffPath < neighbour[-1] or neighbour[0] not in open_list:
            Fcost[neighbour[0]] = fcost(neighbour[-1], heuristic(cities,neighbour[0], "c"))
            childs.append(neighbour)
            parent[current] = childs
            if neighbour[0] not in open_list:
                open_list.append(neighbour[0])
        diffPath = 0
    Fcost.pop(current)