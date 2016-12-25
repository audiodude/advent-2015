import sys

count = 0
i = sys.stdin.read(1)
while i != '':
  if i == '(':
    count += 1
  elif i == ')':
    count += -1
  i = sys.stdin.read(1)
print(count)
