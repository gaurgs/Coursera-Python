largest = -1
smallest = None
while True:
    num = raw_input("Enter a number: ")
    if num == "done" : break
    if len(num)<1 : break
    try:
        inp=int(num)
    except:
        print "Invalid Input"
        continue;
    
    if(smallest is None):
        smallest = num;
    elif(smallest>num):
    	smallest = num
    if(num>largest):
    	largest=num
    

print "Maximum", largest
print "Minimum", smallest
