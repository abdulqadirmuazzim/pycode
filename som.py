import random as rd
import string

rand = "".join(rd.choice(string.ascii_letters + string.digits))
Password = "".join(rd.choices(string.ascii_letters + string.digits, k=20))
# ano = '0HFICxyeJvOCNl4b2kTBc6MbGI5ZrNq9'
# file = [1, 3, 4, 5]

print(rand)
