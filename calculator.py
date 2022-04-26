from replit import clear
def add(a,b):
  return a+b

def sub(c,d):
  return c-d

def mul(e,f):
  return e*f

def division(g,h):
  return g/h

calculator = {"+" : add,
              "-" : sub,
              "*": mul,
              "/": division}
def calculator_fun():
  n1 = float(input("What's the first number?: "))
  continue_or_not = True
  for symbol in calculator:
    print(symbol)
  while continue_or_not:
    operation_symbol =  input("Pick an operation: ")
    n2 = float(input("What's the next number?: "))
    f = calculator[operation_symbol]
    answer1 = f(n1,n2)
    print(f"{n1} {operation_symbol} {n2} = {answer1}")
    loop_iteration = input(f"Type 'y' to continue calculating with {answer1}, or type 'n' to start a new calculation: ")
    if loop_iteration == 'y':
      n1 = answer1
    else:
      continue_or_not = False
      clear()
      calculator_fun()
calculator_fun()   
