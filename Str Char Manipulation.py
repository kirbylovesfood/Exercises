Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> str = "Python is User-friendly"
str_split = str.split(" ")

print(str)

print(str.upper())
#to capitalize the string

print(str.lower())
#to put in lowercase the string

print(len(str))
print("the string is %d letter long" %len(str))
#to know the size of the string

print(str[0])
print(str[1])
print(str[2])
print(str[3])
print(str[4])
print(str[5])
#to call each and every letter in the index

print(str[0:6])
#to print everything in the range of index 0-6

print(str_split)
#to split it into term

print("Do you know that %s is not only cool but %s also %s" %(str_split[0],str_split[1],str_split[2]))

str1 = " and is so cool"
str2 = ". Python is a general-purpose interpreted, "
str3 = "interactive, object-oriented, "
str4 = "and high-level programming language"

print str + str1 + str2 + str3 + str4
