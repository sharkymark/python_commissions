def plantype(args, default_fixed_rate=None):

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
    # Use default rate if provided, otherwise prompt the user
    if default_fixed_rate is not None:
        default_prompt = f"Enter commission rate (percentage) [{default_fixed_rate}%]: "
        user_input = input(default_prompt)
        if user_input.strip() == "":
            rt = default_fixed_rate
        else:
            try:
                rt = float(user_input)
            except ValueError:
                print("Invalid input, using default rate.")
                rt = default_fixed_rate
    else:
        rt = float(input("Enter commission rate (percentage): "))
    
    rt = rt / 100  # Convert percentage to decimal
    commission = float(r) * rt
    
  if pt == "varrate":  
    commission, rt = varrate(q, v, r)

  if pt == "leveraged":
    commission, rt = leveraged(q, v, r)

  inputs(pt,r,v,q,a)

  print('\n** Commission Calculations **')
  print(f"commission: ${commission:.2f}")
  print(f'rate (or attainment): {rt*100:.2f}%')

def inputs(pt,r,v,q,a):
  print('\n** Input & References Variables **')
  print('plan type: ' + pt)
  print(f'revenue: ${float(r):.2f}')
  print(f'variable compensation: ${float(v):.2f}')
  print(f'quota: ${float(q):.2f}')
  print(f'quota attained before this revenue: ${float(a):.2f}')

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

