# Creando una lista de estudiantes
student_list1 = ["Pablo","Felipe","Natanael","Gamaliel","Mateo","Marcos","Lucas","Juan"] # O(1)

def random_function(students):
  first = students[0] # O(1)
  total = 0 # O(1)
  new_list = [] # O(1)

  for student in students:
    total += 1 #O(n)
    new_list.append(student) #O(n)

  print(new_list) # O(1)
  return total # O(1)

print(random_function(student_list1)) # O(6 + 2n)