# Quadratic formula program

def mymain():
    import math
    
    a = raw_input('What is the coefficient of x^2,a?')
    b = raw_input('What is the coefficient of x,b?')
    c = raw_input('What is the constant?')

    a = float(a)
    b = float(b)
    c = float(c)

    x1 = -b/(2*a) + math.sqrt(b**2-4*a*c)/(2*a)
    x2 = -b/(2*a) - math.sqrt(b**2-4*a*c)/(2*a)

    print x1,x2

if __name__=='__main__':
    mymain()
    
