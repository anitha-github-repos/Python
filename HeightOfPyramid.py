blocks = int(input("Enter the number of blocks: "))
height = 0
layer = 0
used_blocks = 0

# Write your code here.

while (blocks>0):
    
    layer = layer+1
    if blocks <= used_blocks:
        break
    #if blocks < used_blocks:
        #break
    height = height+1
    #used_blocks +=layer
    used_blocks = used_blocks+1
    blocks = blocks-used_blocks
    
#	

print("The height of the pyramid:", height)

#Just for practice 

print("practice session")