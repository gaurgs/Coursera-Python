fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
tempLst=list();
srtList=list();
for line in fh:
	tempLst=line.split();
	lst=lst+tempLst;
	
lst.sort();
print lst
