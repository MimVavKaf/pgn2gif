import re
from deneme import *
from PIL import Image

board=Image.open('/home/mevaka/Desktop/gifci/satranc/90.png')
brd=Image.open('/home/mevaka/Desktop/gifci/satranc/90.png')
bkale=Image.open('/home/mevaka/Desktop/gifci/satranc/wr.png' )
bvezir=Image.open('/home/mevaka/Desktop/gifci/satranc/wq.png' )
bpiyon=Image.open('/home/mevaka/Desktop/gifci/satranc/wp.png' )
bat=Image.open('/home/mevaka/Desktop/gifci/satranc/wn.png' )
bfil=Image.open('/home/mevaka/Desktop/gifci/satranc/wb.png' )
bsah=Image.open('/home/mevaka/Desktop/gifci/satranc/wk.png' )
ssah=Image.open('/home/mevaka/Desktop/gifci/satranc/bk.png' )
sat=Image.open('/home/mevaka/Desktop/gifci/satranc/bn.png' )
spiyon=Image.open('/home/mevaka/Desktop/gifci/satranc/bp.png' )
svezir=Image.open('/home/mevaka/Desktop/gifci/satranc/bq.png' )
skale=Image.open('/home/mevaka/Desktop/gifci/satranc/br.png' )
sfil=Image.open('/home/mevaka/Desktop/gifci/satranc/bb.png' )

oyun=open('/home/mevaka/Desktop/gifci/oyun.pgn')
icerik=oyun.read()
icerik=icerik.replace("\n","")
icerik=icerik.replace("\r","")
icerik=icerik.replace("/","")
icerik=icerik.replace("+","")
icerik=icerik.replace("-","")
icerik=icerik.replace("?","")
icerik=icerik.replace("!","")

hamle=re.split("\d*\.", icerik)
for i in range(len(hamle)):
	hamle[i]=hamle[i].split(" ")

for i in range(1, len(hamle)):
	print i, hamle[i][0] # beyaz
	print i, hamle[i][1] # siyah

def saydir(bas,son):
	for i in range(bas,son):
		if "O" in hamle[i][0]:
			rokyap(0,hamle[i][0])
		elif "=" in hamle[i][0]:
			piyongider(hamle[i][0])
		else:
			parca=list(hamle[i][0])
			(nereden,nereye,tas)=hamlecoz(0,parca)
			tahta[nereden[0]][nereden[1]]=0
			tahta[nereye[0]][nereye[1]]=tas
			print i, nereden,nereye,tas
		if "O" in hamle[i][1]:
			rokyap(1,hamle[i][1])
		elif "=" in hamle[i][0]:
			piyongider(hamle[i][1])
		else:
			parca=list(hamle[i][1])
			(nereden,nereye,tas)=hamlecoz(1,parca)
			tahta[nereden[0]][nereden[1]]=0
			tahta[nereye[0]][nereye[1]]=tas
			print i, nereden,nereye,tas

def rokyap(renk,tur):
	if renk==0:
		if tur=="OO":
			tahta[1][5]=0
			tahta[1][7]=6
			tahta[1][8]=0
			tahta[1][6]=4
		else:
			tahta[1][5]=0
			tahta[1][1]=0
			tahta[1][3]=6
			tahta[1][4]=4
	else:
		if tur=="OO":
			tahta[8][5]=0
			tahta[8][7]=12
			tahta[8][8]=0
			tahta[8][6]=10
		else:
			tahta[8][5]=0
			tahta[8][1]=0
			tahta[8][3]=12
			tahta[8][4]=10

def piyongider(hareket):
	if "1" in hareket: # bu siyah # c1=Q  #cxd1=Q
		tahta[2][sutunlar[hareket[0]]]=0
		if len(hareket) == 3:
			if hareket[3]=='Q':
				tahta[1][sutunlar[hareket[0]]]=11
			elif hareket[3]=='R':
				tahta[1][sutunlar[hareket[0]]]=10
			elif hareket[3]=='N':
				tahta[1][sutunlar[hareket[0]]]=9
			elif hareket[3]=='B':
				tahta[1][sutunlar[hareket[0]]]=8
		else:
			if hareket[5]=='Q':
				tahta[1][sutunlar[hareket[2]]]=11
			elif hareket[5]=='R':
				tahta[1][sutunlar[hareket[2]]]=10
			elif hareket[5]=='N':
				tahta[1][sutunlar[hareket[2]]]=9
			elif hareket[5]=='B':
				tahta[1][sutunlar[hareket[2]]]=8
	else: # bu beyaz # c1=Q  #cxd1=Q
		tahta[7][sutunlar[hareket[0]]]=0
		if len(hareket) == 3:
			if hareket[3]=='Q':
				tahta[7][sutunlar[hareket[0]]]=5
			elif hareket[3]=='R':
				tahta[7][sutunlar[hareket[0]]]=4
			elif hareket[3]=='N':
				tahta[7][sutunlar[hareket[0]]]=3
			elif hareket[3]=='B':
				tahta[7][sutunlar[hareket[0]]]=2
		else:
			if hareket[5]=='Q':
				tahta[7][sutunlar[hareket[2]]]=5
			elif hareket[5]=='R':
				tahta[7][sutunlar[hareket[2]]]=4
			elif hareket[5]=='N':
				tahta[7][sutunlar[hareket[2]]]=3
			elif hareket[5]=='B':
				tahta[7][sutunlar[hareket[2]]]=2

def goster():
	for i in range(1,9):
		for j in range(1,9):
			if tahta[i][j]==1:
				brd.paste( bpiyon, ( (i-1)*90, (j-1)*90 ), bpiyon)
			if tahta[i][j]==2:
				brd.paste( bfil,   ( (i-1)*90, (j-1)*90 ), bfil)
			if tahta[i][j]==3:
				brd.paste( bat, ( (i-1)*90, (j-1)*90 ), bat)
			if tahta[i][j]==4:
				brd.paste( bkale, ( (i-1)*90, (j-1)*90 ), bkale)
			if tahta[i][j]==5:
				brd.paste( bvezir, ( (i-1)*90, (j-1)*90 ), bvezir)
			if tahta[i][j]==6:
				brd.paste( bsah, ( (i-1)*90, (j-1)*90 ), bsah)
			if tahta[i][j]==7:
				brd.paste( spiyon, ( (i-1)*90, (j-1)*90 ), spiyon)
			if tahta[i][j]==8:
				brd.paste( sfil, ( (i-1)*90, (j-1)*90 ), sfil)
			if tahta[i][j]==9:
				brd.paste( sat, ( (i-1)*90, (j-1)*90 ), sat)
			if tahta[i][j]==10:
				brd.paste( skale, ( (i-1)*90, (j-1)*90 ), skale)
			if tahta[i][j]==11:
				brd.paste( svezir, ( (i-1)*90, (j-1)*90 ), svezir)
			if tahta[i][j]==12:
				brd.paste( ssah, ( (i-1)*90, (j-1)*90 ), ssah)
	brd.show()
