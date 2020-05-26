#-------------------------------------------------------------------------#
#                1 Exercises with lists
#-------------------------------------------------------------------------#
from pip._vendor.distlib.compat import raw_input
l=[1, 4, 9, 10, 23]
print(l)
count=len(l)
print(count)

#1. Using list slicing get the sublists [4, 9] and [10, 23].
sublist=(l[1:3]),(l[3:5])
print(sublist)

#2. Append the value 90 to the end of the list "l". Check the difference between list concatenation and the "append" method.
l.append(90)
print(l)
# 2 approach
l[len(l):]=[90]
print(l)

#3. Calculate the average value of all values on the list. You can use the "sum" and "len" functions.
sumlist=sum(l)
print(sumlist)
#4. Remove the sublist [4, 9].
#print(l.remove[1])
del l[1:3]
print(l)
#-------------------------------------------------------------------------#
#                2 Input and Print the multiple values with order
#-------------------------------------------------------------------------#
#urinput = input("Enter Ur Inputs:-")
#aa= sorted(urinput, key=None, reverse=False)
#a = sorted(urinput.split(),key=str.lower())
#print("Value Is:-",aa)
# Taking multiple inputs
#lsits=list(map(int,input""))
l_1 = list(map(str, input("Enter multiple values:-").split(',')))
#str_reverse = ''.join(sorted(l_1,key=None, reverse=False)) #   (sorted(l_1))
str_reverse = sorted(l_1)#,key=None, reverse=False)
join_str_reverse = ','
print("The values of input are: - ", join_str_reverse.join(str_reverse))

#-------------------------------------------------------------------------#
#                3 Accepts sequence of lines as input and prints the
#                lines after making all characters in the sentence capitalized
#-------------------------------------------------------------------------#
while True:
    a=input("Enter Ur Inputs:-")
    print(a.upper())
    s =input("Contiune!! Y Or N :- \n")
    if s != 'Y':
        break
else:
    print("Ended the While....!")
#-------------------------------------------------------------------------#
#                   Exercises with dictionaries
#-------------------------------------------------------------------------#
ages = {"Peter":10,"Isabel":11,"Anna":9,"Thomas":10,"Bob":10,"Joseph":11,"Maria":12,"Gabriel":10}
#1. How many students are in the dictionary? Search for the "len" function.
print("They are ", len(ages) ,"students in the dictrionary!")
#2.dictionary as parameter and return the average age of the students
countofdir = len(ages)
print(countofdir)
v=0
sum=0
oldestage=0
for k,v in ages.items():
    sum += v
    print(k,":",v)
    #print(list(ages.items())[k][int(v)])
    print("Sum Of the Ages:-",sum)
print("Averages Is!",sum/countofdir)
#3. Implement a function that receives the "ages" dictionary as parameter and returns the name of the oldest student.
ages = {"Peter":10,"Isabel":11,"Anna":9,"Thomas":10,"Bob":10,"Joseph":11,"Maria":12,"Gabriel":10}
maxage=max(ages.values())
for k,v in ages.items():
    if v == maxage:
        print("Returns the name of the oldest student!",k, ":", v)
        break
#4. Implement a function that receives the "ages" dictionary and a number "n" and returns a new dict where each student is n years older. For instance, new_ages(ages, 10) returns a copy of "ages" where each student is 10 years older.
for k,v in ages.items():
    print("Each student is 10 years older!",k,":",v+10)