# Moving Items from a list to another , While Loop

# list contain the users , and emty one to add the verified
unconfirmed_users = ['reem', 'hanaa', 'ziad']
confirmed_users = []

while unconfirmed_users: #as long as "unconfirmed_users" contain items --> True
    current_user = unconfirmed_users.pop()
    
    print(f"confirming user {current_user.title()}")
    confirmed_users.append(current_user)
    
print(f"\nThe list of verified Users: \n")  
for confirmed_user in confirmed_users:
    print(confirmed_user.title())  

############################################################

# removing instances of an item in a list using while 
pets = ['cat','dog','fish','cat','goldfish','cat']
print(f"\n{pets}")

while 'cat' in pets:
    pets.remove('cat')

print(pets)

############################################################
#Polling

responses = {} #emoty dictionary to store --> 'name': 'response'

poolling_active = True # to use for the while loop

while poolling_active:
    name = input("\nEnter Your Name: ")
    response = input("What city you wish to live on? ")
    responses[name] = response # key is 'name' value 'response'
    contitnue_is = input("You want to answer again (YES/NO)? ")
    if contitnue_is == 'no' or contitnue_is == 'NO':
        poolling_active = False

# poll result
for name, res in responses.items():
    print(f"\n{name} wishes to visit {res}\n")
