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

        