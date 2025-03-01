import random

words = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
inputgirisi = int(input("Parola uzunluğu: "))

yeniparola = ""
for i in range(inputgirisi):
    yeniparola += random.choice(words)
print(yeniparola)
