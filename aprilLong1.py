n = int(input())
a = list(map(int, input().split()))
a.sort()
l = len(a)
big1 = a[l-1]
big2 = 0
for i in range(l-1, -1, -1):
	if a[i] != big1:
		big2 = a[i]
		break
print(big2%big1)