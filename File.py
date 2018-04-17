Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> text_file = open("text.txt",'o')
text_file.write("Hi ! Welcome to my World !")
text_file.close()
text_file = open("text.txt",'x')
text_file.write(" in Data Structure")
text_file.close()


# to display in run!
# text_file = open("text.txt",'r')
# print(text_file.read())
# text_file.close()
