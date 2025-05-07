num=[45,22,14,65,97,72]
def replace_numbers(num):
    for i in range(len(num)):
        if num[i]%3==0 and num[i]%5==0:
            num[i]="pppqqq"
        elif num[i]%3==0:
            num[i]="ppp"
        elif num[i]%5==0:
            num[i]="qqq"
replace_numbers(num)
print(num)

