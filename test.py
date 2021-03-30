class cities:
    def __init__(self, xcord, ycord):
        self.xcord = xcord
        self.ycord = ycord
    def __repr__(self):
        return (self.xcord, self.ycord)

class goal:
    def __init__(self, xcord, ycord):
        self.xcord = xcord
        self.ycord = ycord


a = cities(10, 10)
b = cities(15, 13)
c = cities(15, 8)
d = goal(20, 10)

connection = {
    "a": [["b", 4],
          ["c", 1]],
    "b":[["c", 10],
          ["d", 1]],
    "c":[["b",10],
        ["d", 5]],
}


def heuristic(cities, goal):
    dx = abs(cities.xcord - goal.xcord)
    dy = abs(cities.ycord - goal.ycord)
    return dx + dy


def fcost(g, h):
    return g + h


open_list = []
closed_list = []
open_list.append('a')
Fcost = {'a': fcost(0, heuristic(a, c))}
diffPath = 0
parent={}
while len(open_list) >0:
    current = sorted(Fcost, reverse=False)[0]

    if current in open_list:
        open_list.remove(current)
        closed_list.append(current)

    if current == 'd':
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
            Fcost[neighbour[0]] = fcost(neighbour[-1], heuristic(b, d))
            parent[current] = neighbour[0]
            if neighbour[0] not in open_list:
                open_list.append(neighbour[0])
    Fcost.pop(current)