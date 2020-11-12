'''Write a recursive function called raise_power() that takes in two 
integer parameters, the first parameter being the base number and the second 
parameter being the power you want to raise it to. This function will return the number 
raised to the given power. For example, if you called raise_power(4, 2) you would get 16 
returned which is 4^2. Remember to think about what the base and recursive cases will be and 
start with an iterative approach if you don't know where to begin. '''

def raise_power(base, power):
    #base case, if the power is 1, the base numbeer doesnt change.
    if (power == 1):
        return base
    else:
        #if the power is greater than 1, the base number multiply itself until the power reaches 0
        return (base * raise_power(base, power-1))


print(raise_power(4,2)) #expect to see 16
