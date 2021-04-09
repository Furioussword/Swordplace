
fileobj=open("input/data.txt","r")
S=list(map(int,fileobj.readline().split(' ')))
N=list(map(int,fileobj.readline().split(' ')))
c=0
def subs(A,B):
	X=list()
	Y=list()
	Y.append(0)
	for ind in range(0,len(B)):
		X=list()
		X.append(B[ind])
		for i in range(0,len(B)):
			for j in range(i,len(B)):
				if (B[i]+B[j])%A[1]!=0:
					if B[j] not in X:
						for i1 in range(0,len(X)):
							if (B[j]+X[i1])%A[1]==0:
								f=False
								break
							else:
								f=True
						if f==True:
							X.append(B[j])
							f=False
		if len(X)>len(Y):
			Y=X
			X=list()
	c=len(Y)
	print 'subset' ,Y, "max count ",c
	return Y,c
res = open('output/odata.txt', 'at')
res.write('\n'+str(c))
res.close()
subs(S,N)


input("Press Enter to continue...")