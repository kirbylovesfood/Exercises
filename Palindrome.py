Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def isPalindrome():
    string = input('Enter the string: ')
    string1 = string[::-1]
    if string[0] == string[(len(string)-1)] and string[1:(len(string)-2)] == string1[1:(len(string)-2)]:
            print('This is a palindrome')
    else:
        print('This is not a palindrome')
isPalindrome()
