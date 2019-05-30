t = int(input())
for k in range(t):
	n = int(input())
	s, x = input().split()
	length = len(s)
	fin = length*(length+1)/2
	b = s.split(x)
	b = list(filter(None, b))
	fin1 = 0
	for elem in b:
		fin1 += len(elem)*(len(elem)+1)/2
	fin = int(fin)-int(fin1)
	print(fin)

#Accepted solution