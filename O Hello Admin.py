virtualname=['Holly','Admin','Sibby','Seb','Marie']#list of people

for virtual in virtualname:#uses a loop to show it will repeat the names in that sentence, but if it gets to admin it's a special sentence

    if virtual=='Admin':#if block saying if virtual is = admin print Hi Admin, would you like a report statement on all users?
        print('Hi Admin, would you like a report statement on all users?')
    else:#else block saying if virtual is  not = admin print Hey {virtual} thank you for logging in :)
        print(f'Hey {virtual} thank you for logging in :)')