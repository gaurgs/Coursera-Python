fHand=open('a1.txt');
count=dict();
a="";
lst=list();
for line in fHand:
	l=line.rstrip()
	if(l.startswith('From:')):
		 a=l.split(":");
		 lst.append(a[1].strip())		 	
	
for email in lst:
	count[email] = count.get(email,0)+1

for key in count:
	print key,count[key]

