import os
 
#os.system("cd ..")
 
success = False
success_return = "Everything up-to-date\n"
success_return2 = "To http"
fail_return = "reject"
fail_return2 = "errno"
i = 1
while not success:
	print("start", i, "th git push.")
	os.system("git push > git_push_result.txt 2>&1")
	git_push_result = open('git_push_result.txt', encoding='UTF-8', errors='ignore')
	line = git_push_result.readlines()
	for every_line in line:
		print(every_line)
		if every_line.find(fail_return, 0, len(every_line))>-1:
			success=False
		if every_line.find(fail_return2, 0, len(every_line))>-1:
			success=False
		if success==False:
			break
		if success==True and every_line ==success_return or every_line.find(success_return2, 0, len(every_line))>-1:
			success=True
	first_line_result = line[0]
	# print("first_line_result is:", first_line_result)
	if first_line_result == success_return:
		success = True
	else:
		i += 1
	git_push_result.close()
	
print("Totally git-push", i, "times.")
print("End git-push.")
os.system("del git_push_result.txt")