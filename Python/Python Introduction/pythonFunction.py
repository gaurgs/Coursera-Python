def computepay(h,r):
    if(h<40):
       return h*r
    else:
        return (h*r + (h-40)*5.25)  

hrs = raw_input("Enter Hours:")
ratePerHrs = raw_input("Enter Rate Per Hour:")

h = float(hrs);
r = float(ratePerHrs);

p = computepay(h,r)
print p
