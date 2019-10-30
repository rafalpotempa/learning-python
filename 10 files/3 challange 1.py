with open("sample.txt", 'a') as jabber:
	for i in range(1,13):
		for j in range(1,13):
			print(f"{j:>2} times {i:2} is {i*j:<}", file=jabber)
		print("-"*20, file=jabber)