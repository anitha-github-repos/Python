#Write your code below this line 👇
def prime_checker(number):
    reminder = 0
    for i in range(2,number+1):
        if number%i == 0:
            #print(i)
            reminder+=1
    if reminder == 1:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
def prime_checker2(number):
    prime_numbers = []
    for i in range(1,number+1):
        reminder = 0
        for j in range(2,i+1):
            if i%j == 0:
                reminder+=1
        if reminder == 1:
            prime_numbers.append(i)
    print(prime_numbers)   

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
prime_checker2(number=n)
