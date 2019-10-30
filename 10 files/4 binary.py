# with open("binary", 'bw') as binFile:
# 	for i in range(17):
# 		binFile.write(bytes([i]))

# with open("binary", 'br') as binFile:
# 	for b in binFile:
# 		print(f"{b}")

a = 65534		# FF FE
b = 65535		# FF FF
c = 65536		# 00 01 00 00
x = 2998302		# 00 2D C0 1E

with open("binary2", 'bw') as binFile:
	binFile.write(a.to_bytes(2, 'big'))
	binFile.write(b.to_bytes(2, 'big'))
	binFile.write(c.to_bytes(4, 'big'))
	binFile.write(x.to_bytes(4, 'big'))
	binFile.write(x.to_bytes(4, 'little'))

with open("binary2", 'br') as binFile:
	e = int.from_bytes(binFile.read(2), 'big')
	f = int.from_bytes(binFile.read(2), 'big')
	g = int.from_bytes(binFile.read(4), 'big')
	y = int.from_bytes(binFile.read(4), 'big')
	z = int.from_bytes(binFile.read(4), 'little')
	print(e, f, g, y, z)
	
	for b in binFile:
		print(f"{b}")
