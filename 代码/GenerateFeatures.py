import os
import re
import csv
def getthefilelist(directory):
	filelist=[]
	for root,dire,files in os.walk(directory):
		for file in files:
			if re.search('.*\.txt',file):
				filelist.append(os.path.join(root,file))
	return filelist
def transform(filename):
	name=""
	counter=0
	flag=0
	done=0
	felist=featurelist()
	vector=[0 for x in felist]
	word_num=0.0
	short_num=0
	#corpus=[]
	with open (filename,'r') as file:
		text=file.read()
		namepatter='[a-zA-Z0-9_-]+.[a-zA-Z0-9_-]*@[a-zA-Z0-9_-]+[\.a-zA-Z0-9_-]*\.[a-zA-Z0-9_-]+'
		#namepatter = '[a-zA-Z0-9_-]+.*@.*'
		eadds = re.findall(namepatter,text)
		if len(eadds)==0:
			print filename,"has no writer"
			return vector,name
		else:
			name = eadds[0].split('@')[0]
			name.strip()
		datas=text.split("\n\n")
		e_txt = ""
		if len(datas) < 2:
			print filename,"did not delete the heads successfully"
		else:
			for data in datas[1:len(datas)]:
				if data:
					e_txt += data
		for fe in range(len(felist)):
			mo=' '+felist[fe]+' '
			wlist=re.findall(mo,e_txt)
			vector[fe] += len(wlist)
		words = re.split('[,.! ;:\n=-?]',e_txt)
		words=[x for x in words if x]
		word_num=len(words)*1.0
		for word in words:
			if len(word)<4:
				short_num += 1
	vector.append(short_num)
	vector=[ x/(word_num) for x in vector]   ###calculate ratios
	return vector,name

def featurelist():
	with open(r"C:\Users\YonghaoFu\Desktop\dics.txt",'r') as f:
		felist=[]
		line=f.readline()
		while line:
			line=line.strip()
			datas=line.split(' ')
			datas=[x for x in datas if x]
			for data in datas:
				if data not in felist:
					felist.append(data)
			line=f.readline()
	with open(r"C:\Users\YonghaoFu\Desktop\collos.txt",'r') as f:
		line=f.readline()
		while line:
			line=line.strip()
			datas=line.split(" ")
			datas=[x for x in datas if x]
			for x in range(len(datas)):
				if x%2 == 1:
					data=datas[x-1]+" "+datas[x]
					felist.append(data)
			line= f.readline()
	return felist

def directory():
	directory=r"enron_with_categories"
	return directory

def generate():# use different transform and featurelist function 
	delete=0                          #can get different features
	namelist=[]
	directory=r"enron_with_categories"
	filelist=getthefilelist(directory)
	#filelist=[r"C:\Users\LPX\Desktop\enron_with_categories\1\3111.txt"]
	with open(r"out.csv",'wb') as fileout:
		out=csv.writer(fileout)
		# felist=featurelist()
		# felist.append('len3')
		# felist.append('label')
		#felist=['tab','daxie','kongge','shuzi','Thanks','ThankYou','label']
		felist=featurelist2()
		felist.append('label')
		out.writerow(felist)
		for filename in filelist:
			vector,name=transform2(filename)
			if name == "":
				delete +=1
				continue
			if name not in namelist:
				namelist.append(name)
			label=namelist.index(name)
			vector.append(label)
			out.writerow(vector)
	namelist.sort()
	print namelist
	print len(namelist)
	print delete
def featurelist2():
	#felist = ['\t','[A-Z]',' ','\d']
	felist = ['able','al','ful','ible','ic','ive','less','ly','ous']
	return felist
def transform2(filename):
	felist=featurelist2()
	vector=[0 for x in felist]
	name=""
	with open(filename) as f:
		text=f.read()
		namepatter='[a-zA-Z0-9_-]+.[a-zA-Z0-9_-]*@[a-zA-Z0-9_-]+[\.a-zA-Z0-9_-]*\.[a-zA-Z0-9_-]+'
		eadds = re.findall(namepatter,text)
		if len(eadds)==0:
			print filename,"has no writer"
			return vector,name
		else:
			name = eadds[0].split('@')[0]
			name.strip()
		datas=text.split("\n\n")
		e_txt = ""
		if len(datas) < 2:
			print filename,"did not delete the heads successfully"
		else:
			for data in datas[1:len(datas)]:
				if data:
					e_txt += data
		for fe in range(len(felist)):
			mo=' [a-zA-Z]+'+felist[fe]+' '
			#mo=felist[fe]
			wlist = re.findall(mo,e_txt)
			vector[fe] += len(wlist)
		'''add thank you feature
		wlist=re.findall('.?[Tt]anks.?',e_txt)
		vector.append(len(wlist))
		wlist=re.findall('.?[Tt]ank you.?',e_txt)
		vector.append(len(wlist))
		'''
	return vector,name





if __name__ == '__main__':
	#directory=r"C:\Users\LPX\Desktop\enron_with_categories"
	#filelist=getthefilelist(directory)
	#len(filelist)
	# filename=r"C:\Users\YonghaoFu\Desktop\enron_with_categories\1\3111-1.txt"
	# vector,name=transform2(filename)
	# print vector,name
	#print vector
	generate()
