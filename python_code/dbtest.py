InfoDB = []
Shaurya = {
# These records are of String type
"FirstName": "Shaurya",
"LastName": "Goel",
"DOB": "October 29, 2007",
"Residence": "San Diego",
"Email": "shauryaggamer@gmail.com",

# These records are of lists type
"Owns Cars": ["None"],
"Owns Devices": ["iPhone", "Gaming laptop"],
"Hobbies": ["Football", "Soccer", "Video Games"]
}

TomB = {
# These records are of String type
"FirstName": "Tom",
"LastName": "Brady",
"DOB": "Auguest 3, 1977",
"Residence": "Tampa Bay",
"Email": "info@brandbrady.com ",

# These records are of lists type
"Owns Cars": ["2017 Aston Martin DB11", "2015 Rolls Royce Ghost", "2018 Limited Edition TB12 Aston Martin Vanquish S Volante", "2015 Ferrari M458-T", "2009 Audi R8"],
"Owns Devices": ["iPhone", "Gaming laptop"],
"Hobbies": ["Football", "Cars"]
}

InfoDB.append(Shaurya)
InfoDB.append(TomB)

print("Iterating using key / value")

# iterate over the list of items in InfoDB list
for x in InfoDB:
    # iterate over the dictionary key - values in the items within the list (InfoDB)
    for key in x:
        print(str(key) + " : " + str(x[key]))



print("iterting using index")
# x is an integer variable
# len(InfoDB) returns length of InfoDB as an integer
# range command returns a sequence of numbers, starting from 0 by default and ends (in this case) with the length of InfoDB
for x in range(len(InfoDB)):
    # getting the dictionary stored at index position x. Naming it item
    item = InfoDB[x]
    # printing out every key and value in the dictionary using y as the index
    for y in range(len(item)):
        print(list(item)[y] +" : " + str(list(item.values())[y]))

print ("iterating using while")

# printing out every key and value in the dictionary using x as the index