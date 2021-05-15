'''
Changelog:
1.1 
- Backport to Python < 3.10
1.0
- Initial Release
'''
from pyotp import TOTP
from json import load, dump
from os.path import exists
print("BE CAREFUL! CODES ARE STORED UNENCRYPTED!")
if exists("codes.json"):
    db = load(open("codes.json"))
else:
    db = None
print("What do you want to do?")
print("1. Enter Code")
print("2. Authenticate")
print("3. Delete code")
'''
while True:
    match input(">"):
        case "1":
            print("Let's do this!")
            code = input("What is the 32-character code?")
            name = input("What is this code's name?")
            print("Great.")
            if db:
                db["codes"].append({"code":code, "name":name})
                dump(db, open("codes.json", 'w')) 
            else:
                db = {"codes":[{"code":code, "name":name}]}
                dump(db, open("codes.json", 'w'))
        case "2":
            print("Let's do this!")
            print("Please press the key corresponding to the code you want to authenticate for")
            index = 0
            for code in db["codes"]:
                print(f"{index}: {code['name']}")
            code = db[input(">")]
            print("Great.")
            print("The code is:")
            print(TOTP(code['code']).now())
        case "3":
            print("I can't let you do that")
        case _:
            print("How am I supposed to do that?")
'''
while True:
    cmd = input(">")
    if cmd == "1":
        print("Let's do this!")
        code = input("What is the 32-character code?")
        name = input("What is this code's name?")
        print("Great.")
        if db:
            db["codes"].append({"code":code, "name":name})
            dump(db, open("codes.json", 'w')) 
        else:
            db = {"codes":[{"code":code, "name":name}]}
            dump(db, open("codes.json", 'w'))
    elif cmd == "2":
        print("Let's do this!")
        print("Please press the key corresponding to the code you want to authenticate for")
        index = 0
        for code in db["codes"]:
            print(f"{index}: {code['name']}")
        code = db["codes"][int(input(">"))]
        print("Great.")
        print("The code is:")
        print(TOTP(code['code']).now())
    elif cmd == "3":
        print("I can't let you do that")
    else:
        print("How am I supposed to do that?")