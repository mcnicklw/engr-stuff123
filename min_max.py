num_int = int(input("How many integers would you like?"))
print("please enter", num_int, "integers")
min = 9223372036854775807
max = -9223372036854775807
for i in range(0,num_int):
    numbie = int(input())
    if numbie > max:
         max = numbie
    if numbie < min:
        min = numbie
print ("min:",min)
print ("max:",max)