num_list = [1,2,3,4,5,6,7]
num_list01 = [10,20,30]

def random_function(num_list):
  total = 0
  for num1 in num_list:
    for num2 in num_list01:
      print(f"{num1} - {num2}")
      total += 1

  return total

print(random_function(num_list))