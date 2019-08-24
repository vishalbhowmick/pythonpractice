open_file=open('fil','a')
print('enter')
while True:
    try:
        line = input()
    except EOFError:
        break

open_file.writelines(line)
open_file.close()