import fileinput

def paper_for(x, y, z):
  length = 2*x*y
  width = 2*x*z
  breadth = 2*y*z
  small = min((length, width, breadth))
  return length + width + breadth + small/2

assert paper_for(2, 3, 4) == 58
assert paper_for(1, 1, 10) == 43

total = 0
for line in fileinput.input():
  x, y, z = [int(i) for i in line.split('x')]
  total += paper_for(x, y, z)
print(total)
