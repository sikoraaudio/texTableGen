
import numpy as np
import csv
import os

filename = 'table1'

# read in transition matrix from csv
reader = csv.reader(open(filename + '.csv', "r"), delimiter=',')
x = list(reader)
table_array = np.array(x)
cols = table_array.shape[1]-1
rows = table_array.shape[0]

table_title = ''
for i in range(0, cols):
    table_title += (table_array[1][i] + ' &')
table_title += ' \\\\ [0.5ex] \n'

table_content = ''
for i in range(2, rows-1):
    for j in range(0, cols):
        table_content += (table_array[i][j] + ' &')
    table_content += ' \\\\ [0.5ex] \n'

with open(filename + '.tex', 'w') as f_out:
    f_out.write('\\begin{table} [ht] % \n'
                '\\centering % used for centering table % \n'
                '\\caption{' + table_array[0][1] + '} % title of Table % \n'
                '\\vspace{0.5cm} % \n'
                '\\begin{tabular}{|' + 'c|' * cols + ''
                '} % centered columns (4 columns) % \n'
                '\\hline \n')
    f_out.write(table_title)
    f_out.write('\\hline \n')
    f_out.write(table_content)
    f_out.write('[1ex] % [1ex] adds vertical space % \n'
                '\hline %inserts single line % \n'
                '\end{tabular} % \n'
                '\label{table:' + table_array[1][cols] + '} % is used to refer this table in the text % \n'
                '\end{table} % \n')

    os.system("pdflatex ../main.tex")