# SecretSanta_Emailer

This Secret Santa Emailer is a script written in Python3 for everyone who can't meet in person and don't want to use those websites with logins and passwords. To use this you will need a list of all the participants emails and a way to send emails from the command line (like mutt or neomutt).

# Instructions

## Adding the participants

To add the participants, you need to edit the array `participants` in the 72nd line on code, their name comes first and after a colon their emails.
You should do like the example bellow:

```
participants = [
    "michael: michael@email.com",
    "dwight: dwight@email.com",
    "pam: pam@email.com",
    "jim: jim@email.com"
]
```

If you don't want a group of people been each other Secret Santa, like couples and close family, just make sure they are next to each other in the participants list (take note of their position) and you can create a group so this won't happen.
You just need to uncomment the 81st (and add the correct positions in this line) and 92nd lines so it matches your groups:

```
# jim & pam
groupA = participants[3:4]
```

```
possible_recipients = pick_recipient(groupA, possible_recipients, 0)
```

You can add as many groups as you want, just copy this lines and change the group name.


## Sending the email

There is 2 lines in the code that you may need to change, both of them are in the `mail` function.

The first one (47th) is the body of the email, you can edit to be the way you want to. The way the code is right now, the first `%s` will be the Secret Santa, and the second will be the Santee. If you wish to change the order they appear, you need to chenge the line bellow to `% (pto[0], pfrom[0])`.

The second one (53rd) is the command to send the email, the way it is set the mail will be sent from neomutt, you can change it to be the email client you are using.

# Picking the Secret Santa - Santee pair

Now, you can just run `santa.py`, and you can sent the emails! Enjoy and Happy Holidays!

#### Fork of: eformo/secret_santa_emailer
