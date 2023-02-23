current_users=['Unknown','Preston','Brianna','Youtube','Discover']#list of current users

new_users=['poop','Preston','urfriend','Brianna','Justin']#list of new users
for name in new_users:#uses for loop to see if any new names are in current_users
    if name in current_users:#if statement showing what should happen if the name is in current_userssss
        print ('sorry but that name is unavailable and currently being used by another player')
    else:#else statement showing what should happen if the name is not in current users
        print('That name is available!')
