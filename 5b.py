import fileinput
from collections import defaultdict

def naughty_or_nice(s):
  sandwich = False
  twice = False
  twice_prospects = defaultdict(int)
  triplets = defaultdict(int)
  back_1 = None
  back_2 = None
  for l in s:
    if back_1 == back_2 and back_1 == l:
      triplets[back_2 + back_1 + l] += 1
    if back_1:
      twice_prospects[back_1 + l] += 1
    if back_2 == l:
      sandwich = True
    back_2 = back_1
    back_1 = l
    
  for k, v in triplets.items():
    if v > 1:
      twice = True
      break

  if not twice:
    for k, v in twice_prospects.items():
      if k[0] == k[1] and (k[0] + k[0] + k[0]) in triplets:
        v -= 1
      if v >= 2:
        twice = True
        break

  if sandwich and twice:
    return 'nice'
  else:
    return 'naughty'


assert naughty_or_nice('aaa') == 'naughty'
assert naughty_or_nice('aaaa') == 'nice'
assert naughty_or_nice('xxyxx') == 'nice'
assert naughty_or_nice('uurcxstgmygtbstg') == 'naughty'
assert naughty_or_nice('ieodomkazucvgmuy') == 'naughty'
assert naughty_or_nice('ieodomkazzucvgmzzuy') == 'nice'
assert naughty_or_nice('aaayaaa') == 'nice'
assert naughty_or_nice('zaaayaaa') == 'nice'
assert naughty_or_nice('aaayaa') == 'nice'

naughty = 0
nice = 0
for s in fileinput.input():
  status = naughty_or_nice(s.strip())
  if status == 'naughty':
    naughty += 1
  elif status == 'nice':
    nice += 1
  else:
    raise ValueError('String was not naughty or nice')


print('naughty %s  nice %s' % (naughty, nice))

