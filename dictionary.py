Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print ("\n\t\t Kitchen Equipments \n\t\t  BASIC INFORMATION ABOUT: \n\n 1.Kitchen Knife \n 2. Cast iron Pan \n 3. Stove \n 4. Gas Tank \n 5. Spoon and Fork")
def hey():
     
    tutor = {"1":"Item: Power Supply \nQuantity: 10","2":"Item: Soldering Iron \nQuantity: 18","3":"Item: Power Extension \nQuantity: 12","4":"Item: Drill \nQuantity: 5","5":"Item: Pliers \nQuantity: 12",}

    mike = input("\n Enter Item Number :  ")
    if mike == 1:
        print tutor["1"]
    elif mike == 2:
        print tutor["2"]
    elif mike == 3:
        print tutor["3"]
    elif mike == 4:
        print tutor["4"]
    elif mike == 5:
        print tutor["5"]
   
    else:
        print ("No name matched with the no. you've entered!!!")
        return hey()
    return hey()

    
hey()
