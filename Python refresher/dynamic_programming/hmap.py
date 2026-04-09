# Enter your code here. Read input from STDIN. Print output to STDOUT
thickness = int(input())

# first start with head which is n
letter = "H"
triangleline = "H"
for i in range(thickness):
    spacing = (thickness*2)-1
    if i < thickness-1:
        print (f"{triangleline}".center(spacing," "))
        triangleline = "H"+ triangleline + "H"
    else:
        print (f"{triangleline}")
#calculate the gap between
gap = (thickness*thickness) - (len(triangleline)*2)
# second of height n+1
for i in range(thickness+1):
    displayletters = "H"*thickness
    rcolumns = (displayletters.center(thickness*2," "))
    lcolumns = (displayletters.center((thickness+3)*2," "))
    print(rcolumns+(" "*gap)+lcolumns)
# middle of round(n/2)
for i in range(int((thickness/2)+0.5)):
    middlespace = len(triangleline)-thickness
    print((letter*(5*thickness)).center(middlespace+(5*thickness)," "))
# third of height n+1
for i in range(thickness+1):
    displayletters = "H"*thickness
    rcolumns = (displayletters.center(thickness*2," "))
    lcolumns = (displayletters.center((thickness+3)*2," "))
    print(rcolumns+(" "*gap)+lcolumns)
# fourth of n
for i in range(thickness):
    spacing = ((thickness*thickness)+4)-(i)
    print(triangleline.rjust(spacing," "))     
    triangleline = triangleline[2:]
