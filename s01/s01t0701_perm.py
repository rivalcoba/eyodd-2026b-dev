import itertools

num_list = [1,2,3,4]

def all_permutations(num_list):
  total = 0
  for p in itertools.permutations(num_list):
    print(p)
    total += 1
  return total

print(all_permutations(num_list))