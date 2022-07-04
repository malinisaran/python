Lower_range = int(input("Enter the Lower Range:"))
Upper_range = int(input("Enter the Upper Range"))

print("The Prime Numbers in the Range are: ")

for number in range(Lower_range,Upper_range + 1):
    if number > 1:
        for i in range(2,number):
            if(number % i) ==  0:
                break
        else:
            print(number)
