string = "Hello,World"
print(string.upper())
print(string.capitalize())
print(string.split(','))


x = "Insert the string in between 1 {a} 2 is {b} ".format(a="AND", b=1.5)
print(x)

#Defininig list which is equivalent to arrays
#list can have mixed data types
myListMix = ["abcdefdg",1,1.5,True]
myListInt = [1,2,3]
print(myListMix)
print(myListInt)

#print length of the list
print(len(myListMix))

#Indexing in the list starts with 0
print("my first item in the list before assigning new item is " + myListMix[0])

myListMix[0] = "Meaningful item"
print("my first item in the list after assigning Meaningful item is " + myListMix[0])

#to append a list to the end of the list

listToAppend = ["New appended list"]
myListMix.append(listToAppend)

print( myListMix)


#to extend a list to the end of the list
listToAppend = ["New appended list"]
myListMix.extend(listToAppend)

print( myListMix)

# to remove an item from the list pop method on the list is used, It returns a list so it has to be assigned to a variableself.
popItem = myListMix.pop()

print("print the list after the pop")
print(myListMix)

#pop the item from a particular position. It takes index 0 based. so, essentially 3rd is the 4th item in the list.

popItem = myListMix.pop(3)

print("print the list after the pop of 3rd item in the list")
print(myListMix)


# Reversing the list
myListInt.reverse()

print("after the reversal of the list " )
print(myListInt)

myListMix.reverse()

print("after the reversal of the list " )
print(myListMix)

# python doesn't support to sort the list which has mix data types.

#myListMix.sort()
#print("after the sorting of the list " )
#print(myListMix)


# how to access nestedl lists

nestedList = ['a','b','c',['d','e','f',['g','h']]]
print(" First nested list is")
print(nestedList[3])

print("Sub nested list insdie the nested list is")
print(nestedList[3][3])

print("Sub-Sub nested first item insdie the Sub nested list is")
print(nestedList[3][3][0])


# List comprehension

# Dictionary

myDict = {"username":"password","address1":"bangalore", "key3": [1,2,3]}

print("username value is ")
print(myDict["username"])

# to access the list members from within the dictionary
# to add a new key value pair to the dictionary
print("key3 is ")
print(myDict["key3"][1])


myDict["newkeyadded"]="I am new"
print("key3 is ")
print(myDict["newkeyadded"])

print(myDict)

# Learn Tuples

myTuple=('1','2','4')
print ("my tuple is")
print (myTuple)

myTuple=('5','62','46')
print ("my tuple after reassignment is")
print (myTuple[0])

print ("length of myTuple is")
print(len(myTuple))

print ("length of myListMix is")
print(len(myListMix))

print ("myListMix is")
print(myListMix)

#Define sets
mySet = set()

mySet.add(1)
mySet.add(1)
mySet.add(2)

print("mySet is ")
print(mySet)
mySet.discard(1)
print("mySet is after removing 1 is")
print(mySet)
# try to mutate the tuple popItem
#myTuple[0] = "try changing the value"

#print (myTuple)

#try to assign a list to set element

mySetWithList = set([1,1,1,2,3,4,5])
#mySetWithList.add([5,5,6,6,7])
print (mySetWithList)

mySetWithList.add(10)
print (mySetWithList)


# Learn if else elif Statements

num1 = 10
num2 = 20

if num1<10:
    print("Less than 10")
elif num1>10:
    print("More than 10")
else:
    if num2==20:
        print("evanluated 20")

    print("num1 is exactly 10")

# Working on LOOPS
print("work on loops")

lst = [1,"gagan",4,5,6,7]

print ("loop on list")
for lstitem in lst:
    print(lstitem)

print("loop on dictionary")

dictLoop = {"key1":"value1", "key2":"value2"}

for dictItem in dictLoop:
    print(dictLoop[dictItem])


# Iterating through Tuples

print (" Iterating through Tuples")

myTuple = (1,2,3,5,6,"try text in tuple")

for tuplei in myTuple:
    print(tuplei)

print("tuple printing")

myTuple = (1,2)

for tupleItem in myTuple:
    print(tupleItem)


print("tuple printing that are enclosed in a list")

myListWithTuples = [(1,2),(3,4),(5,6)]

for tupleItem in myListWithTuples:

    for tupleSubItem in tupleItem:
        print(tupleSubItem)

    print(tupleItem)

print("tuple unpacking")

myTuplePacked = [('1','2'),(3,5), (4,5)]

for (unPackedTuple1,unPackedTuple2) in myTuplePacked:
    print("Unpacked tuple1 is")
    print(unPackedTuple1)
    print ("Unpacked tuple2 is")
    print(unPackedTuple2)
    #    print("Unpacked tuple3 is")
    #    print(unPackedTuple3)


print("while loops in action")

i = 1

while i < 11:
    print(i)
    i = i + 1


print("use range. Range doesn't include the last number so always add an extra number to the end if that number is needed")

range(0,5)
print(range(5,10,2))
print("list or range")
print(list(range(5,22,2)))


for item in range(5,10,2):
    print(item)


print("Lets run functions")


def myFunc(param1):
    print("this is my first function")

print("calling the function")
myFunc(10)

print("LEARN THE DOCTRING. DOCSTRING IS TO DOCUMENT THE CODE IN FUNCTION. ITS DENOTED WITH THREE DOUBLE QUOTES AND END WITH 3 DOUBLE QUOTES")

def myFunc(param2):
    """
    THIS IS DOCSTRING AND IT DOESN'T EXECUTE.
    adssf
    adfsdf
    adfsfdfs
    """
    print("I am inside the myFunc with docstring")

myFunc(10)

print("return the values from function")
def myFuncRet(Param1):
    if type(Param1) == type(10):
        return Paraam1 + 10
    else:
        return "Please input integers"

print(myFuncRet("gagan"))

print("Use type() function to return the data type of the variable")

print(str(type(mySet)) + " data type is returned")

typeInfo = type(mySet)

def checkSequence(lst):

    for seq in range(len(lst)):
        print("seq value is " + str(seq))
        print(lst[seq])
        if seq <= len(lst) - 2:
            if lst[seq] == 1 and lst[seq+1] == 2 and lst[seq+2] == 3:
                print("sequence exists on index numbers " + str(seq) + " and " + str(seq+1) + " and " + str(seq+2))
                seqExists = True
                break
        else:
            seqExists=False
    if seqExists == True:
        print("Sequence 123 exists")
    else:
        print("sequence 123 doesn't exist")

checkSequence([1,2,4,1,2,3])

#Print the alternate string
def printAlternateString(str1):
    for seq in range(0, len(str1), 2):
        print("character at sequence " + str(seq) + " is " + str1[seq])

printAlternateString("Heelllloo")

def checkStrEnd(str1, str2):
    if str1[-3:].lower() == str2[-3:].lower():
        print("strings have equal last 3 characters")
    else:
        print("str1 is " + str1 + " str2 is " + str2)

checkStrEnd("manabc", "namabc")


def checkStrEnd1(str1, str2):
    print(str1[-len(str2):].lower() == str2.lower() or str2[-len(str1):].lower() == str1.lower() )
    print (str1[-len(str2):].lower())
    print(str2.lower())
checkStrEnd1("manabc", "hellomanabdbc")

# How classes work in Python
class author():
    def __init__(self,name,address):
        self.name1 = name
        self.address1 = address

newAuthor = author(name="gagan",address="bangalore")

print (newAuthor.name1 + newAuthor.address1)

class mathematics():
    blaassigned = 0

    def __init__(self, bla1, bla2):
        mathematics.blaassigned = bla1

    def addition(a,b):
        return a + b


print("blaassigned is " + str(mathematics.blaassigned))

mathematics.blaassigned = 5

print("blaassigned is " + str(mathematics.blaassigned))

print(mathematics.addition(3,2))

# inheritance

class Animal():
    def __init__(self,animalType):
        self.animalType = animalType
        print("animal created")

    def eat(self):
        print("Animal Eating")


class Dog(Animal):
    def __init__(self,dogType):
        Animal.animalType = "Dog"
        self.dogType = dogType
        print("Dog Created")

# overriding the eat method
    def eat(self):
        print("Dog Eating instead of animal")

myDog = Dog("Labrador")
print(myDog.animalType)

myDog.eat();

## SPECIAL functions
##THEY START AND END WITH DOUBLE UNDERSCORE

class book():
    def __init__(self, bookName, bookAuthor, bookLength):
        self.bookName = bookName
        self.bookAuthor = bookAuthor
        self.bookLength = bookLength

    def __str__(self):
        return "Object Book has Title: {}, Author: {}, Length: {}".format(self.bookName, self.bookAuthor, self.bookLength)

    def __len__(self):
        return self.bookLength


myBook = book(bookName="Financial Management", bookAuthor="Gilbert", bookLength=568)
print("Length of myBook object is "+ str(len(myBook)))
