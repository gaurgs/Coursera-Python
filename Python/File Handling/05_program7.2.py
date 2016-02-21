# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
sum=0
count=0
for line in fh:
    line=line.rstrip();	
    if not line.startswith("X-DSPAM-Confidence:") : continue
    a=line.find(':')
    sum=sum+float(line[a+1:].lstrip())
    count=count+1
	
print 'Average spam confidence:',(sum/float(count))  
 
