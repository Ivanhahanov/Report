import random
from fpdf import FPDF
import json
class Task:

    task_name = 'Default task'
    task_group = 'group'
    task_weight = 0
    deadline = False
    difficult = 0
    visit = 0
    independent = 0
    description = 'Description'

class Person:

    name = 'Name'
    surname = "Surname"
    patronymic = "Patronymic"
    tasks = [] #list of tasks
    result = 0

    def personal_skills(self):
        return self.weights[0] * self.num_of_tasks + \
               self.weights[1] * self.deadlines + \
               self.weights[2] * self.brought_projects + \
               self.weights[3] * self.difficulty

    def company_skills(self):
        return self.weights[4] * self.visits + \
               self.weights[5] * self.independence

    def calc(self):
        for task in self.tasks:
            res = task['difficult'] + task['visits'] + task['independent']
            res = res * task['task_weight']
            self.result += res

    def get_mark(self):

        personal_skills = self.personal_skills()
        company_skills = self.company_skills()
        return personal_skills + company_skills

    def doc(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Report", ln=1, align="C")
        pdf.cell(200, 10, txt="Surname: %s"%self.surname, ln=1, align="L")
        pdf.cell(200, 10, txt="Name: %s"%self.name, ln=1, align="L")
        pdf.cell(200, 10, txt="Patronymic: %s"%self.patronymic, ln=1, align="L")
        pdf.cell(200, 10, txt="Mark: %s"%self.result, ln=1, align="L")
        pdf.cell(200, 10, txt="Number of tasks: %s"%len(self.tasks), ln=1, align="L")

        user_tasks = self.tasks
        for task in user_tasks:
            pdf.cell(200, 10, txt="Name of task: %s"%task['task_name'], ln=1, align="L")
            pdf.cell(200, 10, txt="Description: %s"%task['description'], ln=1, align="L")
            pdf.cell(200, 10, txt="Deadline: %s"%task['deadline'], ln=1, align="L")
            pdf.cell(200, 10, txt="Visits: %s"%task['visits'], ln=1, align="L")
            pdf.cell(200, 10, txt="Independent: %s"%task['independent'], ln=1, align="L")


        pdf.output("pdf/%s.pdf"%self.name)
        return self.name



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
