fHand=open('a1.txt');
count=dict();
a=" ";
lst=list();
templst=list();
for line in fHand:
	l=line.rstrip()
	if(l.endswith('2008') and l.startswith('From')):			
		word = l.split(" ")[6].split(":")[0].strip()
		lst.append(word)	

for word in lst:
	count[word] = count.get(word,0) + 1	

for key,val in count.items():
	templst.append( (key,val))

templst.sort()
for key,val in templst:
	print key,val
