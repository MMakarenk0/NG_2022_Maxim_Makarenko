number = int(input("Enter number: ")) #Input number for calculation.
decr = number
i=1
factorial = 1
while decr>0:
    factorial=factorial*i #Calculation of factorial. 
    i=i+1
    decr=decr-1
print("Factorial of " + str(number) + " is: " + str(factorial)) #Output factorial. 