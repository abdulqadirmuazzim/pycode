# A PROGRAM TO HACK A PASSWORD

from som import rand, Password
import subprocess as sub

ano = Password

num = 0

file = []

for it in ano:
    print("Searching...")
    while len(file) == num:
        process = sub.run(['python', 'som.py'],
                          capture_output=True, text=True)
        com = [file.append(val) for val in process.stdout if val == it]
        if com:
            print(f"found {process.stdout}")
            break
    num += 1

output = ''.join(file)

print(f'your password is {output}')
