import math #för mer avancerad matte 

a  = 10 
# name = input("b?") 
# color = input("färg?")
name = "a"
color = "b"
print("funky " + color + " och " + name)
print(type(name))
print(a*name)
print('''Gefunken?
      
Nä''')


ord = ("långt och jobbigt")
print(ord[1]) #som om stringen är en array?
print(ord[-3]) #samma men från höger
print(ord[1:4]) #positionerna 1-4 i arrayen
print(ord[:4]) #samma som 0:4 
print(ord[:]) #hela ordet/arrayen

# first_name = "förnamn B)"
# last_name = "efternamn :("
# name = first_name + last_name
# print(name)

print(len(ord))
print(ord.upper())
print(ord.lower())

print(ord.find("t")) #hittar poisitionen för det första "t" i ord, ger 4, fungerar med hela ord också
print(ord.find("ö")) #blir ledsen för att den inte hittar "ö" i ord, ger -1

print(ord.replace("jobbigt", "SÄMST")) #ersätter "jobbigt" med "sämst", case sensitive
print("och" in ord) #hittar "och" i ord, ger bool
# ord = ""
# len()
# ord.upper()
# ord.lower()
# ord.title()
# ord.find()
# ord.replace()
# "..." in ord

print('''
      da basic maths!
      ''')
print(10 / 3) #10 / 3, ger float med decimaler
print(10 // 3) #10 / 3, ger int
print(10 % 3) #10 - 10 / 3, ger resten av 10 / 3, 1
print(10 ** 3) #10^3, ger 1000


x = 10
x += 3
print(x)

print('''
      abs o round
      ''')
y = 2.9
print(round(y)) #ger avrundat y
print(abs(y)) #ger absolutbeloppet, alltid >= 0

print('''
      le if-sats''')

temp = "hot"
hot = True

if temp == "hot" or hot:
    print("varm")

elif temp == "cold" or not hot:
    print("kall")

else:
    print("moment")

#and
#or
#not
#and not, or not

#<, <=, >, >=, =, ==, !=, samma som i c#

    
# function() 
# {
    
# }