def array_hash(lines):
	count = 0
	result = 0
	for l in lines:
		for i in range(len(l)): result += (ord(l[i]) - 65) + count + i
		count += 1
	return result

test_cases = int(input())
for i in range(test_cases):
	number = int(input())
	line = []
	for j in range(number):
		line.append(input())
	print(array_hash(line))
	line = []