import random
import sys
args = sys.argv
lowercase = 'qwertyuiopasdfghjklzxcvbnm'
capitalize_letter = lowercase.upper()
symbols = r"""!@#$%^&*()-_=+[]{};:'",<.>/?|"""
num = '123456789'
print("Generate password: "+"".join(random.sample(list(lowercase + capitalize_letter + symbols + num), int(args[1]))))
