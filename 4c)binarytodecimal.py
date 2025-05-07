def binarytodecimal(num):
    decimal=0
    i=0
    while num!=0:
        decimal+=(num%10)*(2**i)
        num//=10
        i+=1
    return decimal
num=int(input("Enter the binary number"))
print("The decimal number is:",binarytodecimal(num))