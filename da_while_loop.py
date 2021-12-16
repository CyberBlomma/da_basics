import math

gafunken = True

while gafunken:
    print("'a' or 'b' for epic win, 'stop' for stop")
    command = input()
    
    if command.lower() == "a":
        print("din mor")
        
    elif command.lower() == "b":
        print("har skor")
        
    elif command.lower() == "stop":
        gafunken = False
        
    else:
        print("input 'a' or 'b'")

if gafunken == False:
    print("lmao sämst")