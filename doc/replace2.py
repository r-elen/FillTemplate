import re
from docx import Document
from datetime import datetime


SERVICES = ["Анализ нормативно-правовой базы и формирование правовой позиции", "Составление проекта",
             "3", "4", "5", "6",]


def create_num(number: str) -> str:
    d = datetime.today().strftime('%d%m%y')
    return ''.join([d, number])


def create_date():
    dd = datetime.today().strftime('%d')
    yyyy = datetime.today().strftime('%Y')

    month = datetime.today().strftime('%m')
    dic = {'01': "января", '02': "февраля", '03': "марта", '04': "апреля", '05': "мая", '06': "июня", '07': "июля", '08': "августа", '09': "сентября", '10': "октября", '11': "ноября", '12': "декабря"}
    mm = dic[month]

    return ' '.join([dd, mm, yyyy])


def create_full_name(last_name: str, name: str, middle_name=None):
    if len(middle_name) == 0:
        full_name = ' '.join([last_name, name])
    else:
        full_name = ' '.join([last_name, name, middle_name])
    return full_name


def create_initials(last_name: str, name: str, middle_name=None):
    """
    :param last_name: last name
    :param name: first name
    :param middle_name: middle name
    :return: None
    """
    if len(middle_name) == 0:
        name_initials = '.'.join([name[0], last_name])
    else:
        name_initials = '.'.join([name[0], middle_name[0], last_name])
    return name_initials


def docx_replace_regex(doc_obj, regex, replace):

    for p in doc_obj.paragraphs:
        if regex.search(p.text):
            inline = p.runs
            # Loop added to work with runs (strings with same style)
            for i in range(len(inline)):
                if regex.search(inline[i].text):
                    text = regex.sub(replace, inline[i].text)
                    inline[i].text = text

    for table in doc_obj.tables:
        for row in table.rows:
            for cell in row.cells:
                docx_replace_regex(cell, regex, replace)


def repl_template(templ_name: str, file_name: str, temps: list, info: list):
    open_doc = Document(templ_name)
    dict_ = {key: value for key, value in zip(temps, info)}
    for template, info in dict_.items():
        print(str(template) + '->' + info)
        docx_replace_regex(open_doc, template, info)
    open_doc.save(file_name + '.docx')


def create_template_list():
    tmp_num_doc = re.compile(r"{(\w+)}")
    tmp_date_1 = re.compile(r"date")
    tmp_client_name = re.compile(r"fullname")
    tmp_address = re.compile(r"address")
    tmp_initials = re.compile(r"initials")
    tmp_tel = re.compile(r"tel")

    list_templates = [tmp_num_doc, tmp_date_1, tmp_client_name, tmp_address, tmp_initials, tmp_tel]

    return list_templates


def input_info():
    doc_num = create_num(input("№ договора: "))
    date_1 = create_date()
    client_lastname = input("Фамилия: ")
    client_name = input("Имя: ")
    client_middname = input("Отчество: ")
    client_full_name = create_full_name(client_lastname, client_name, client_middname)
    initials = create_initials(client_lastname, client_name, client_middname)
    address = input("Адрес: ")
    tel = input("Тел.: ")

    list_info = [doc_num, date_1, client_full_name, address, initials, tel]
    return list_info


def get_services(services = SERVICES) -> list:
    """
    Получение случайного списка имён

    :param count: длина списка
    :return: список с именами
    """

    return services


def main():

    list_temps = create_template_list()
    list_info = input_info()

    tmp_doc = "Шаблон 1.docx"
    name_save_doc = ' '.join(['Договор', list_info[0]])
    repl_template(tmp_doc, name_save_doc, list_temps, list_info)


if __name__ == '__main__':
    main()






