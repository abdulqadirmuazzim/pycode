from pathlib import Path

way = Path(r'C:\Users\King_Abdul\text\run.py')
fade = Path(r'C:\Users\King_Abdul\text\som.py')


with open("run", 'a') as file:
    dip = way.read_text()
    file.write(str(dip))
    print(dip)

with open("som", 'a') as file:
    f = fade.read_text()
    file.write(str(f))
    print(f)
