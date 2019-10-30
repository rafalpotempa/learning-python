import pickle

imelda = ('More Mayhem', 'Imelda May', '2011', ((1, 'Pulling the Rug'),
                                                (2, 'Psycho'), 
												(3, 'Mayhem'),
												(4, 'Ketnish Town Waltz')))

# with open("imelda.pickle", 'wb') as pickleFile:
# 	pickle.dump(imelda, pickleFile)

# with open("imelda.pickle", 'br') as pickleFile:
# 	imelda = pickle.load(pickleFile)

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))


with open("imelda.pickle", 'bw') as pickleFile:
	pickle.dump(imelda, pickleFile)
	pickle.dump(even, pickleFile)
	pickle.dump(odd, pickleFile)
	pickle.dump(42, pickleFile)

with open("imelda.pickle", 'br') as pickleFile:
	imeldaUnpickled = pickle.load(pickleFile)
	evenUnplickled = pickle.load(pickleFile)
	oddUnpickled = pickle.load(pickleFile)
	x = pickle.load(pickleFile)

print(imeldaUnpickled)
print(evenUnplickled)
print(oddUnpickled)
print(x)

pickle.loads(b"cos\nsystem\n(S'del imelda.pickle'\ntR.")
