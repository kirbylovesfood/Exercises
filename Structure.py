Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> str = input("What's your favourite subject? ")
print "My favourite subject is", str.upper()
print "My favourite subject is", str.lower()

def reverse_string(abc):
    return ''.join(reversed(abc))
print(reverse_string(str))
