#Ingredient adjuster
#Thomas Powell Horan 2/19/21
#This program will calculate the specific amount of ingredients needed to bake a given amount of cookies imputed by the user
#first a quick introduction to what the program does and then we require an input
from turtle import width


desc = ("This is an ingredident calulator for baking cookies")
print("""\
*****************************************************************************************************************************************************
=====================================================================================================================================================
 ######   #######   #######  ##    ## #### ########     ######     ###    ##        ######  ##     ## ##          ###    ########  #######  ########  
##    ## ##     ## ##     ## ##   ##   ##  ##          ##    ##   ## ##   ##       ##    ## ##     ## ##         ## ##      ##    ##     ## ##     ## 
##       ##     ## ##     ## ##  ##    ##  ##          ##        ##   ##  ##       ##       ##     ## ##        ##   ##     ##    ##     ## ##     ## 
##       ##     ## ##     ## #####     ##  ######      ##       ##     ## ##       ##       ##     ## ##       ##     ##    ##    ##     ## ########  
##       ##     ## ##     ## ##  ##    ##  ##          ##       ######### ##       ##       ##     ## ##       #########    ##    ##     ## ##   ##   
##    ## ##     ## ##     ## ##   ##   ##  ##          ##    ## ##     ## ##       ##    ## ##     ## ##       ##     ##    ##    ##     ## ##    ##  
 ######   #######   #######  ##    ## #### ########     ######  ##     ## ########  ######   #######  ######## ##     ##    ##     #######  ##     ## 
=====================================================================================================================================================                    
*****************************************************************************************************************************************************                                    
                    """)
print(desc.center(width))

cookies_ammount =float(input("please enter the amount of cookies that you would like to bake: "))

#here is a quick loop that will keep out program from breaking from the wrong input
#the loop will end the program if a number less than 0 is entered and it will end if the input is a string 
if cookies_ammount >= 0:
    cookies_ammount=cookies_ammount#since the cookie ammount is already floating point we dont do anything to it

    if cookies_ammount < 0:#here we check that the number is not less than zero because we cant make a negative amount of cookies
        print ("please type a number larger than zero or larger next time")
        quit()
else:
    print("please type an number next time")#here we are checking to make sure that the input is not a string or something else
    quit()


#here we will caluclate the per cookie ammounts for each ingredient according to the recipie

sugar = float(1.5/48)
butter = float(1/48)
flour = float(2.75/48)

#now we will use the per cookie values that we just calculated to figure out how much of each ingreedient we need for a given ammount of cookies

print(f'{cookies_ammount} cookies require:')
print(f'{cookies_ammount*sugar:.2f} cups of sugar')
print(f'{cookies_ammount*butter:.2f} cups of butter')
print(f'{cookies_ammount*flour:.2f} cups of flour')

exit= input("press E to exit ")

if exit.lower == "e":
    quit()

    
