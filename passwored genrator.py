#impor string moudule and ramdoum
#store all character in list (lowercase uppercase digits punctuaion)
#take input number from user 
# make sure the number of character is 6 or more
# shuffle all list
# calculate 30% and 20% of number letter 
# create password 60% letter and 40% digitals and puncation 

import string
import random

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list (string.punctuation)

character_number= input("how many character for the password : ")

while True :
    try:
        character_number = int(character_number)
        if character_number<6:
            print(" you need at leat 6 character : ")
            character_number= input("how many character dor the password : ")
        else:
            break
    except:
        print(" please enter the numbers only")
        character_number= input("how many character dor the password : ")   

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1 = round(character_number * (30/100)) 
part2 = round(character_number * (20/100))

password = []

for i in range(part1):
    password.append(s3[i])
    password.append(s2[i])

for i in range(part2):
    password.append(s1[i])
    password.append(s4[i])

random.shuffle(password)
password = "".join(password[0:])
print(password)