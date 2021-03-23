import random
import os
import time
a1 ="please spin again :>" # this is the string that comes up when u chosse a choice that is nothing, in a way its like customizaition so you dont "have" to have 12 choices, but if u want more just tell me or adjust it yourself

def clear():
    os.system('clear')
# these are you choices, 
#you can also put links here, just do  "str" +"link adress"


c1 = "Coconut Song: ""https://www.youtube.com/watch?v=w0AOGeqOnFY"  
c2 = "Coconut Song: ""https://www.youtube.com/watch?v=w0AOGeqOnFY"  
c3 = "Coconut Song: ""https://www.youtube.com/watch?v=w0AOGeqOnFY"
c4 = "Coconut Song: ""https://www.youtube.com/watch?v=w0AOGeqOnFY"
c5 = "Coconut Song: ""https://www.youtube.com/watch?v=w0AOGeqOnFY"
c6 = "Coconut Song: ""https://www.youtube.com/watch?v=w0AOGeqOnFY"
c7 = "Coconut Song: ""https://www.youtube.com/watch?v=w0AOGeqOnFY"
c8 = "Coconut Song: ""https://www.youtube.com/watch?v=w0AOGeqOnFY"
c9 = "Coconut Song: ""https://www.youtube.com/watch?v=w0AOGeqOnFY"
c10 = "Coconut Song: ""https://www.youtube.com/watch?v=w0AOGeqOnFY"
c11 = "Coconut Song: ""https://www.youtube.com/watch?v=w0AOGeqOnFY"
c12 = "Coconut Song: ""https://www.youtube.com/watch?v=w0AOGeqOnFY"

github = ""


update = "upsized the spin numbers " 

update_version = 'Running on Wheel version 1.02:'

#im probaly gonna get rid of this
print ("|         |\n\n\n\n \________/")
print("\n\n\n\n\n Booting...")
time.sleep(3)
clear()
print ("_         _\n\n\n\n \________/")
print("\n\n\n\n\n Booting...")
time.sleep(.5)
clear()
print ("|         | \n\n\n\n \________/")
print("\n\n\n\n\n Booting...\n\n\n")

print (update_version)
print (update)


three = "██████╗░\n╚════██╗\n░█████╔╝\n░╚═══██╗\n██████╔╝\n╚═════╝░"
two = "██████╗\n╚════██╗\n░░███╔═╝\n██╔══╝░░\n███████╗\n╚══════╝"
one = "░░███╗░░\n░████║░░\n██╔██║░░\n╚═╝██║░░\n███████╗\n╚══════╝"

spinning = "░██████╗██████╗░██╗███╗░░██╗██╗███╗░░██╗░██████╗░░░░░░░░░░\n██╔════╝██╔══██╗██║████╗░██║██║████╗░██║██╔════╝░░░░░░░░░░\n╚█████╗░██████╔╝██║██╔██╗██║██║██╔██╗██║██║░░██╗░░░░░░░░░░\n░╚═══██╗██╔═══╝░██║██║╚████║██║██║╚████║██║░░╚██╗░░░░░░░░░\n██████╔╝██║░░░░░██║██║░╚███║██║██║░╚███║╚██████╔╝██╗██╗██╗\n╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝╚═╝╚═╝"


time.sleep (5)
clear()
print (spinning)
time.sleep(5)
clear()
print (three)
time.sleep(1)
clear()
print (two)
time.sleep(1)
clear()
print (one)
time.sleep (1)
clear()


if c1 == " ":
	c1 = a1

if c2 == " ":
	c2 = a1

if c3 == " ":
	c3 = a1

if c4 == " ":
	c4 = a1

if c5 == " ":
	c5 = a1

if c6 == " ":
	c6 = a1

if c7 == " ":
	c7 = a1

if c8 == " ":
	c8 = a1

if c9 == " ":
	c9 = a1

if c10 == " ":
	c10 = a1

if c11 == " ":
	c11 = a1

if c12 == " ":
	c12 = a1						

lista = [
	c1,
  c2, 
	c3, 
	c4, 
	c5, 
	c6, 
	c7, 
	c8, 
	c9, 
	c10, 
	c11, 
	c12]

print (random.choice(lista))
time.sleep (3)
