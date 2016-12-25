import sys


map_santa = {}
santa_x = 0
santa_y = 0
map_santa[(santa_x, santa_y)] = True

map_robo = {}
robo_x = 0
robo_y = 0
map_robo[(robo_x, robo_y)] = True
while True:
  i = sys.stdin.read(1)
  if i == '':
    break
  elif i == '^':
    santa_y += 1
  elif i == '>':
    santa_x += 1
  elif i == 'v':
    santa_y += -1
  elif i == '<':
    santa_x += -1
  map_santa[(santa_x, santa_y)] = True

  i = sys.stdin.read(1)
  if i == '':
    break
  elif i == '^':
    robo_y += 1
  elif i == '>':
    robo_x += 1
  elif i == 'v':
    robo_y += -1
  elif i == '<':
    robo_x += -1
  map_robo[(robo_x, robo_y)] = True

print(len(set(map_santa.keys()) | set(map_robo.keys())))
