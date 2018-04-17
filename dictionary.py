Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print ("\n\t\t Kitchen Equipments \n\t\t  BASIC INFORMATION ABOUT: \n\n 1.Kitchen Knife \n 2. Cast iron Pan \n 3. Stove \n 4. Gas Tank \n 5. Spoon and Fork")
def hey():
     
    tutor = {"1":"Item: Kitchen Knife \nQuantity: 10","2":"Item: Cast Iron \nQuantity: 10","3":"Stove \nQuantity: 3","4":"Item: Gas Tank \nQuantity: 9","5":"Item: Spoon and Fork \nQuantity: 1000",}

    kitchen = input("\n Enter Item Number :  ")
    if kitchen == 1:
        print tutor["1"]
    elif kitchen == 2:
        print tutor["2"]
    elif kitchen == 3:
        print tutor["3"]
    elif kitchen == 4:
        print tutor["4"]
    elif kitchen == 5:
        print tutor["5"]
   
    else:
        print ("No name matched with the no. you've entered!!!")
        return hey()
    return hey()

    
hey()
