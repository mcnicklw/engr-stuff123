inty = int(input("Please enter a positive integer: "))
print ("The factors of",inty,"are:")
for int in range(1,inty+1):
    if inty % int == 0:
        print(int)