num_list = [1,2,3,4,5,6,7]

def random_function(num_list):
  total = 0
  all_integer = 0

  for num in num_list:
    print(num)

  for num1 in num_list:
    for num2 in num_list:
      print(f"{num1} - {num2}")
      total += 1

  msg = "Rule 5 - Remove all non-dominants"

  return total

print(random_function(num_list))