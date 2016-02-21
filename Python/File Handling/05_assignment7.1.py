# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
for line in fh:
	temp=line.rstrip();
	print temp.upper();
