class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
    def add_student(self, student_details):
        new_node = Node(student_details)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def display_students(self):
        current = self.head
        while current:
            print("Name:", current.data['name'])
            print("ID:", current.data['id'])
            print("GPA:", current.data['gpa'])
            print()
            current = current.next
    def calculate_average_gpa(self):
        total_gpa = 0
        total_students = 0
        current = self.head
        while current:
            total_gpa += float(current.data['gpa'])
            total_students += 1
            current = current.next
        if total_students == 0:
            return 0
        else:
            return total_gpa/total_students
        
#main program
student_list = Linkedlist()
while True:
    print("1. Add Student")
    print("2. Display Students")
    print("3. Calcultae gpa")
    print("4. Exit")
    choice = input("Enter your choice:")
    if choice == '1':
        name = input("enter student name: ")
        student_id =  input("enetr student ID: ")
        gpa =  input("enter gpa: ") 
        student_details = {'name':name,'id':student_id,'gpa':gpa}
        student_list.add_student(student_details)
        print("Student added successfully\n")
    elif choice == '2':
        print("List of students:")
        student_list.display_students()
    elif choice == '3':
        average_gpa = student_list.calculate_average_gpa()
        print("average gpa :", average_gpa)
    elif choice =='4':
        print("exit program")
        break
    else:
        print("Invalid choice, enter an option")