from IPython.core.display import display, HTML

InfoDB = []
Shaurya = {
# These records are of String type
"FirstName": "Shaurya",
"LastName": "Goel",
"DOB": "October 29, 2007",
"Residence": "San Diego",
"Email": "shauryaggamer@gmail.com",

# These records are of lists type
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

def showValue(dic, key):
    if (key in dic):
        display(HTML ("<td>" + str(dic[key]) + "</td>"))
    else:
        display(HTML ("<td> </td>"))

# printing using specific keys, check if the key exists, otherwise don't print
display(HTML('<table>'))
for x in InfoDB:
    # iterate over the dictionary key - values in the items within the list (InfoDB)
    display(HTML('<tr>'))
    showValue(x,"FirstName")
    showValue(x,"LastName")
    showValue(x,"DOB")
    showValue(x,"Email")
    showValue(x,"Owns Cars")
    showValue(x,"Owns Devices")
    showValue(x,"Hobbies")    
    display(HTML('</tr>'))

display(HTML('</table>'))