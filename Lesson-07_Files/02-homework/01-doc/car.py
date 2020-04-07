import datetime


from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage


def get_context(car_list):
    return {
        'brand': car_list[0],
        'model': car_list[1],
        'consumption': car_list[2],
        'price': car_list[3],
    }


def from_template(car_list, template):
    template = DocxTemplate(template)
    context = get_context(car_list)
    template.render(context)
    template.save(car_list[0] + '_' + str(datetime.datetime.now().date()) + '_report.docx')


def generate_report(car_list):
    template = 'report.docx'
    from_template(car_list, template)


car_list = ['Toyota', 'Camry', '8л/100км', '1 500 000 руб']
generate_report(car_list)
