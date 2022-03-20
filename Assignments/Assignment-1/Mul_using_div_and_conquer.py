   
def mul_using_div_and_conquer():
    n = 0
    b = str(input("Enter the first number: "))
    l1 = []
    a1 = ""
    ao = ""


    d = str(input("Enter the second number: "))

    l2 = []
    b1 = ""
    bo = ""


# These two loops are to append the both numbers in the list 
    for i in b: 
        l1.append(i)


    for i in d:
        l2.append(i)

"""This check is to check if from both inputs the length of any input will be odd it will 
    automatically add 0 to the 0th index of the list """   

    if(len(l1)%2!=0):
        l1.insert(0,"0")

    if(len(l2)%2!=0):
        l2.insert(0,"0")

# If the length of both numbers will be same then we will get the "n" which will be used in formula


    if(len(l1)==len(l2)):

            n = len(l1)
# If the length will not be same then this logic will make the lenght og both numbers same
    else:
        if(len(l1)>len(l2)):
            z = len(l1)
            k = len(l2)
            f = z-k

            for i in range(f):
                l2.insert(i,"0")

        elif(len(l1)<len(l2)):
            z = len(l2)
            k = len(l1)
            f = z-k
            for i in range(f):
                l1.insert(i,"0")

        if(len(l1)==len(l2)):
            n = len(l1)
        else:
            print("There is something wrong!!!")

#Dividing the number(input1) in two parts 
    
    for j in range(len(l1)//2):
        a1 += l1[j] 

    for k in range(len(l1)//2,len(l1)):
        ao += l1[k] 

#Dividing the number(input2) in two parts


    for i in range(len(l2)//2):
        b1 += l2[i] 

    for i in range(len(l2)//2,len(l2)):
        bo += l2[i] 

"""The number we broke was actually in the string form.Now we have to use breaked numbers into 
into the formula so we will change the type of divided numbers!!!""" 
    
    a1 = int(a1)
    ao = int(ao)
    b1 = int(b1)
    bo = int(bo)


    formula = ((a1*b1)*(10**n)) + (a1*bo+ao*b1)*(10**(n//2))+ao*bo

    print("The Multiplication of ",b,"and",d,"using divide and conquer is",formula)

    
mul_using_div_and_conquer()
