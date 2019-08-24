import json


with open('f.json') as f:
    file = json.load(f)
    def add():

        name = input("Enter name\n")
        date = input("Enter date\n")
        file[name] = date
    def loop():
        i = input("To Add another birthdate type 'yes' or 'no' to exit\n")
        while i == 'yes':
            if i == 'yes':
                add()
                i = input("To Add another birthdate type 'yes' or 'no' to exit\n")
            elif i == 'no':
                break

        with open('f.json', 'w') as f:
            json.dump(file, f)

a = input("Enter name of person:\n")
print("The birthday is on")
date = file[a]
print(date)
loop()