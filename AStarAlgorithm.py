from math import sqrt
adjacent_list = {}
cities = {}
citiesCoord = []
parent= {}
howMany = input("How many Cities: ")

for x in range(int(howMany)):
    temp = []
    citiesCoord.append(str(input("Input City Name: ")))
    coordsX = int(input("Input x coordinate: "))
    coordsy = int(input("Input y coordinate: "))
    temp.append(coordsX)
    temp.append(coordsy)
    cities[citiesCoord[x]] = temp

def connections(cities):

    for x in cities:
        tempArr = []
        connection = int(
                input("How many Connection for city " +
                      str(x) + ": "))
        for j in range(connection):
                # for z in range(1):
            cityConnect = str(input("City Name: "))
            cityWeight = int(input("Weight: "))
            tempCoord = (cityConnect, cityWeight)
            tempArr.append(tempCoord)
             # tempArr.append(cityCoord)
            adjacent_list[x] = tempArr
    return adjacent_list
for x in cities:
    print(cities[x][0], cities[x][1])
    # print(cities)
endGoal = str(input("What is the Destination? "))

def Heuristic(city, end):
    temporarryArr = []
    for x in city:
        if city[x] != city[end]:
            temporarryArr.append(
                    (sqrt(((city[x][0] - city[end][0])**2) + ((city[x][1] - city[end][1])**2))))
    return temporarryArr
def HeuristicsValue(citiesHeuristic, tempArr, end):
    valueH = {}
    j = 0
    for x in citiesHeuristic:
        if x != end:
            valueH[x] = tempArr[j]
            j += 1
        elif x == end:
            valueH[x] = 0
    return valueH
print(HeuristicsValue(cities, Heuristic(cities, endGoal),
          endGoal), "This is Heuristic Value for A")
ConnectionsOfCity = connections(cities)

HeuritcValueCities = HeuristicsValue(cities, Heuristic(cities, endGoal),
          endGoal)

def h(n): #isinya Nilai Heuristic dari masing2 Nodes

    H = HeuristicsValue(cities, Heuristic(cities, endGoal),
          endGoal)
    return H[n]




# print(h("B"))

# ------------- A* Algorithm
print(adjacent_list["A"][0][1]) #Cara manggil Weight dari Adjacent Masing2
print(adjacent_list)
open_list = set()
close_list = set()
start_node = str(input("What is the Start Nodes"))

open_list.add(start_node)

# print(open_list)
temp = h(start_node);
current = 0;
#
print(adjacent_list)
close_list = set()

HeuritcValueCities = HeuristicsValue(cities, Heuristic(cities, endGoal),
                                     endGoal)
open_list = set()
start_node = str(input("What is the Start Nodes"))
open_list.add(start_node)
# cur = start_node
# curpath = []
# curpath.append([cur, ], 0)

# while len(curpath) > 0:
#     if curpath == None:
#         print("No Path")
#         break;

## ----------------------------- Next Step = Create a function that hold the value for weight of each Nodes!
# ------------------------------ Then next try to compare it to each Node of a parents

z = 0;
fcost = {}
while len(open_list) > 0:

    for x in open_list:
        for y in range(len(adjacent_list[x])):
               gCost = adjacent_list[x][y][1] ## Weight for each Adjacent List
               hCost = h(adjacent_list[x][y][0]) ## Heuristic Cost of each Adjacent List
               # print(gCost, hCost)
               fcost[adjacent_list[x][y][0]] = gCost + hCost
    # break
               # fcost[] =
               #open_list.remove(x) this is to remove

    currrent = fcost[list(fcost.keys())[0]] #First Key in the Dictionary for comparing the smallest Fcost
    curr = 0;
    for i in fcost:
        temp = fcost[i]
        if temp < current:
            curr = i;
    open_list.pop(current)
    close_list.add(current)

    if current == endGoal:
        print("We reach The Goal")
        break;

    for neighbour in adjacent_list[current]:
        for i in close_list:
            if neighbour == None or neighbour == i:
                continue;
        new_path = fcost[neighbour]
        if new_path <  fcost[current] or neighbour not in close_list:
            fcost[current] = fcost[neighbour]
            parent[neighbour] = current
            if neighbour not in open_list:
                open_list.add(neighbour)















