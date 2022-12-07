import re
from docx import Document
from datetime import datetime

name = input("ФИО: ")
n = input("№ договора: ")
address = input("Адрес: ")
tel = input("Телефон: ")
NameDoc = input("Введите имя выходного документа: ")

def docx_replace_regex(doc_obj, regex , replace):

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


filename = "Шаблон 1.docx"
doc = Document(filename)

regex1 = re.compile(r"номер")
d = datetime.today().strftime('%d%m%y')
replace1 = d + n
docx_replace_regex(doc, regex1, replace1)

regex1 = re.compile(r"дата 1")
day = datetime.today().strftime('%d')
month = datetime.today().strftime('%m')
dic = {'01': " января", '02': " февраля", '03': " марта", '04': " апреля", '05': " мая", '06': " июня", '07': " июля", '08': " августа", '09': " сентября", '10': " октября", '11': " ноября", '12': " декабря"}
m = dic[month]
replace1 = day + m
docx_replace_regex(doc, regex1, replace1)

regex1 = re.compile(r"ФИО")
replace1 = name
docx_replace_regex(doc, regex1, replace1)

regex1 = re.compile(r"имя")
f, i, i2 = (name.split(' '))
l = len(name)
replace1 = i[0] + '. ' + i2[0] + '. ' + f
docx_replace_regex(doc, regex1, replace1)

regex1 = re.compile(r"адрес")
replace1 = address
docx_replace_regex(doc, regex1, replace1)

regex1 = re.compile(r"телефон")
replace1 = tel
docx_replace_regex(doc, regex1, replace1)

doc.save(NameDoc + '.docx')
