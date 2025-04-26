# -*- coding: utf-8 -*-

import numpy as np

# Q1 
print('_____________Q1_____________')
a = 'The rain in Spain' 
b = a.upper() 
print(b)
print(a)
print(b.isupper())
print(a.count('n'))

#Q2.a
print('_____________Q2a_____________')
month_num = np.arange(120)
moly_salary = np.zeros(np.shape(month_num), dtype = 'f') + 3000

print("month_num: ", month_num)
print("moly_salary: ", moly_salary)

for imo in range(np.size(moly_salary)):
 	if imo == 0:
         moly_salary[imo] = 3000
 	elif month_num[imo] % 12 == 0:
		 moly_salary[imo] = moly_salary[imo -1] * 1.03
 	else:
		 moly_salary[imo] = moly_salary[imo -1]

print("\n\n\nmoly_salary after for loop: ", moly_salary)
print("\n\ntotal of moly salary for 10 years " + str(np.sum(moly_salary)))

#Q2.b
print('_____________Q2b_____________')
file_name = 'file moly_salary_one_col.txt'
file_obj= open(file_name, 'w')
for imo in range(np.size(moly_salary)):
    file_obj.write(str(moly_salary[imo]) + '\n')
file_obj.close()
    
#Q2.c
print('_____________Q2c_____________')
file_obj = open(file_name, 'r')
data = file_obj.readlines()
file_obj.close()
print(data)
print(len(data))

data_in = np.zeros(len(data), dtype = 'f')
for imo in range (len(data)):
    data_in[imo] = float(data[imo])
print("Comparing moly salary and file" + str(np.allclose(moly_salary, data_in)))


#3
print('_____________Q3_____________')
file_name = 'SingleColumnData.txt'
file_obj= open(file_name, 'w')

for imo in range (np.size(moly_salary)):
    file_obj.write(str(month_num[imo] + 1) + '\t' + str(moly_salary[imo]) + '\n')
file_obj.close()


file_obj = open(file_name, 'r')
data = file_obj.readlines()
file_obj.close()
print(data)


#4
print('_____________Q4_____________')
file_name = 'TwoColumnData.txt'

file_obj = open(file_name, 'w')
file_obj.write('Column1\tColumn2\n')
for i in range(5):  # Example data
    file_obj.write(str(i + 1) + '\t' + str((i + 1) * 10) + '\n')
file_obj.close()

file_obj = open(file_name, 'r')
data = file_obj.readlines()[1:]
file_obj.close()
print(data)
array_data = []
for line in data:
    values = line.split('\t')
    array_data.append([int(values[0]), int(values[1])])

array_data = np.array(array_data)

column_sum = array_data[:, 0] + array_data[:, 1]

print(column_sum)

#5
print('_____________Q5_____________')
file_name = 'FourColumnData.txt'
file_obj = open(file_name, 'r')
data = file_obj.readlines()
file_obj.close()
data_2d = []

for line in data:
    cols = line.split()
    data_2d.append([float(col) for col in cols])

column_sums = [0, 0, 0, 0]

for row in data_2d:
    for i in range(4):
        column_sums[i] += row[i]
print(column_sums)
