# -*- coding: utf-8 -*-

import datetime
import csv
from docxtpl import DocxTemplate
import json

car_data = [['brand', 'model', 'consumption', 'price'], ['Toyota', 'Camry', '8l/100km', '1 500 000 rubles.']]


def get_context(car_list):
    return {
        car_list[0][0]: car_list[1][0],
        car_list[0][1]: car_list[1][1],
        car_list[0][2]: car_list[1][2],
        car_list[0][3]: car_list[1][3]
    }


data_obj = get_context(car_data)


def from_template(data, template):
    template = DocxTemplate(template)
    template.render(data)
    template.save(str(datetime.datetime.now().date()) + '_report.docx')


def generate_report(data):
    template = 'report.docx'
    from_template(data, template)


generate_report(data_obj)


#  Записываем в csv
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(car_data)


#  Записываем в json
dict_to_json = json.dumps(data_obj)

with open('data.json', 'w') as f:
    json.dump(dict_to_json, f)


