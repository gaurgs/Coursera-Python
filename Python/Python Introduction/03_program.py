fHand=open('mybox.txt');
for line in fHand:
	print line
	if line.startswith('From:'):
		print line

