n=int(input("Enter total numbers:"))
numbers=[]
for i in range(n):
    num=int(input("Enter a number:"))
    numbers.append(num)

sum=0
product=1
10
for i in numbers:
    if i%2==0:
        sum=sum+i
    else :
        product=product*i

print("sum",sum)
print("product",product)
