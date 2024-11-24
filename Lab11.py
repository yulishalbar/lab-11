import matplotlib.pyplot as plt
import os

message = """1. Student grade
2. Assignment statistics
3. Assignment graph"""



def get_weight(assignment_id_in_submissions):
    with (open("data/assignments.txt", "r+") as assignments):
        line_numbers = 1
        found_id = False

        for t in assignments:
            t =t.strip()
            if found_id and line_numbers % 3 == 0:
                weight = t
                return int(weight)
            elif line_numbers % 3 == 2:
                assignment_id = t
                if assignment_id == assignment_id_in_submissions:
                    found_id = True
            line_numbers += 1

def assignment_grades(assignment_id):
    grade_list = []
    submissions_files = os.listdir("data/submissions")
    for file in submissions_files:
        file_path = os.path.join("data/submissions", file)
        with open(file_path, "r") as f:
            contents = f.read()

        submissions = contents.split("|")
        student_id_in_assignments = submissions[0]
        assignment_id_in_submissions = submissions[1]
        grade_value = int(submissions[2])
        if assignment_id_in_submissions == assignment_id:
            grade_list.append(grade_value)

    return grade_list

#print(assignment_grades("99909"))

def get_assignment_id_by_name(assignment_name):
    with (open("data/assignments.txt", "r+") as assignments):
        line_numbers = 1
        found = False

        for t in assignments:
            t =t.strip()
            if line_numbers % 1 == 0:
                name = t
                if name == assignment_name:
                    found = True
            if found and line_numbers % 3 == 2:
                assignment_id = t
                return assignment_id
            line_numbers += 1
    return None

#print(get_assignment_id_by_name("Quiz 2444"))

def get_student_grade(student_id):
    total_weight = 0
    grade = 0
    submissions_files = os.listdir("data/submissions")
    for file in submissions_files:
        file_path = os.path.join("data/submissions", file)
        with open(file_path, "r") as f:
            contents = f.read()

        submissions = contents.split("|")
        student_id_in_assignments = submissions[0]
        assignment_id_in_submissions = submissions[1]
        grade_value = int(submissions[2])

        if student_id_in_assignments == student_id:
            weight = get_weight(assignment_id_in_submissions)
            total_weight+=weight
            grade += (weight*grade_value)

    grade = grade / total_weight
    return round(grade)


def get_id(name):
    with open("data/students.txt", "r+") as students:
        for t in students:
            t = t.strip()
            student_name = t[3::]
            if name == student_name:
                student_id = t[0:3]
                return student_id

        return None

if __name__ == "__main__":
    print(message)
    choice = int(input("Enter your selection: "))

    if choice == 1:
        name = input("Enter the student's name: ")
        student_id = get_id(name)
        if student_id != None:
           student_grade = get_student_grade(student_id)
           print(f"{student_grade}%")

        else:
            print("Student not found")




    elif choice == 2:
        assignment_name = input("What is the assignment name: ")
        assignment_id = get_assignment_id_by_name(assignment_name)
        if assignment_id == None:
            print("Assignment not found")
        else:
            grades = assignment_grades(assignment_id)
            if len(grades) == 0:
                min = max = 0
            else:
                min = max  = grades[0]
            total = count = 0
            for grade in grades:
                if grade < min:
                    min = grade
                if grade > max:
                    max = grade
                total += grade
                count +=1
            avg = total / count
            print(f"Min: {round(min)}%")
            print(f"Avg: {round(avg)}%")
            print(f"Max: {round(max)}%")

    elif choice == 3:
        assignment_name = input("What is the assignment name: ")
        assignment_id = get_assignment_id_by_name(assignment_name)
        if assignment_id == None:
            print("Assignment not found")
        else:
            scores = assignment_grades(assignment_id)

            plt.hist(scores, bins=[0,10,20,30,40,50,60,70,80,90,100])
            plt.show()

            


