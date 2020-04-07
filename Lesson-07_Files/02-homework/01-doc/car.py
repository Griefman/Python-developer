import datetime
import csv
from docxtpl import DocxTemplate


data_lst = []

with open('data.csv', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        data_lst.append(row)
headers_lst = data_lst[0]
vals_lst = data_lst[1]

data_obj = {}
for i in range(0, len(headers_lst)):
    data_obj[headers_lst[i]] = vals_lst[i]


def from_template(data, template):
    template = DocxTemplate(template)
    template.render(data)
    template.save(str(datetime.datetime.now().date()) + '_report.docx')


def generate_report(data):
    template = 'report.docx'
    from_template(data, template)


generate_report(data_obj)
