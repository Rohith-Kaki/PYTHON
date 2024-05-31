class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
    def add_Employee(self, employe_details):
        new_node = Node(employe_details)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display_employes(self):
        current = self.head
        while current:
            print("Name:", current.data['name'])
            print("ID:", current.data['id'])
            print("salary:", current.data['salary'])
            print()
            current = current.next
    def calculate_average_salary(self):
        total_salary = 0
        total_employes = 0
        current = self.head
        while current:
            total_salary += float(current.data['salary'])
            total_employes += 1
            current = current.next
        if total_salary == 0:
            return 0
        else:
            return total_salary/total_employes
        
#main program
employe_list = Linkedlist()
while True:
    print("1. employe name")
    print("2. list of employe")
    print("3. Calcultae avg salary")
    print("4. Exit")
    choice = input("Enter your choice:")
    if choice == '1':
        employe_name = input("enter employe name: ")
        employe_id =  input("enetr employe ID: ")
        employe_salary =  input("enetr employe salary: ")
        employe_details = {'name':employe_name,'id':employe_id, 'salary':employe_salary}
        employe_list.add_Employee(employe_details)
        print("Student added successfully\n")
    elif choice == '2':
        print("List of employees:")
        employe_list.display_employes()
    elif choice == '3':
        average_salary = employe_list.calculate_average_salary()
        print("average salary :", average_salary )
    elif choice =='4':
        print("exit program")
        break
    else:
        print("Invalid choice, enter an option")