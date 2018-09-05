import random
import xlrd

workbook_name = 'xxx.xls'
sheet_name = 'xxx'


workbook= xlrd.open_workbook(workbook_name)
table = workbook.sheet_by_name(sheet_name) 
order_list = table.col_values(0)[5:]
name_list = table.col_values(2)[5:]
num_list = table.col_values(3)[5:]
choice_list = []


def choice_student():
	times = 1
	while True:
		for i in zip(order_list,name_list, num_list):
			if i[2] < times:
				choice_list.append(i)
		if choice_list:
			result = random.choice(choice_list)
			break
		times += 1
	return result
