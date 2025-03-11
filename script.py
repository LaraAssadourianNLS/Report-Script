import pandas as pd
import numpy as np
file = open("Student 1.txt", "r")
weekDaysMapping = ["Monday", "Tuesday", 
                   "Wednesday", "Thursday",
                   "Friday", "Saturday",
                   "Sunday"]
lines = file.readlines()

day_indexes = [len(lines)]
names = []
for days in weekDaysMapping:
    for i in range(len(lines)):
        if days in lines[i]:
            name = lines[i+1].strip().split(',')
            day_indexes.append(i)
            for j in name:
                names.append(j.strip())
day_indexes = sorted(day_indexes)

name_indexes = []
for i in names:
    if len(i.strip()) > 1:
        for j in range(len(lines)):
            if lines[j].strip() == i.strip():
                name_indexes.append(j)
name_indexes=sorted(list(dict.fromkeys(name_indexes)))

days_class={}
for i in range(1, len(day_indexes)):
    ind = []
    for j in name_indexes:
        if j > day_indexes[i-1] and j < day_indexes[i]:
            ind.append(j)
    ind.append(day_indexes[i])
    days_class[lines[day_indexes[i-1]].strip()] = ind

student_info={}
for i in days_class.keys():
    indx = days_class[i]
    info = {}
    for j in range(1, len(indx)):
        info[lines[indx[j-1]].strip()] = lines[indx[j-1]+1:indx[j]]
    student_info[i] = info

for i in student_info.keys():
    for j in student_info[i].keys():
        text = ''
        for k in student_info[i][j]:
            text = text + k.strip() + r' \newline '
        student_info[i][j] = text

##########################################

from latex_document_reader import LaTeXDocumentReader
document_reader = LaTeXDocumentReader('template_mine.tex')

# Read the LaTeX document
content = document_reader.read_document()
new_string = "\draw (10, -11) node[font=\\fontsize{52}{58}\sffamily\\bfseries]{TEXT};\n \end{tikzpicture}\n\n \hspace{7cm}\n \\begin{minipage}{0.7\\textwidth}\n \\vspace*{20cm}\n\n \\fontsize{30}{30}\n \selectfont\n DESC \n \end{minipage}\n \end{document}"
for i in student_info.keys():
    for j in student_info[i]:
        text_rep = new_string.replace('TEXT', j)
        text_rep = text_rep.replace('DESC', student_info[i][j])
        new = content + text_rep
        f = open(j+'_'+i +'.tex', 'w')
        f.write(new)
        f.close()

new = content + text_rep

result = [ new]
filename = [ 'res1']
for (res, name) in zip(result, filename):
   f = open(name +'.tex', 'w')
   f.write(res)
   f.close()