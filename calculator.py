def calculate():
    num1 = float(input("num1"))
    num2 = float(input("num2"))
    operator = int(input("operator (1=multiply, 2=divide, 3=add, 4=subtract)"))
    if operator == 1:
        ans = num1*num2
    elif operator == 2:
        ans = num1/num2
    elif operator == 3:
        ans = num1 + num2
    elif operator == 4:
        ans = num1-num2
    return ans
ans = calculate()
if ans%1 == 0:
    print(str(int(ans)))
else:
    print(str(ans))
more = input("do another? (y/n)")
while more == "y":
    ans = calculate()
    if ans%1 == 0:
        print(str(int(ans)))
    else:
        print(str(ans))
    more = input("do another? (y/n)")
print("good calculating!")
