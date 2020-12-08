#!/usr/bin/python

#      _   _ _
#     | | | | |        Heloisa Lazari
#     | |_| | |        GitHub: Hello-Helo/SecretSanta_Emailer
#     |  _  | |___     heloisalbento@usp.br | heloisalbento@gmail.com
#     |_| |_|_____|
#                      Fork of: eformo/secret_santa_emailer
#

import os
import random


# Secret Santa picker
def pick_recipient(group, recipient, single_flag):
    # Chose the Santee for each Secret Santa
    for person in group:
        # print(person)
        gift = random.choice(recipient)
        # Check if the Santee picked is valid
        if single_flag == 0:
            while gift in group:
                gift = random.choice(recipient)
        else:
            while gift in person:
                gift = random.choice(recipient)
        recipient.remove(gift)
        mail_list.append("%s=%s" % (person, gift))
    return recipient


# Send mail
def mail():
    print("Pairing complete!")
    verbose = input("Send mails? (Y/n) ")
    if verbose == "n":
        exit(1)
    elif (verbose == "y") or (verbose == "Y") or (verbose == ""):
        for item in mail_list:
            sep = item.split("=")
            pfrom = sep[0].split(":")
            pto = sep[1].split(":")
            # This is what will be in the email body
            # The first '%s' corespond to the Santa, and the second to the Santee
            os.system(
                "echo HoHoHo %s! You will be buying a gift for %s this year. The decided limit is \$50. > test.txt"
                % (pfrom[0], pto[0])
            )
            # Put here the path to this program directory
            # Change to your mail progras (Mutt, Neomutt...)
            cmd = (
                "neomutt -e 'set realname='Santa'' -s 'Gift Exchange 2020' -- %s  < ~/path_to/test.txt"
                % pfrom[1]
            )

            os.system(cmd)
            # print(cmd)
    else:
        print("Invalid Input: Please type either y to continue or n to exit")
        exit(2)


# Main
if __name__ == "__main__":
    # Create the list with Santa-Santee pair
    global mail_list
    mail_list = []

    # Create the list with all the participants
    # Put those who can't gift each others side by side
    participants = [
        # "michael: michael@email.com",
        # "dwight: dwight@email.com",
        # "pam: pam@email.com",
        # "jim: jim@email.com"
    ]

    # Create the groups that can't gift each other
    # Put the correct delimiters
    # groupA = participants[:]
    # groupB = participants[:]

    # Put everyone with no limitations together
    single = participants[:]

    # Create a list with participants without Santas
    possible_recipients = participants

    # Pick the Santa-Santee pair
    # Do the closed groups first
    # possible_recipients = pick_recipient(groupA, possible_recipients, 0)
    # possible_recipients = pick_recipient(groupB, possible_recipients, 0)

    # The singles Santa-Santee pair
    possible_recipients = pick_recipient(single, possible_recipients, 1)

    # The pairs, print for tests
    # print(mail_list)

    mail()
