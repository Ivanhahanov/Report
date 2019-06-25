import random
from fpdf import FPDF
import json

class Task:
    task_name = 'Default task'
    task_group = 0
    task_weight = task_group
    deadline = False
    difficult = 0
    visit = 0
    indepentdent = 0
    description = 'Description'

class Person:

    name = 'Name'
    surname = "Surname"
    patronymic = "Patronymic"
    tasks = [] #list of tasks


    def personal_skills(self):
        return self.weights[0] * self.num_of_tasks + \
               self.weights[1] * self.deadlines + \
               self.weights[2] * self.brought_projects + \
               self.weights[3] * self.difficulty

    def company_skills(self):
        return self.weights[4] * self.visits + \
               self.weights[5] * self.independence

    def get_mark(self):

        personal_skills = self.personal_skills()
        company_skills = self.company_skills()
        return personal_skills + company_skills

    def doc(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Report", ln=1, align="C")
        pdf.cell(200, 10, txt="Name: %s"%self.name, ln=1, align="C")
        pdf.cell(200, 10, txt="Mark: %s"%self.get_mark(), ln=1, align="C")

        pdf.output("%s.pdf"%self.name)
        return self.name, self.get_mark()

    def create_json(self):
        data = {
            'name': self.name,
            'mark': self.get_mark()
        }
        return data

    def save_json(self, data):
        with open("info.json", 'w') as write_file:
            json.dump(data, write_file)

def get_best(data):
    best_staff = max(data, key=data.get)
    best_mark = data[best_staff]
    return best_staff, best_mark


def get_worse(data):
    worse_staff = min(data, key=data.get)
    worse_mark = data[worse_staff]
    return worse_staff, worse_mark




def main(persons):
    result = {}
    for person in persons:
        p = Person()
        p.name = person
        p.num_of_tasks = random.randint(1, 5)
        p.deadlines = random.randint(1, 5)
        p.difficulty = random.randint(1, 5)
        p.brought_projects = random.randint(1, 3)
        p.visits = random.randint(1, 5)
        p.independence = random.randint(1, 5)
        name, document = p.doc()
        print(name)
        print('\t', '[Personal]',
              'Complete tasks:', p.num_of_tasks,
              'Deadlines:', p.deadlines,
              'Difficulty of task:', p.difficulty,
              'Brought projects:', p.brought_projects)
        print('\t', '[Personal]', 'Mark:', p.personal_skills())
        print('\t', '[Company]', 'Visits:', p.visits,
              'Independence:', p.independence)
        print('\t', '[Company]', 'Mark:', p.company_skills())
        print('\t', 'Mark:', document)
        result[name] = document
    best_name, best_mark = get_best(result)
    worse_name, worse_mark = get_worse(result)
    print('Best:', best_name, best_mark)
    print('Worse:', worse_name, worse_mark)


if __name__ == '__main__':
    staff = ['Ivan', 'Natali', 'Vlad', 'Stas', 'Vlada', 'Sveta', 'Sergey']
    main(staff)
