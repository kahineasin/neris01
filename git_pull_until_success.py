import os
 
#os.system("cd ..")
 
success = False
success_return = "Already up to date.\n"
i = 1
while not success:
	print("start", i, "th git pull.")
	os.system("git pull > git_pull_result.txt 2>&1")
	git_pull_result = open('git_pull_result.txt', encoding='UTF-8', errors='ignore')
	line = git_pull_result.readlines()
	for every_line in line:
		print(every_line)
	first_line_result = line[0]
	# print("first_line_result is:", first_line_result)
	if first_line_result == success_return:
		success = True
	else:
		i += 1
	git_pull_result.close()
 
print("Totally git-pull", i, "times.")
print("End git-pull.")
os.system("del git_pull_result.txt")