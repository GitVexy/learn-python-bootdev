def cool_fizzbuzz(start, end):
    out = []
    
    for i in range(start, end):
        out.append("fizzbuzz" 
                   if i % 3 == 0 and i % 5 == 0 
                   else "fizz" if i % 3 == 0 
                   else "buzz" if i % 5 == 0 
                   else i)
    return out

def fizzbuzz(start, end):
    out = []
    
    for i in range(start, end):
        if i % 3 == 0 and i % 5 == 0:
            out.append("fizzbuzz")
        elif i % 3 == 0:
            out.append("fizz")
        elif i % 5 == 0:
            out.append("buzz")
        else:
            out.append(i)
        
print(fizzbuzz(1, 15))