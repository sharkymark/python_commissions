def plantype(args):

  # commission plan

  # fixedrate or varrate or leveraged
  pt = args[0]
  # revenue 115000
  r = args[1]
  # variable compensation 100000
  v = args[2]
  # quota 500000
  q = args[3]  
  # quota attained so far 0
  a = args[4]

  if pt == "fixedrate":
    rt = float(input(f"entered commission rate: "))
    print("what you typed: " + str(rt))
    commission,rt = fixedrate(r,rt)

  if pt == "varrate":  
    commission,rt = varrate(q, v, r)

  if pt == "leveraged":
    commission,rt = leveraged(q, v, r)

  inputs(pt,r,v,q,a)

  print('\n** Commission Calculations **')
  print("commission: $" + str(commission))
  print('rate (or attainment): ' + str(rt*100) + "%")

def inputs(pt,r,v,q,a):
  print('\n** Input & References Variables **')
  print('plan type: ' + pt)
  print('revenue: $' + r)
  print('variable compensation: $' + v)
  print('quota: $' + q)
  print('quota attained before this revenue: $' + a)

def fixedrate(r,rt):
  rt = float(rt)/100
  r = float(r)  
  return r*rt, rt

def varrate(q,v,r):
  q = float(q)
  v = float(v)
  r = float(r)
  rate = v / q
  return rate * r, rate

def leveraged(q,v,r):
  q = float(q)
  v = float(v)
  r = float(r)
  attain = r / q
  return v*attain, attain

