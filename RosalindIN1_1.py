print 'The two legs of a right angled triangle are designated a and b.'

a = input ("Enter a number < 1000 for a: ")
assert(0 < a < 1000),"Number NOT between 0 and 1000"

b = input ("Enter a number < 1000 for b: ")
assert(0 < b < 1000),"Number NOT between 0 and 1000"

c = (a**2 + b**2)**(0.5)

# print the number here to check whether c is rounded or not.

print c, type(c)

print "For right angled triangles, if Pythagoras is correct, a^2 + b^2 = c^2"

#c is rounded to 2 decimal places as a float.
print "c =: %.2f" % c
