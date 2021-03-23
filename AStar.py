from collections import deque
from math import sqrt

import numpy as py
class Graph:

    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    # heuristic function with equal values for all nodes
    def h(self, n):
        H = {
            'A': 1,
            'B': 1,
            'C': 1,
            'D': 1,
            'E' : 1

        }
        #  h = sqrt ( (current_cell.x – goal.x)2 +
        #             (current_cell.y – goal.y)2 )
        return H[n]

    howMany = input("How many Cities");
    print(howMany)

    cities = {}
    citiesCoord = []

    for x in range(int(howMany)):
        temp = []
        citiesCoord.append(str(input("Cities")))
        coordsX = int(input("Input Coord X"))
        coordsy = int(input("Input Coord y"))
        temp.append(coordsX)
        temp.append(coordsy)
        cities[citiesCoord[x]] = temp
    # print(cities["A"])
    # print(cities["A"][0])


    def connections(cities):
        adjacent_list = {}
        for x in cities:
            tempArr = []
            connection = int(input("How many Connection ? "))
            for j in range(connection):
                # for z in range(1):
                cityConnect = str(input("City Name"))
                cityCoord = int(input("City Coord"))
                tempCoord = (cityConnect, cityCoord)
                tempArr.append(tempCoord)
                # tempArr.append(cityCoord)
                adjacent_list[x] = tempArr
        return adjacent_list
          #adjacent_list[x] =

    # print(cities[0])
    for x in cities:
        print(cities[x][0], cities[x][1])
    # print(cities)
    endGoal = str(input("What is the Destinations? "))
    def Heuristic(city,end):
        temporarryArr = []
        for x in city:
            if city[x] != city[end]:
                temporarryArr.append((sqrt(((city[x][0] - city[end][0])**2) + ((city[x][1] - city[end][1])**2))))
        return temporarryArr;

    # print(len());
    # adjacent_list = {
    # for x in cities:
    #
    # }
    print(Heuristic(cities,endGoal))

    def HeuristicsValue(citiesHeuristic, tempArr,end):
        valueH = {}
        j = 0;
        for x in citiesHeuristic:
            if x != end:
                valueH[x] = tempArr[j]
                j += 1;
        return valueH;
    print(HeuristicsValue(cities, Heuristic(cities,endGoal),endGoal), "This is Heuristic Value")
    print(cities)
    print(connections(cities))


    adjacent_list = {}

    def a_star_algorithm(self, start_node, stop_node):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = set([start_node])
        closed_list = set([])

        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}

        g[start_node] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            # find a node with the lowest value of f() - evaluation function
            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v;

            if n == None:
                print('Path does not exist!')
                return None

            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print(str('Path found: {}'.format(reconst_path)) ,"Cost:" +  str(g[stop_node]))
                return reconst_path

            # for all neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None



# for x in cities["A"]["coordsX"]:
#     print(x)


adjacency_list = {'A': [('B', 7), ('D', 6)],
'B': [('C', 5), ('E', 10)],
'C': [('E', 5)],
'D': [('E', 4)]}



# print(adjacency_list)

# graph1 = Graph(adjacency_list)
# graph1.a_star_algorithm('A', 'E')
#


