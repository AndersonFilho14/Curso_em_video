from random import randint
pc = randint(0,10)
user = int(input("Numero ate 10\n"))
i =0
while pc != user:
    if user > pc:
        print('Chutou alto')

    else:
        print('Chutou baixo')
    user = int(input("Outro chute\n"))
    i += 1
print(f"O numero de tentativas para acerta foi de: {i}")