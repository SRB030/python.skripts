def diskriminant():
    a = int(input('a = :'))
    b = int(input('b = :'))
    c = int(input('c = :'))
    diskr = b**2-4*a*c
    x1 = b-diskr/2
    x2 = b+diskr/2
    return print('diskriminant = :',diskr,'\n','x1 = :',x1,'\n','x2 = :',x2)

diskriminant()

input('press to enter')
