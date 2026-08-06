def all_cubes(items):
  result = []
  for item in items:
    result.append(pow(item,3))
  print(result)


items = range(1,6)
all_cubes(items)