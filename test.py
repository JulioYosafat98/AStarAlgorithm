cities =  {
  "a": [10,20],
  "b": [24,10],
  "c":[24,28],
  "d":[41,29],
  "e":[60,20]
}
connection = {
    "a": [["b", 5],
          ["e", 100],
          ["c",10]],
    "b":[["e", 5]],
    "c":[["d", 10]],
    "d":[["e",10]]
}


def heuristic(cities, start, goal):
    dx = abs(cities[start][0] - cities[goal][0])
    dy = abs(cities[start][1] - cities[goal][1])
    return dx + dy


def fcost(g, h):
    return g + h


open_list = []
closed_list = []
open_list.append('a')
Fcost = {'a': fcost(0, heuristic(cities,'a', 'e'))}
diffPath = 0
parent={}
while open_list:
    current = sorted(Fcost.items(), key=lambda x: x[1], reverse=False)[0][0]
    if current in open_list:
        open_list.remove(current)
        closed_list.append(current)

    if current == 'e':
        print("the end")
        print(parent)
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
            Fcost[neighbour[0]] = fcost(neighbour[-1], heuristic(cities,neighbour[0], "e"))
            parent[current] = neighbour
            if neighbour[0] not in open_list:
                open_list.append(neighbour[0])
        diffPath = 0
    Fcost.pop(current)