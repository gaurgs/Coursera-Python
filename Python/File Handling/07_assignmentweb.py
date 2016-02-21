import re
# opening the file and fh is file handler
fh = open('regex_sum_207537.txt')

# Creating Temperory variable to sum individual list element
resultSum=0

for line in fh:
	temp=line.rstrip();
	y=re.findall('[0-9]+',temp)
	if(len(y)==0):continue
	y=[int(x) for x in y]
	resultSum=resultSum+sum(y)

#printing final result
print resultSum
