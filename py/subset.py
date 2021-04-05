
fileobj=open("input/data.txt","r")
S=list(map(int,fileobj.readline().split(' ')))
N=list(map(int,fileobj.readline().split(' ')))
c=0
for i in range(0,len(N)):
	for j in range(i+1,len(N)):
		if (N[i]+N[j])%S[1]==0:
			c=c+1

res = open('output/odata.txt', 'at')
res.write('\n'+str(c))
res.close()

print (S,N,'\n',c)
input("Press Enter to continue...")