Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def counting_numbers_description():
    print "the counting numbers are:"

def counting_numbers():
    counting_numbers = [1, 2, 3, 4, 5, 6, 7]
    counting_numbers.append(8)
    print counting_numbers

def  odd_numbers_description():
    print "the odd numbers are:"

def odd_numbers():
    odd_numbers = [1,3,5,7,9,11]
    odd_numbers.remove(11)
    print odd_numbers

def even_numbers_description():
    print "the even numbers are:"

def even_numbers():
    even_numbers = [2,4,6,8,12]
    even_numbers.append(10)
    even_numbers.pop(4)
    print even_numbers

print counting_numbers_description()
print counting_numbers()
print odd_numbers_description()
print odd_numbers()
print even_numbers_description()
print even_numbers()
