
def is_prime(num):
    
    value = 0
    
    for i in range(2,num):
        if(num%i == 0):
            value = value+1
        # else:
        #     value = True
    if (value>=1):
        return False
    else:
        return True
#
# Write your code here.
#

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()


expeted output:

2 3 5 7 11 13 17 19