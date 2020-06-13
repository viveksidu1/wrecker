def add(a,b):
    c=a+b
    print('Addition of {} and {} = {}'.format(a,b,c))
def sub(a,b):
    c=a-b
    print('Subtraction of {} and {} = {}'.format(a,b,c))
def mul(a,b):
    c=a*b
    print('Multiplication of {} and {} = {}'.format(a,b,c))
def div(a,b):
    if a==0 or b==0:
        print("Number should not be Zero")
    else:
        c = a / b
        print('Division of {} and {} = {}'.format(a,b,c))



n=int(input("Enter the first number : "))
m=int(input("Enter the second number : "))

add(n,m)
sub(n,m)
mul(n,m)
div(n,m)
