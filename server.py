import urllib.request
import sys

print("                   \033[44;11m Auther Name- Imran Ahmed \033[m")
print ("                         version- 0.0.1")
print("----------------------------------------")

url= input("Enter The Full Name Of Target Website :- ")
url.rstrip()
header = urllib.request.urlopen(url).info()
print (str(header))
