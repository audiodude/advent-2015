import fileinput

def ribbon_for(x, y, z):
  l = [x, y, z]
  small_1 = min(l)
  l.remove(small_1)
  small_2 = min(l)

  return 2*small_1 + 2*small_2 + x*y*z

assert ribbon_for(2, 3, 4) == 34
assert ribbon_for(1, 1, 10) == 14

total = 0
for line in fileinput.input():
  x, y, z = [int(i) for i in line.split('x')]
  total += ribbon_for(x, y, z)
print(total)
