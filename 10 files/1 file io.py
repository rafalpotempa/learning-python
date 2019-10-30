# jabber = open("sample.txt", 'r')
# for line in jabber:
# 	if "jabberwock" in line.lower():
# 		print(line, end='')
# jabber.close()

# print(f"\n Example 2\n" + "-"*11)
# with open("sample.txt", 'r') as jabber:
# 	for line in jabber:
# 		if "JAB" in line.upper():
# 			print(line, end='')

# with open("sample.txt", 'r') as jabber:
# 	line = jabber.readline()
# 	while line:
# 		print(line, end='')
# 		line = jabber.readline()

# with open("sample.txt", 'r') as jabber:
# 	lines = jabber.readlines()
# 	for line in lines:
# 		print(line, end='')

with open("sample.txt", 'r') as jabber:
	lines = jabber.readlines()
	for line in lines[::-1]:
		print(line, end='')

with open("sample.txt", 'r') as jabber:
	lines = jabber.read()
	for line in lines[::-1]:
		print(line, end='')
