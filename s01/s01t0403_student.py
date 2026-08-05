# Creando una lista de estudiantes
student_list1 = ["Mateo","Marcos","Lucas","Juan"]
student_list2 = ["Pablo","Felipe","Natanael","Gamaliel"]

# Verificando presencia de estudiante
def check_stutend(student_input, stundet_list):
  for student in stundet_list:
    if student == student_input:
      print("Estudiante disponible")

# Consumo de la funcion
check_stutend("Juan", student_list1)