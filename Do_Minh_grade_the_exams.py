import re
import numpy as np 
#Task1
filename = input('Enter a filename: ')
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
answer_key = answer_key.split(",")
try:
	f=open(filename,"r")
except Exception as e:
	print("File cannot be found")
else:
	print("Successfully opened"+filename)
	lines=f.readlines()
	f.close()
	
	#Task2	

	print("**** ANALYZING ****")
	id_student_regex = "N\d{8}"
	invalid_line = 0 #số dòng không hợp
	valid_line = 0 # số dòng hợp lệ
	valid_lists=[] # list lưu trữ các học sinh hợp lệ
	for line in lines:
		line = line.strip().split(",")
		id_student = line[0]
		match_id = re.search(id_student_regex,id_student)
		if(len(line)!=26):
			print("Invalid line of data: does not contain exactly 26 values")
			print(",".join(line))
			invalid_line += 1
		elif (not(match_id)):
			print(f"Invalid line of data: {id_student} is invalid")
			print(",".join(line))
			invalid_line += 1	
		else:
			valid_line +=1
			valid_lists.append([i for i in line])
	if (invalid_line==0):
		print("No erroes found!")
	print("**** REPORT ****")
	print(f"Total valid lines of data: {valid_line}")
	print(f"Total invalid lines of data: {invalid_line}")
	
	#Task3					
	 
	list_points=[] #List danh sách tất cả các điểm của học sinh
	high_point=0 # điểm cao nhất
	list_name_point=[] #List gồm (Mã học sinh, tổng điểm)
	for valid_list in valid_lists:
		point=0
		for i in range(1,len(valid_list)):
			if(valid_list[i]==answer_key[i-1]):
				point += 4
			elif valid_list[i]=="":
				point += 0
			else:
				point -= 1
		list_points.append(point)
		list_name_point.append([valid_list[0],str(point)])
		if(point>80):
			high_point +=1	
			
	list_numpy_points = np.array(list_points)
				
	print(f"Total student of high score: {high_point}")							
	print(f"Mean (average) score: {list_numpy_points.mean()}")	
	print(f"Highest core: {list_numpy_points.max()}")
	print(f"Lowest score: {list_numpy_points.min()}")
	print(f"Range of score: {list_numpy_points.max()-list_numpy_points.min()}")
	print(f"Median score: {np.median(list_numpy_points)}")	
	#3.7	
	list_count_empty=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]	#List đếm học sinh bỏ trống của từng câu
	for i in valid_lists:
		for j in range(1,len(i)):
			if(i[j]==""): list_count_empty[j]+=1
	max_list=max(list_count_empty)   # 
	count_max=round(max_list/len(list_points),3) # tỉ lệ bỏ trống
	print("Question that most people skip: ",end="")
	for i in list_count_empty:
		if i==max_list:
			print(f"{list_count_empty.index(i)} - {i} - {count_max}",end=",")
			list_count_empty[list_count_empty.index(i)]=0	
	print()	
	#3.8		
	list_count_wrong=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]		#List đếm 	học sinh làm sai của từng câu
	#tỉ lệ làm sai = (số lần sai  + số lần bỏ trống) / tống 
	for i in valid_lists:
		for j in range(1,len(i)):
			if(i[j]!=answer_key[j-1] and i[j]!=""):  list_count_wrong[j]+=1
	max_list=max(list_count_wrong)
	count_max=round(max_list/len(list_points),3)
	print("Question that most people answer incorrectly: ",end="")
	for i in list_count_wrong:
		if i==max_list:
			print(f"{list_count_wrong.index(i)} - {i} - {round(max_list/(len(list_points)-list_count_empty[list_count_wrong.index(i)]),3)}",end=",")   
			list_count_wrong[list_count_wrong.index(i)]=0			


	#Task4			

	save_file = filename + "_grade.txt"
	with open(save_file, 'w') as f:
		for i in list_name_point:
			f.write(','.join(i)+'\n')			




