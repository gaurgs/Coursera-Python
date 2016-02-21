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
	if email not in count:
		count[email] = 1
	else:
		count[email] = count[email] + 1;		


print count 			
