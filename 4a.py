import hashlib

KEY = 'iwrupvqb'

i = 0
while True:
  data = (KEY + str(i)).encode('utf-8')
  m = hashlib.md5(data).hexdigest()
  if m.startswith('00000'):
    print(m, i)
    break
  elif i % 1000 == 0:
    print('...%s' % i)
  i += 1
