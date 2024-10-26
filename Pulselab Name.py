def NameExtractor(Names):
    Names.strip() #to get rid of the whitespaces in my text input
    NameArray = []
    NumberOfCharacters = len(Names)
    for i in range NumberOfCharacters: #this loop identifies the commas in the text and adds each name between commas into array
        IndividualName = ''
        if Names[i] != ',':
            IndividualName = IndividualName + i
        else:
            NameArray.append(IndividualName)
            continue
    return NameArray

def NamePrinter():
    NameArray[] = NameExtractor(Names) #calls nameextractor function and initializes the returned array from nameextractor to NameArray[]
    global MessageType
    MessageType = input("Which message would you like? starter or follow up")
    if MessageType.lower() == starter:
        for FName in NameArray:
            print(f"Hey {FName}, I was wondering if you work with buyers or sellers?")
    else:
        print("call the FollowUp() function for a follow up :)")

def FollowUp(NameExtractor(Names)): #as follow ups won't be for all names so user can add just needed names required for follow up
    FNum = int(input("which follow up number would you like? 1-10"))
    if FNum = 1:













