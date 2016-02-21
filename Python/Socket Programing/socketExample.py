import urllib
fHand=urllib.urlopen('http://www.dr-chuck.com/page1.htm');
for line in fHand:
	print line.strip()
