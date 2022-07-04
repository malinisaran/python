number = int(input("Enter the Number for Mulitiplication Table:"))
print("The multiplication Table of:",number)

for count in range(1,11):
    print (number,'x',count,'=',number*count)