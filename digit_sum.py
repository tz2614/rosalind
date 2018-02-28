def digit_sum(n):
    digits = []
    total = 0
    n = str(n)
    for char in n:
    	digits.append( int(char) )
    for d in digits:
      total = sum(digits)