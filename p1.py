def gen():
    num1=0
    num2=1
    while num1<=20:
        yield num1
        num1,num2=num2,(num1+num2)
ob=gen()
for i in ob:
    print(i)