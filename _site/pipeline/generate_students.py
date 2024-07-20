import csv
# from models.student import Student

# - name:
#  photo: rock.jpg
#  info:
#  email:
#  number_educ:
#  education1:
#  education2:
#  education3:
#  education4:


class Student:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.info = ""
        self.photo = ""
        self.number_educ = 0
        self.education = []
        self.is_alumni = False

    def set_info(self, info):
        self.info = info

    def set_photo(self, photo):
        self.photo = photo

    def add_education(self, education):
        if self.number_educ == 5:
            return
        if education == "":
            return
        self.education.append(education)
        self.number_educ += 1

    def set_alumni(self):
        self.is_alumni = True

    def to_yml(self):
        student_str = f"- name: {self.name}\n"
        student_str += f"  photo: {self.photo}\n"
        student_str += f"  info: {self.info}\n"
        student_str += f"  email: {self.email}\n"
        student_str += f"  number_educ: {self.number_educ}\n"
        for i in range(self.number_educ):
            student_str += f"  education{i+1}: {self.education[i]}\n"
        student_str += f"  alumni: {self.is_alumni}\n"
        return student_str

        

def read_students():
    with open('students.csv', 'r') as f:
        reader = csv.DictReader(f)
        students = [row for row in reader]
    return students


student_list = []


def generate_students():
    students = read_students()
    for student in students:
        stud = Student(student['Name'], student['Email'])
        stud.set_info(student['Designation'])
        stud.set_photo("")
        stud.add_education(student['Achievements1'])
        stud.add_education(student['Achievements2'])
        stud.add_education(student['Achievements3'])
        stud.add_education(student['Achievements4'])
        stud.add_education(student['Achievements5'])
        if student['Alumni'] == 'true':
            stud.set_alumni()

        student_list.append(stud)


generate_students()


file = open('students.yml', 'w')
for student in student_list:
    # print to file
    file.write(student.to_yml())
    file.write("\n")

file.close() 
    