def prime(num):
    if num>1:
        for i in range(2,int(num/2) + 1):
            if(num % i) == 0:
                print(num,"Not an Prime Number")
                break
        else:
            print(num,"is an Prime Number")

    else:
        print(num,"Not an Prime Number")

num =int(input("Enter the Number:"))

prime(num)