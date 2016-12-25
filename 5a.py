import fileinput

def naughty_or_nice(s):
  vowels = 0
  doubles = False
  last = None
  for l in s:
    if l in list('aeiou'):
      vowels += 1
    if last == 'a' and l == 'b':
      return 'naughty'
    elif last == 'c' and l == 'd':
      return 'naughty'
    elif last == 'p' and l == 'q':
      return 'naughty'
    elif last == 'x' and l == 'y':
      return 'naughty'
    if last == l:
      doubles = True
    last = l

  if vowels >= 3 and doubles:
    return 'nice'
  else:
    return 'naughty'


assert naughty_or_nice('aaa') == 'nice'
assert naughty_or_nice('jchzalrnumimnmhp') == 'naughty'
assert naughty_or_nice('haegwjzuvuyypxyu') == 'naughty'
assert naughty_or_nice('dvszwmarrgswjxmb') == 'naughty'
assert naughty_or_nice('dvszwmarrgswjxmbei') == 'nice'

naughty = 0
nice = 0
for s in fileinput.input():
  status = naughty_or_nice(s)
  if status  == 'naughty':
    naughty += 1
  elif status == 'nice':
    nice += 1
  else:
    raise ValueError('String was not naughty or nice')

print('naughty %s  nice %s' % (naughty, nice))

