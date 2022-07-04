year = int(input("Enter the Number:"))
def leap_year(year):
    if((year  % 400 == 0 ) or
    (year % 100 !=0) and 
    (year % 4 == 0)):

  
        print("Given Number is a Leap Year")

    else:
        print("Given Number is Not a Leap Year")

# year = int(input("Enter the Number:"))

leap_year(year)
