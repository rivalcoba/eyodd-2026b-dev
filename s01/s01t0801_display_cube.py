def display_cube(items, index):
  result = pow(items[index],3) # O(1)
  print(result)

items = [2,3,4,5,6,7,10,12]

display_cube(items, 0)