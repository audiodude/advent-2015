import sys

count = 0
pos = 0
i = sys.stdin.read(1)
while i != '':
  pos += 1
  if i == '(':
    count += 1
  elif i == ')':
    count += -1
  if count == -1:
    print(pos)
    break
  i = sys.stdin.read(1)
else:
  print('Basement never entered')
