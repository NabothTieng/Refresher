
def fizbuzz(x):
    for n in range(1,x+1):
        if n%3==0 and n%5 == 0:
            print("Fizzbuzz",n)
        elif n%3==0:
            print("Fizz",n)
        elif n%5==0:
            print("Buzz",n)

x=int(input("Enter a number: "))
fizbuzz(x)