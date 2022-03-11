#!/usr/bin/env python3

#Author:
print("Ashley Bryant")

#Purpose: To demonstrate the use of counters, while loops, dictionaries, if-else statements, accepting inputs, etc.

password_database = dict()
password_database = {'Username':'dnedry','Password':'please'}

command_database = dict()
command_database = {'reboot    ':'Ok. I will reboot all park systems.','shutdown    ':'I will shut down all park systems.','done    ':'I hate all this hacker stuff.'}

white_rabbit_object = 0
counter = 0

while counter < 3:
    counter += 1

    input_user = input('Enter your username:')
    input_password = input('Enter your password:')

    if (input_user == password_database['Username']) and \
        (input_password == password_database['Password']):
        white_rabbit_object = 1
        print('Hi, Dennis. You\'re still the best hacker in Jurassic Park.')
        input_command = input("Please enter a command [command_database_keys:(['reboot', 'shutdown', 'done'])]:")
        if input_command == 'reboot':
            print(command_database['reboot    '])
        elif input_command == 'shutdown':
            print(command_database['shutdown    '])
        elif input_command == 'done':
            print(command_database['done    '])
        else:
            print('The Lysine Contingency has been put into effect.')
if counter == 3:
    print('You didn\'t say the magic word \n'*25)
