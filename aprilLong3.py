t = int(input())
for case in range(t):
	n, m, k = list(map(int, input().split()))
	a = [[0 for i in range(m)] for j in range(n)]
	for s in range(k):
		r, c = list(map(int, input().split()))
		a[r-1][c-1] = 1
	# print(arr)
	count = 0
	for i in range(n):
		for j in range(m):
			if a[i][j]==1:
				if i==0 or i==n-1:
					count+=1
				if j==0 or j==m-1:
					count+=1
				if j!=0 and a[i][j-1]==0:
					count+=1
				if i!=0 and a[i-1][j]==0:
					count+=1
				if j!=m-1 and a[i][j+1]==0:
					count+=1
				if i!=n-1 and a[i+1][j]==0:
					count+=1
	print(count)