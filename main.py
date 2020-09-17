# Author: Liam Hooks lrh5428@psu.edu
# Collaborator: Jacob Henderson jrh6433@psu.edu
# Collaborator: Hunter Fristick hjf5143@psu.edu
# Collaborator: John Sweetall jts6052@psu.edu
# Section: 2
# Breakout: 4

def sum_n(n):
  if n == 0:
    return 0
  else:
    return(int(sum_n(n-1) + n))
  

def print_n(s, n):
  if n != 0:
    print(s)
    print_n(s, n - 1)

def run():
  num = int(input("Enter an int: "))
  print("sum is " + str(sum_n(num)) + ".")
    
  thing = input("Enter a string: ")
  print_n(thing, num)

if __name__ == "__main__":
  run()