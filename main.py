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
for i in adjacencies:
  print("%s %s" % (i, adjacencies[i]))

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


print("\n")


def bfs(s, g):
  if s == g:
    return close
  for target in adjacencies.keys():
    if s in target:
      # print("\n%s %s\n" % (target, adjacencies[target]))
      for coord in Coords:
        if g == coord.name:
          # print("%s %s" % (coord.name, coord.coords))
          mainCoord = coord.coords
          for i in adjacencies[target]:
            for coord in Coords:
              if i == coord.name:
                distance = math.dist(mainCoord, coord.coords)
                open.append([coord.name, distance])
                if coord.name in close:
                  open.pop()
                # print("%s %s %s" % (coord.name, coord.coords, distance))
          open.sort(reverse=True, key=second)
  print(s)
  for i in open:
    print("%s is %f away from %s" % (i[0], i[1], g))
  print("\n")

  close.append(open.pop()[0])
  if close[len(close) - 1] == s:
    close.insert(len(close) - 1, g)
    close.pop()
    return print(
      "%s had the closest distance to %s even through listed dependecies" %
      (s, g))
  bfs(close[len(close) - 1], g)


open = []
start = "Pratt"
close = [start]
goal = "Abilene"
bfs(start, goal)
for i in range(len(close)-1):
  print("%s -> " % close[i], end='')
print(close[len(close)-1])