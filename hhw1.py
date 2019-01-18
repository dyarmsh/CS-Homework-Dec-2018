def hcfinder():
    num1 = int(input("enter number"))
    num2 = int(input("enter number"))
    if num1 > num2:
        least = num2
    else:
        least = num1

    for hcf in range (1, least+1):
        if((num1 % hcf == 0) and (num2 % hcf == 0)):
            print (hcf)

    print ("the last number displayed is the hcf")

hcfinder()
            

