# Ask for enter the number from the use  
Number = int(input("Enter the Number:"))

# Initiate value to null  
rev = 0

while(Number>0):

     # Logic  
    rem = Number%10
    rev = (rev * 10)+ rem
    Number = Number//10

# Display the result  
print("The Reverse Number is :{}".format(rev))



# for example
# Reminder = number %10
# Reminder = 12345%10 = 5
# Reverse = Reverse *10 + Reminder Initial value of revs_number is null
# Reverse = 0 * 10 + 5 = 0 + 5 = 5
# Number = Number //10
# Number = 1234 //10 = 1234 // Now loop will iterate on this number. 