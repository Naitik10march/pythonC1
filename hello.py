myname = "naitik"
print(myname)

myage = "14"
print(myage)

myfriendlist = ["ragu","yash","harman"]
print (myfriendlist[1])

pocketmoney = input("enter the pocket money you get : ")
print(pocketmoney)

age = int(input("enter your age : "))
if(age>18):
    print("you are an adult ,you can vote")
elif(age>12):
        print("you are a teenager")
else:
            print("you are still a kid")

myfriendlist = ["ragu","yash","harman"]
for friend in myfriendlist:
    print(friend)

count = 5
while (count>=0):
 print(count)
 count = count - 1    

pocketmoney = int(input("enter your pocketmoney you get every month : "))
if(pocketmoney>500):
    print("you are rich")
elif(pocketmoney>100):
        print("you have a good life")
else:
            print("I know how you feel")