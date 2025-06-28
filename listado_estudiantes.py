# dictionary for storing students
students = {}

# Function to register a new student 1
def register_student():
    id_est = input("Ingrese el número de identificación del estudiante: ")
    if id_est in students:
        print("¡Este estudiante ya está registrado!")
        return
    
    name = input("Ingrese el nombre del estudiante: ")
    age = input("Ingrese la edad del estudiante: ")


    grades = []
    for i in range(4):  
        while True:
            try:
                grade = float(input(f"Ingrese la nota #{i + 1}: "))
                if 0 <= grade <= 5:# conditions for saving notes
                    grades.append(grade)
                    break
                else:
                    print("La nota debe estar entre 0 y 5.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

    students[id_est] = {
        "nombre": name,
        "edad": age,
        "notas": grade
    }


    print("Estudiante registrado con éxito.\n")

# Function to query a student 2
def query_student():
    
    id_est = input("Ingrese el número de identificación: ")
    student = students.get(id_est)
    
    if student:
        print(f"\nNombre: {student['nombre']}")
        print(f"Edad: {student['edad']}")
        print(f"Notas: {student['notas']}")
        Average = sum(student['notas']) / len(student['notas'])
        print(f"Promedio: {Average:.2f}\n")
    else:
        print("Estudiante no encontrado.\n")

#  Function to update grades 3
def  Update_grades():
    id_est = input("Ingrese el número de identificación: ")
    if id_est in students:
        new_grade = []
        for i in range(3):
            while True:
                try:
                    nota = float(input(f"Ingrese la nueva nota #{i + 1}: "))
                    if 0 <= nota <= 5:
                        new_grade.append(grade)
                        break
                    else:
                        print("La nota debe estar entre 0 y 5.")
                except ValueError:
                    print("Entrada inválida.")
        students[id_est]["notas"] = new_grade
        print("Notas actualizadas correctamente.\n")
    else:
        print("Estudiante no encontrado.\n")

# Function to delete student 4
def delete_student():
    id_est = input("Ingrese el número de identificación: ")
    if id_est in students:
        del students[id_est]
        print("Estudiante eliminado con éxito.\n")
    else:
        print("Estudiante no encontrado.\n")

# Function to view all students 5
def view_all():
    if not students:
        print("No hay estudiantes registrados.\n")
    else:
        for id_est, data in students.items():
            average = sum(data['notas']) / len(data['notas'])
            print(f"ID: {id_est}, Nombre: {data['nombre']}, Promedio: {average:.2f}")
        print()

# Menú principal
def menu():
    while True:
        print("===== MENÚ PRINCIPAL =====")
        print("1. Registrar estudiante")
        print("2. Consultar estudiante")
        print("3. Actualizar notas")
        print("4. Eliminar estudiante")
        print("5. Ver todos los estudiantes")
        print("6. Salir")

        option = input("Seleccione una opción: ")
        
        if option == "1":
            register_student()
        elif option == "2":
            check_student()
        elif option == "3":
            Update_grades()
        elif option == "4":
            delete_student()
        elif option == "5":
            view_all()
        elif option == "6":
            print("Gracias por usar el sistema.")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")

# Run the menu
menu()