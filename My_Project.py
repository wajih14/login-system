import json

sign_or_log = input("enter (l) to log in or (s) to sign up")

if sign_or_log == "s":
    username = input("enter your username")
    password = input("create a password")
    while len(password) < 8:
        print("the password should be more than 8 digits")
        password = input("create a password")
    re_password = input("re-enter the password")
    while re_password != password:
        print("confirm your password")
        re_password = input("re-enter the password")
    email = input("enter your email")
    checker = 0
    for i in email:
        if i == "@":
            checker += 1
        elif i == ".":
            checker += 1
    while checker != 2:
        checker = 0
        email = input("enter your email")
        for i in email:
            if i == "@":
                checker += 1
            elif i == ".":
                checker += 1
    infos = {}
    infos['username'] = username
    infos['email'] = email
    infos['password'] = password
    with open('infos.json', 'w')as t:
        json.dump(infos, t)
    print('you have successfully registred')

elif sign_or_log == "l":
    with open('infos.json', 'r') as f:
        dic = json.load(f)
    username = input('enter the username')
    while dic['username'] != username:
        username = input('enter the correct username')
    email = input('enter the email')
    while dic['email'] != email:
        email = input('enter the correct email')
    password = input("enter the password")
    while dic['password'] != password:
        password = input("enter correctly the password")

    print('You have succefully logged in')
