# trying to learn lists, tuples, sets and dictionaries
print("---------------------")
print("Lists!")
print("---------------------")
thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist[0] = "Mango"
print(thislist)

if "Mango" in thislist:
  print("Yes, 'Mango' is in the fruits list")

print(len(thislist))

thislist.append("orange")
print(thislist)

print("---------------------")
print("Touples!")
print("---------------------")
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
  


print("---------------------")
print("Sets!")
print("---------------------")
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)



print("---------------------")
print("Dictuionary!")
print("---------------------")

cost = 63.13

thisdict =	{
  "Twenty": 0,
  "Ten": 0,
  "Five": 0,
  "One": 0,
  "Quarter": 0,
  "Dime": 0,
  "Nickel": 0,
  "Penny": 0
}


while cost > 0:
    while cost >= 20:
        thisdict["Twenty"] +=1
        cost -= 20
    while cost >= 10:
        thisdict["Ten"] +=1
        cost -= 10
    while cost >= 5:
        thisdict["Five"] +=1
        cost -= 5


    cost = 0

for x, y in thisdict.items():
  if y != 0:
      if y >1:
          print(y , x +"s", end = " ")
      else:
          print(y , x, end = " ")
    
