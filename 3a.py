import sys


map = {}
x = 0
y = 0
map[(x, y)] = True
i = sys.stdin.read(1)
while i != '':
  if i == '^':
    y += 1
  elif i == '>':
    x += 1
  elif i == 'v':
    y += -1
  elif i == '<':
    x += -1
  map[(x, y)] = True
  i = sys.stdin.read(1)

print(len(map.keys()))
