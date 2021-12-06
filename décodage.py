import matplotlib.pyplot as plt

bi=[]
x=int(input('donner le taille de donneé'))
for i in range(x):
    print('donner les bit de donneé')
    bi.append(input())


    
#NRZ
NRZ=[]
for x in bi:
    for i in range(10):
        NRZ.append(x)
plt.xlabel('data size')           
plt.title("NRZ")
plt.plot(NRZ,color='r')
plt.show()




#Manchester
man=[]
pol=[]
for k in bi:
	if k==1:
		pol.append(-1)
	else:
		pol.append(1)
for x in pol:
	for i in range(5):
	    man.append(0)
	for i in range(5):
	    man.append(1)
plt.xlabel('data size')		
plt.title("Manchester")
plt.plot(man,color='g')
plt.show()
