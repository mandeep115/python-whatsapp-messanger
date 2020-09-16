# Created at Tue Sep 15 12:47:36 2020 ⏲
# By. Mandeep
# Auto Whatsapp message sender 🚀
# Check end of the code for message cheat-sheet

import webbrowser
import keyboard
import time
import csv

numbers = []  # We will store our numbers here

# # Going to open csv file
# with open("docs/names.csv", 'r') as file:  # Fancy way to open files

#     reader = csv.reader(file)  # Reader now has each line of csv file

#     # Uncomment this to limit number of peoples
#     # i = 0
#     for row in reader:  # We will itrate over every line 🔁

#         # Replace with number of people you want to send message
#         # if i > 8:
#         #     break

#         # Our last col is of numbers so we will append that col to our numbers array
#         numbers.append(row[-1])
#         # This line for limiting peoples
#         # i = i + 1

# # 1st row is of heading in our csv file so we will cut 1st row 🔢
# numbers = numbers[1:]

message = r'''
*Dear student,%0AYou have successfully registered for Preliminary Workshop of Eureka! Junior 2020 Competition.%0A%0ADate: 20th September%0ATime: 03:00 PM - 04:30 PM%0A%0ARequirement: Google Meet App%0A%0ATo attend the workshop you will get a Google Meet link on 19th September on your registered e-mail and whatsapp number.%0A%0ARegards,%0ATeam E-Cell, SSGMCE
'''  # Enter message that you want to send

# Now comes the juciy part
for number in numbers:  # Loop over numbers array 🔁
    # using Whatsapp api and webbrowser
    webbrowser.open(
        f'https://api.whatsapp.com/send?phone=+91{number}&text={message}')
    # giving our system time to open chrome
    time.sleep(10) # Increase the time of sleep if your internet or System is slow
    keyboard.press_and_release('enter')


# We are using an api in a way which it was not meant to be used
# we can't just type our message and expect it to work as normal
# message, as the message will be converted to an url and all
# it's rich text will be lost.

# SO! we are going to use URL Encoding Reference to emuilate some
# special charecters.

#### In a nutshell just use %0A before every next line ####

# Here's a list of things you might find usefull

# %03   Enter (carriage return)
# %0A   line feed (Works same as enter)

# For a full-list visit https://www.w3schools.com/tags/ref_urlencode.ASP
