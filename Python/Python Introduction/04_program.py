fHand=open('mybox.txt');
for line in fHand:
	l=line.rstrip()
	print l
	if(l.startswith('From:')):
		print l;
