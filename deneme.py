tahta=[
[-1,-1,-1,-1,-1,-1,-1,-1],
[-1,4,3,2,5,6,2,3,4],
[-1,1,1,1,1,1,1,1,1],
[-1,0,0,0,0,0,0,0,0],
[-1,0,0,0,0,0,0,0,0],
[-1,0,0,0,0,0,0,0,0],
[-1,0,0,0,0,0,0,0,0],
[-1,7,7,7,7,7,7,7,7],
[-1,10,9,8,11,12,8,9,10]]

sutunlar={'z':0, 'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}

def hamlecoz(renk,parca):
	nereden=0
	if len(parca)==2: # d4
		sutun=sutunlar[parca[0]]
		satir=int(parca[1])
		tas=renk*6+1
		if renk == 0:
			if parca[1] =='4':
				if tahta[satir-1][sutun]==1:
					nereden=(satir-1, sutun)
				else:
					nereden=( satir-2, sutun)
			else:
				nereden=( satir-1, sutun)
		else:
			if parca[1] =='5':
				if tahta[satir+1][sutun]==7:
					nereden=(satir+1, sutun)
				else:
					nereden=( satir+2, sutun)
			else:
				nereden=( satir+1, sutun)

	elif parca[0].islower(): #exd5
		satir=int(parca[3])
		sutun=sutunlar[parca[0]]
		tas=renk*6+1
		if renk==0:
			nereden=( satir-1, sutun)
		else:
			nereden=( satir+1, sutun)

	elif parca[1]=='x': # Bxc4
		satir=int(parca[3])
		sutun=sutunlar[parca[2]]
		ayrac=0
	elif parca[2]=='x': #Rdxd5
		satir=int(parca[4])
		sutun=sutunlar[parca[3]]
		ayrac=parca[1]

	elif len(parca)==3: #icinde x yok ,ayracsiz #Rd5
		satir=int(parca[2])
		sutun=sutunlar[parca[1]]
		ayrac=0
	else: #R3d4 , Nde5
		satir=int(parca[3])
		sutun=sutunlar[parca[2]]
		ayrac=parca[1]

	if nereden==0: # eger giden tas bir piyonsa zaten nereden geldigini cozduk
		# eger diger taslardan biriyse nereden degeri hala 0 omlasi lazm
		if parca[0]=='R': # bu bir kale
			nereden=kale(renk,satir,sutun,ayrac)
			tas=renk*6+4
		elif parca[0]=='B':
			nereden=fil(renk,satir,sutun)
			tas=renk*6+2
		elif parca[0]=='N':
			nereden=at(renk,satir,sutun,ayrac)
			tas=renk*6+3
		elif parca[0]=='Q':
			nereden=vezir(renk,satir,sutun)
			tas=renk*6+5
		elif parca[0]=='K':
			nereden=sah(renk,satir,sutun)
			tas=renk*6+6

	nereye=(satir,sutun)
#	r1=renkne(nereden[0],nereden[1])
#	r2=renkne(nereye[0],nereye[1])

#	return (nereden,nereye,r1,r2,tas)
	return (nereden,nereye,tas)

def renkne(satir,sutun):
	if satir%2==0:
		if sutun % 2 ==0:
			return 1
		else:
			return 0
	else:
		if sutun%2==0:
			return 0
		else :
			return 1

def kale(renk,satir,sutun,ayrac):
	aranan=renk*6+4 #beyaz kale 3, siyah kale 9
	#beyaz ise renk=0 , siyah ise 1

	if ayrac==0:
		for i in range(satir+1,9): # sutun sabit satirlari arttir
			if tahta[i][sutun] != 0:
				if tahta[i][sutun] == aranan:
					return (i, sutun)
				else:
					break
		for i in range(satir-1,0,-1): # sutun sabit satirlari azalt
			if tahta[i][sutun] != 0:
				if tahta[i][sutun] == aranan:
					return (i, sutun)
				else:
					break
		for i in range(sutun+1,9):
			if tahta[satir][i] !=0:
				if tahta[satir][i] == aranan:
					return (satir,i)
				else:
					break
		for i in range(sutun-1,0,-1):
			if tahta[satir][i] != 0:
				if tahta[satir][i] == aranan:
					return (satir,i)
				else:
					break

	else :
		if ayrac in 'abcdefgh':
			sutun=sutunlar[ayrac]
		else :
			satir=int(ayrac)

		return (satir,sutun)


def at(renk,satir,sutun,ayrac):
	aranan=renk*6+3
	if ayrac==0:
		if satir>2 and sutun>1:
			if tahta[satir-2][sutun-1]==aranan:
				return (satir-2,sutun-1)
		if satir>2 and sutun<8:
			if tahta[satir-2][sutun+1]==aranan:
				return (satir-2,sutun+1)
		if satir<7 and sutun>1:
			if tahta[satir+2][sutun-1]==aranan:
				return (satir+2,sutun-1)
		if satir<7 and sutun<8:
			if tahta[satir+2][sutun+1]==aranan:
				return (satir+2,sutun+1)
		if satir>1 and sutun>2:
			if tahta[satir-1][sutun-2]==aranan:
				return (satir-1,sutun-2)
		if satir>1 and sutun<7:
			if tahta[satir-1][sutun+2]==aranan:
				return (satir-1,sutun+2)
		if satir<8 and sutun>2:
			if tahta[satir+1][sutun-2]==aranan:
				return (satir+1,sutun-2)
		if satir<8 and sutun<7:
			if tahta[satir+1][sutun+2]==aranan:
				return (satir+1,sutun+2)
	else:
		if ayrac in 'abcdefgh':
			sutun=sutunlar[ayrac]
			for i in range(1,9):
				if tahta[i][sutun]==aranan:
					return (i,sutun)
		else :
			satir=int(ayrac)
			for i in range(1,9):
				if tahta[satir][i]==aranan:
					return (satir,i)

def fil(renk,satir,sutun):
	#print "fil geldi"
	aranan=renk*6+2
	sa=satir
	su=sutun

	while (satir<8 and sutun<8):
		#print "bir"
		satir+=1
		sutun+=1
		if tahta[satir][sutun] != 0:
			if tahta[satir][sutun] == aranan:
				return (satir,sutun)
			else:
				break

	satir=sa
	sutun=su
	while (satir>1 and sutun>1):
		#print "iki"
		satir -=1
		sutun -=1
		if tahta[satir][sutun] != 0:
			if tahta[satir][sutun] == aranan:
				return (satir,sutun)
			else:
				break
	satir=sa
	sutun=su
	while (satir<8 and sutun>1):
		#print "uc"
		satir +=1
		sutun -=1
		if tahta[satir][sutun] != 0:
			if tahta[satir][sutun] == aranan:
				return (satir,sutun)
			else:
				break
	satir=sa
	sutun=su
	while (satir>1 and sutun<8):
		#print "dort"
		satir -=1
		sutun +=1
		if tahta[satir][sutun] != 0:
			if tahta[satir][sutun] == aranan:
				return (satir,sutun)
			else:
				break

def vezir(renk,satir,sutun):
	aranan=renk*6 +5
	sa=satir
	su=sutun

	for i in range(satir+1,9): # sutun sabit satirlari arttir
		if tahta[i][sutun] != 0:
			if tahta[i][sutun] == aranan:
				return (i, sutun)
			else:
				break
	for i in range(satir-1,0,-1): # sutun sabit satirlari azalt
		if tahta[i][sutun] != 0:
			if tahta[i][sutun] == aranan:
				return (i, sutun)
			else:
				break
	for i in range(sutun+1,9):
		if tahta[satir][i] !=0:
			if tahta[satir][i] == aranan:
				return (satir,i)
			else:
				break
	for i in range(sutun-1,0,-1):
		if tahta[satir][i] != 0:
			if tahta[satir][i] == aranan:
				return (satir,i)
			else:
				break

	while (satir<8 and sutun<8):
		satir+=1
		sutun+=1
		if tahta[satir][sutun] != 0:
			if tahta[satir][sutun] == aranan:
				return (satir,sutun)
			else:
				break

	satir=sa
	sutun=su
	while (satir>1 and sutun>1):
		satir -=1
		sutun -=1
		if tahta[satir][sutun] != 0:
			if tahta[satir][sutun] == aranan:
				return (satir,sutun)
			else:
				break
	satir=sa
	sutun=su
	while (satir<8 and sutun>1):
		satir +=1
		sutun -=1
		if tahta[satir][sutun] != 0:
			if tahta[satir][sutun] == aranan:
				return (satir,sutun)
			else:
				break
	satir=sa
	sutun=su
	while (satir>1 and sutun<8):
		satir -=1
		sutun +=1
		if tahta[satir][sutun] != 0:
			if tahta[satir][sutun] == aranan:
				return (satir,sutun)
			else:
				break

def sah(renk,satir,sutun):
	aranan=renk*6 + 6

	if satir<8 and sutun<8:
		if tahta[satir+1][sutun+1]==aranan:
			return (satir+1,sutun+1)
	if satir<8 and sutun>1:
		if tahta[satir+1][sutun-1]==aranan:
			return (satir+1,sutun-1)
	if sutun<8:
		if tahta[satir][sutun+1]==aranan:
			return (satir,sutun+1)
	if sutun>1:
		if tahta[satir][sutun-1]==aranan:
			return (satir,sutun-1)
	if satir>1 and sutun<8:
		if tahta[satir-1][sutun+1]==aranan:
			return (satir-1,sutun+1)
	if satir>1 and sutun>1:
		if tahta[satir-1][sutun-1]==aranan:
			return (satir-1,sutun-1)
	if satir<8:
		if tahta[satir+1][sutun]==aranan:
			return (satir+1,sutun)
	if satir>1:
		if tahta[satir-1][sutun]==aranan:
			return (satir-1,sutun)
