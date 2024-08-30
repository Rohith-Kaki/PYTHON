class Node:
    def __init__(self, name, roll_num, marks):
        self.name = name
        self.roll_num = roll_num
        self.marks = marks
        self.next = None

class LinkedList:
    def add_student(self, name, roll_num, marks):
        new_student = Node(name, roll_num, marks)
        new_student.next = self.head
        self.head = new_student
    
    def __init__(self):
        self.head = None
    
    
    def display_students(self):
        current = self.head
        while current:
            print(f"Name: {current.name}, Roll Num: {current.roll_num}, Marks: {current.marks}")
            current = current.next
    
    def calculate_gpa(self):
        total_marks = 0
        total_students = 0
        current = self.head
        while current:
            total_marks += current.marks
            total_students += 1
            current = current.next
        if total_students == 0:
            return 0  # Avoid division by zero
        average_marks = total_marks / total_students
        # GPA calculation logic (you can customize this based on your grading system)
        if average_marks >= 90:
            return 'A'
        elif 80 <= average_marks < 90:
            return 'B'
        elif 70 <= average_marks < 80:
            return 'C'
        elif 60 <= average_marks < 70:
            return 'D'
        else:
            return 'F'

# Example usage:
if __name__ == "__main__":
    student_list = LinkedList()
    # Add students to the linked list
    student_list.add_student("Alice", "A001", 85)
    student_list.add_student("Bob", "A002", 99)
    # Display the list of students
    print("List of Students:")
    student_list.display_students()
    # Calculate and display GPA
    gpa = student_list.calculate_gpa()
    print(f"\nCalculated GPA: {gpa}")