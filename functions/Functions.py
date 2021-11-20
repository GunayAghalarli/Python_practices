def computepay(h, r):
    if h<40:
    	p = r*h
    else:
        p = 1.5 * r * (h - 40) + (40 *r)
        
    return p

hrs = float(input("Enter Hours:"))
rate  = float(input("Enter rate:"))
p = computepay(hrs, rate)
print("Pay", p)