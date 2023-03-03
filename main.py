import math


class city:

  def __init__(self, name, coords):
    self.name = name
    self.coords = coords


fstream = open("Adjacencies.txt", 'r')
line = fstream.readline()
listAdjacencies = []
while line:
  listAdjacencies.append(line.replace(" \n", "").replace("\n", "").split(" "))
  line = fstream.readline()
fstream.close()
adjacencies = {}
for cities in listAdjacencies:
  adjacencies.update({cities[0]: cities[1::]})
myDict = {}
for i in adjacencies:
  for c in adjacencies[i]:
    if c not in adjacencies.keys():
      myDict[c] = []
for i in adjacencies:
  for c in adjacencies[i]:
    if c not in adjacencies.keys():
      myDict[c].append(i)
for i in adjacencies:
  for c in adjacencies[i]:
    for j in adjacencies:
      if c == j:
        if i not in adjacencies[j]:
          adjacencies[j].append(i)
for i in adjacencies:
  myDict.update({i: adjacencies[i]})
myKeys = list(myDict.keys())
myKeys.sort()
sorted_dict = {i: myDict[i] for i in myKeys}
adjacencies = sorted_dict
listCoords = []
fstream = open("coordinates.txt", 'r')
line = fstream.readline()
while line:
  listCoords.append(line.replace(" \n", "").replace("\n", "").split(" "))
  line = fstream.readline()
fstream.close()
Coords = []
for coord in listCoords:
  Coords.append(city(coord[0], [float(coord[1]), float(coord[2])]))


def second(elem):
  return elem[1]


def bfs(s, g):
  if s == g:
    for i in range(len(close) - 1):
      print("%s -> " % close[i], end='')
    print(close[len(close) - 1])

    y = input("Do you want to try again? (Y/N):")
    if y == "Y":
      close.clear()
      open.clear()
      start = ""
      goal = ""
      while start not in adjacencies.keys():
        start = input("What is your starting city?\n->").replace(" ", "_")
        if start not in adjacencies.keys():
          print("Try Again")
      close.append(start)
      while goal not in adjacencies.keys():
        goal = input("What is your goal city?\n->").replace(" ", "_")
        if goal not in adjacencies.keys():
          print("Try Again")
      bfs(start, goal)
    return close
  for target in adjacencies.keys():
    if s in target:
      for coord in Coords:
        if g == coord.name:
          mainCoord = coord.coords
          for i in adjacencies[target]:
            for coord in Coords:
              if i == coord.name:
                distance = math.dist(mainCoord, coord.coords)
                open.append([coord.name, distance])
                if coord.name in close:
                  open.pop()

          open.sort(reverse=True, key=second)
  print("\nCities Adjacent to {}:".format(s))
  for i in range(0, len(open) - 1):
    print("{:15} {:.5f}".format(open[i][0], open[i][1]))
  print("{:15} {:.5f} Closest Adjacent City from {} to {}".format(
    open[len(open) - 1][0], open[len(open) - 1][1], s, g))

  print("")
  close.append(open.pop()[0])
  bfs(close[len(close) - 1], g)


print("Cities [and their adjacent cities]:")
for i in adjacencies:
  print("{:15} {}".format(i, adjacencies[i]))
print("")
close = []
open = []
start = ""
goal = ""
while start not in adjacencies.keys():
  start = input("What is your starting city?\n->").replace(" ", "_")
  if start not in adjacencies.keys():
    print("Try Again")
close = [start]
while goal not in adjacencies.keys():
  goal = input("What is your goal city?\n->").replace(" ", "_")
  if start not in adjacencies.keys():
    print("Try Again")
bfs(start, goal)
